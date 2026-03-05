import json
from src.evaluator import evaluate_response

MODEL_NAME = "example_model"

results = []

with open("../dataset/adversarial_prompts.jsonl") as f:

    for line in f:

        test = json.loads(line)

        prompt = test["prompt"]

        # Replace this with real model call later
        response = "placeholder response"

        verdict = evaluate_response(response, test["expected"])

        results.append({
            "model": MODEL_NAME,
            "test": test["id"],
            "category": test["category"],
            "verdict": verdict
        })

print(results)
