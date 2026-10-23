# SOREN V3 Preview — validate and install a replacement gateway JWT.
# The embedded anon JWT is a PUBLISHABLE key used only as a signature-verification fixture.
# NEVER paste the Supabase Legacy JWT Secret into chat or a command-line argument.
param([switch]$SelfTest)
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'

$ProjectRef='xoyefnfesvrqsohuppxe'
$WorkspaceId='bc7390e8-2908-4677-beed-c1677acf7266'
$PublicLegacyAnonJwt='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhveWVmbmZlc3ZycXNvaHVwcHhlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI2OTM1NTgsImV4cCI6MjEwODI2OTU1OH0.TTp_otyWypno4YURbHRyCuxR0XinyFlMs7m3jJm9-Kc'
$Project='prj_n1PULnMPv3uCy1Df7qBCnKBRzNNp'
$Team='sorensadr-gmailcoms-projects'

function To-Base64Url {
    param([Parameter(Mandatory=$true)][byte[]]$Bytes)
    return [Convert]::ToBase64String($Bytes).TrimEnd('=').Replace('+','-').Replace('/','_')
}
function From-Base64Url {
    param([Parameter(Mandatory=$true)][string]$Text)
    $s=$Text.Replace('-','+').Replace('_','/')
    $s+='=' * ((4-$s.Length%4)%4)
    return [Convert]::FromBase64String($s)
}
function Get-HmacB64 {
    param([byte[]]$Key,[string]$Content)
    $mac=[Security.Cryptography.HMACSHA256]::new($Key)
    $bytes=$null
    try {
        $bytes=$mac.ComputeHash([Text.Encoding]::ASCII.GetBytes($Content))
        return To-Base64Url $bytes
    } finally {
        $mac.Dispose()
        if($null -ne $bytes){[Array]::Clear($bytes,0,$bytes.Length)}
    }
}
function New-SignedJwt {
    param([byte[]]$Key,[object]$Claims)
    $header=[ordered]@{alg='HS256';typ='JWT'}
    $h=To-Base64Url ([Text.Encoding]::UTF8.GetBytes((ConvertTo-Json -InputObject $header -Compress)))
    $p=To-Base64Url ([Text.Encoding]::UTF8.GetBytes((ConvertTo-Json -InputObject $Claims -Compress -Depth 12)))
    $data=$h+'.'+$p
    $signature=Get-HmacB64 -Key $Key -Content $data
    return $data+'.'+$signature
}
function Test-Signature {
    param([byte[]]$Key,[string]$Jwt)
    $parts=$Jwt.Split('.')
    if($parts.Count -ne 3){return $false}
    $expected=Get-HmacB64 -Key $Key -Content ($parts[0]+'.'+$parts[1])
    return [string]::Equals($expected,$parts[2],[StringComparison]::Ordinal)
}

if($SelfTest) {
    $dummy=[Text.Encoding]::UTF8.GetBytes('soren-dummy-fixture-key-do-not-use-for-production-98765')
    $wrong=[Text.Encoding]::UTF8.GetBytes('soren-another-incorrect-dummy-signing-key-98765')
    try {
        $fakeAnon=New-SignedJwt -Key $dummy -Claims ([ordered]@{role='anon';iat=1735689600;exp=1735693200})
        if(-not (Test-Signature -Key $dummy -Jwt $fakeAnon)){throw 'Test FAIL: valid secret not accepted'}
        if(Test-Signature -Key $wrong -Jwt $fakeAnon){throw 'Test FAIL: incorrect secret accepted'}
        $clock=[long]1735689600
        $claims=[ordered]@{role='soren_gateway';workspace_id=$WorkspaceId;iss="https://$ProjectRef.supabase.co/auth/v1";aud='authenticated';iat=$clock;exp=($clock+604800)}
        $token=New-SignedJwt -Key $dummy -Claims $claims
        if(-not(Test-Signature -Key $dummy -Jwt $token)){throw 'Test FAIL: gateway signature wrong'}
        $segments=$token.Split('.')
        $decoded=[Text.Encoding]::UTF8.GetString((From-Base64Url $segments[1]))|ConvertFrom-Json
        if($decoded.role -cne 'soren_gateway' -or $decoded.workspace_id -cne $WorkspaceId -or $decoded.exp -ne $clock+604800){throw 'Test FAIL: gateway claims invalid'}
        Write-Host 'PASS: valid fixture secret, rejection of wrong secret, HS256 signing, workspace and seven-day expiration.' -ForegroundColor Green
        Write-Host 'Self-test used dummy keys only; NO network calls or Vercel writes.'
    } finally {
        [Array]::Clear($dummy,0,$dummy.Length)
        [Array]::Clear($wrong,0,$wrong.Length)
    }
    return
}

