# LLM Adversarial Reliability Benchmark

This repository contains a simple benchmark for evaluating how language models behave under adversarial prompts.

The benchmark tests several failure categories such as:

- hallucination
- prompt injection
- safety violations
- constraint following
- citation fabrication
- reasoning consistency
- policy boundary adherence

The goal of this project is to provide a lightweight framework for testing model reliability.

---

## Repository Structure

dataset/  
Contains adversarial prompts used for testing.

src/  
Contains the evaluation logic and scoring functions.

notebooks/  
Contains the script that runs the benchmark.

results/  
Stores benchmark outputs.

---

## Running the Benchmark

To run the benchmark locally, follow these steps.

Step 1 — Clone the repository

git clone https://github.com/gourav7pandey-universal/llm-adversarial-reliability-benchmark

Then move into the project folder:

cd llm-adversarial-reliability-benchmark


Step 2 — Install required libraries

pip install -r requirements.txt


Step 3 — Run the benchmark

python notebooks/run_benchmark.py


The script will:

- load the adversarial prompt dataset
- generate model responses
- evaluate them using the scoring logic
- compute failure rates
- save the results in the results/ folder

---

## Safety Note

Some prompts reference harmful or illegal activities.
They are included only to test whether language models appropriately refuse unsafe requests.

This benchmark does not provide instructions for harmful activities.

---

## Purpose

This project explores how adversarial prompts can expose reliability weaknesses in language models and provides a lightweight framework for evaluating them.

## Example Benchmark Output

After running the benchmark, the script prints failure rates for each category.

Example output:

- example_model - hallucination failure rate: 0.33
- example_model - prompt_injection failure rate: 0.10
- example_model - safety failure rate: 0.00
- example_model - constraint failure rate: 0.20
- example_model - citation_fabrication failure rate: 0.15

These results are also saved in the `results/` directory as JSON files.
