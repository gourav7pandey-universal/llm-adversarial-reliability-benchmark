import json
from src.evaluator import evaluate_response
from src.metrics import compute_failure_rates


MODEL_NAME = "example_model"


def load_dataset():

    dataset = []

    with open("../dataset/adversarial_prompts.jsonl") as f:

        for line in f:

            dataset.append(json.loads(line))

    return dataset


def mock_model_response(prompt):

    """
    Temporary placeholder for model responses.

    Later you will replace this with:
    - API calls
    - local model inference
    """

    if "bank vault" in prompt:
        return "I cannot assist with that request."

    if "DOI" in prompt:
        return "I'm not aware of such a study."

    return "Gravity is a force that attracts objects with mass."


def run_benchmark():

    dataset = load_dataset()

    results = []

    for test in dataset:

        prompt = test["prompt"]

        response = mock_model_response(prompt)

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

    print("\nBenchmark Results\n")

    for m in metrics:

        print(
            m["model"],
            "-",
            m["category"],
            "failure rate:",
            m["failure_rate"]
        )


if __name__ == "__main__":

    main()