if(-not (Get-Command npx -ErrorAction SilentlyContinue)){throw 'Node/npm missing. Cannot update Preview automatically.'}
Write-Host ''
Write-Host 'SOREN V3 Preview: correct the gateway JWT' -ForegroundColor Cyan
Write-Host "Confirm the dashboard project is $ProjectRef."
Write-Host ("https://supabase.com/dashboard/project/"+$ProjectRef+"/settings/jwt")
Write-Host 'Copy the LEGACY JWT SECRET from that project (not anon or service_role).'
Write-Host 'This script first proves it signs that project public anon JWT.'
Write-Host 'It will refuse to update Vercel if the verification or RPC test fails.' -ForegroundColor Yellow

$secure=Read-Host 'Paste LEGACY JWT SECRET (hidden input)' -AsSecureString
$bstr=[IntPtr]::Zero
$keyBytes=$null
$plain=$null
$gatewayJwt=$null
try {
    $bstr=[Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
    $plain=[Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
    if([string]::IsNullOrWhiteSpace($plain)){throw 'Signing secret is empty.'}
    $keyBytes=[Text.Encoding]::UTF8.GetBytes($plain.Trim())
    $plain=$null
    if($keyBytes.Length -lt 32){throw 'Signing secret is too short; check that you copied the right field.'}
    if(-not (Test-Signature -Key $keyBytes -Jwt $PublicLegacyAnonJwt)) {
        throw "Incorrect Legacy JWT Secret for project $ProjectRef. No JWT generated or uploaded. Copy the secret from this exact project's JWT Settings."
    }
    Write-Host 'PASS: Secret cryptographically matches this Supabase project.' -ForegroundColor Green
    $now=[DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
    $claims=[ordered]@{
        role='soren_gateway'
        workspace_id=$WorkspaceId
        aud='authenticated'
        iss="https://$ProjectRef.supabase.co/auth/v1"
        iat=$now
        exp=($now+604800)
    }
    $gatewayJwt=New-SignedJwt -Key $keyBytes -Claims $claims
    if(-not (Test-Signature -Key $keyBytes -Jwt $gatewayJwt)){throw 'Generated token HMAC verification failed.'}

    $url="https://$ProjectRef.supabase.co/rest/v1/rpc/get_federation_cache"
    $headers=@{apikey=$PublicLegacyAnonJwt;Authorization=('Bearer '+$gatewayJwt)}
    try {
        $probe=Invoke-WebRequest -Uri $url -Method Post -Headers $headers -Body '{"p_key":"soren-gateway-signature-validation-only"}' -ContentType 'application/json' -UseBasicParsing -TimeoutSec 15
    } catch {
        $code='unknown'
        if($_.Exception.Response){$code=[int]$_.Exception.Response.StatusCode}
        throw "Supabase rejected the signed gateway JWT (HTTP $code). No Vercel setting changed. Check which JWT signing keys are trusted."
    } finally {
        $headers.Clear()
    }
    if([int]$probe.StatusCode -ne 200){throw "Unexpected Supabase RPC status $($probe.StatusCode). No Vercel setting changed."}
    Write-Host 'PASS: Supabase accepted the signed gateway JWT and authorized the restricted read-only RPC.' -ForegroundColor Green
    Write-Host 'Updating SOREN_GATEWAY_DB_KEY in Vercel Preview only...'
    $gatewayJwt | & npx --yes vercel@65.1.0 env update SOREN_GATEWAY_DB_KEY --environment preview --project $Project --scope $Team --yes --sensitive
    if($LASTEXITCODE -ne 0){throw "Vercel CLI update failed with exit code $LASTEXITCODE."}
    Write-Host 'SUCCESS: Preview gateway JWT updated. Seven-day expiry:' -ForegroundColor Green
    Write-Host ([DateTimeOffset]::FromUnixTimeSeconds($now+604800).UtcDateTime.ToString('u'))
    Write-Host 'Nothing was sent to chat or saved to a plaintext credential file.'
} finally {
    $gatewayJwt=$null
    $plain=$null
    if($bstr -ne [IntPtr]::Zero){[Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)}
    if($null -ne $keyBytes){[Array]::Clear($keyBytes,0,$keyBytes.Length)}
    if($null -ne $secure){$secure.Dispose()}
}
