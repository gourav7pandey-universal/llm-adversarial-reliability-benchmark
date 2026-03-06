import json
from src.evaluator import evaluate_response
from src.metrics import compute_failure_rates
from transformers import pipeline


MODEL_NAME = "flan-t5-base"

model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


def load_dataset():

    dataset = []

    with open("../dataset/adversarial_prompts.jsonl") as f:

        for line in f:
            dataset.append(json.loads(line))

    return dataset


def model_response(prompt):

    output = model(prompt, max_length=50)

    return output[0]["generated_text"]


def run_benchmark():

    dataset = load_dataset()

    results = []

    for test in dataset:

        prompt = test["prompt"]

        response = model_response(prompt)

        verdict = evaluate_response(response, test["expected"])

        results.append({
            "model": MODEL_NAME,
            "test": test["id"],
            "category": test["category"],
            "verdict": verdict
        })

    return results


def save_results(results):

    with open("../results/example_results.json", "w") as f:
        json.dump(results, f, indent=2)


def main():

    results = run_benchmark()

    save_results(results)

    metrics = compute_failure_rates(results)

    print("\nBenchmark Summary\n")

    print("{:<15} {:<25} {:<10}".format("Model", "Category", "Failure Rate"))
    print("-" * 50)

    for m in metrics:
        print("{:<15} {:<25} {:<10}".format(
            m["model"],
            m["category"],
            m["failure_rate"]
        ))


if __name__ == "__main__":

    main()
