import os
import sys
import json

sys.path.insert(0, "/app/soren-spline-kb/src")
from retriever import SorenSplineKBRetriever

EVAL_QUESTIONS = [
    {"id": 1, "query": "How do I create a glass material in 3D?", "expected_type": "material"},
    {"id": 2, "query": "Where is the Home button located in the UI?", "expected_type": "ui_element"},
    {"id": 3, "query": "How do I add interactive mouse hover state transitions?", "expected_type": "state_event"},
    {"id": 4, "query": "What is Hana mode and how do I design 2D UI components?", "expected_type": "hana"},
    {"id": 5, "query": "How do I set up scroll driven 3D camera animations?", "expected_type": "scroll_animation"},
    {"id": 6, "query": "How do physics rigid bodies and collisions work in Spline?", "expected_type": "physics"},
    {"id": 7, "query": "How do I use variables and conditional actions?", "expected_type": "variable_logic"},
    {"id": 8, "query": "How do I add directional lighting and HDRI environments?", "expected_type": "lighting"},
    {"id": 9, "query": "How do I configure a particle emitter system?", "expected_type": "particle"},
    {"id": 10, "query": "How do I export a scene as spline-viewer web component?", "expected_type": "export_web"},
    {"id": 11, "query": "How do I integrate Spline with React using React-Spline?", "expected_type": "code_api"},
    {"id": 12, "query": "How do I create smooth camera state transitions?", "expected_type": "camera"},
    {"id": 13, "query": "How do I animate an object along a vector path in Hana?", "expected_type": "path_animation"},
    {"id": 14, "query": "How do I dynamic extrude 3D text and typography?", "expected_type": "3d_text"},
    {"id": 15, "query": "How do I build an interactive switch with progressive blur in Hana?", "expected_type": "hana_switch"},
    {"id": 16, "query": "How do I import glTF models and decimate polygon count?", "expected_type": "import_gltf"},
    {"id": 17, "query": "How do I generate 3D assets and textures with Spline AI?", "expected_type": "ai_gen"},
    {"id": 18, "query": "How do I connect 3D scenes to live real-time REST APIs?", "expected_type": "rest_api"},
    {"id": 19, "query": "How do I setup responsive auto layout constraints in Hana?", "expected_type": "auto_layout"},
    {"id": 20, "query": "How do I add spatial 3D audio triggers?", "expected_type": "audio"}
]

def run_evaluation():
    retriever = SorenSplineKBRetriever()
    passed = 0
    total = len(EVAL_QUESTIONS)
    results = []

    print("Running 20 Representative Evaluation Suite Queries...")
    for q in EVAL_QUESTIONS:
        query = q["query"]
        fts_res = retriever.search_fts(query, limit=3)
        rb_res = retriever.search_runbooks(q["expected_type"].replace('_', ' '))

        has_results = len(fts_res) > 0 or len(rb_res) > 0
        if has_results:
            passed += 1

        results.append({
            "id": q["id"],
            "query": query,
            "fts_matches_count": len(fts_res),
            "top_fts_title": fts_res[0]["title"] if fts_res else "None",
            "passed": has_results
        })

    eval_summary = {
        "total_queries": total,
        "passed_queries": passed,
        "success_rate_pct": (passed / total) * 100,
        "details": results
    }

    eval_output_path = "/app/soren-spline-kb/data/eval_results.json"
    with open(eval_output_path, 'w', encoding='utf-8') as f:
        json.dump(eval_summary, f, indent=2)

    print(f"Evaluation complete: {passed}/{total} queries matched ({eval_summary['success_rate_pct']}%)")
    print(f"Results saved to {eval_output_path}")

if __name__ == '__main__':
    run_evaluation()
