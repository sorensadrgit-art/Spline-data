# Task Runbook 19: Adding Spatial Audio and Interactive Sound Triggers

## Workflow Overview
Trigger ambient sound effects or 3D positional audio when users interact with scene elements.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- Sound file (`.mp3` or `.wav`).

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `audio_tools` / `event_tools`

## Exact UI Path
1. Right Sidebar -> **Events** -> Add Event (e.g. **Mouse Down** or **Trigger Area / Proximity**).
2. Action -> **Play Sound**.
3. Sound Asset -> Upload audio file or select from library.
4. Sound Settings:
   - Volume (0.0 to 1.0).
   - Loop (Toggle On/Off).
   - Spatial Audio (Toggle On -> Distance attenuation curve).

## Expected Outcomes
- Audio playback triggers instantly upon user interaction or proximity entry.

## Failure Recovery & Common Pitfalls
- **Problem**: Audio fails to play automatically on page load.
- **Fix**: Modern web browsers block unmuted autoplay without user gesture; attach audio trigger to user click/hover event instead.

## Source References
- [Sound Action Docs](https://docs.spline.design/interaction-states-events-and-actions/actions/sound-action)
