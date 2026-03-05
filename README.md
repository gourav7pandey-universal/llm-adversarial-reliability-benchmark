# LLM Adversarial Reliability Benchmark

This repository contains a simple benchmark for evaluating how language models behave under adversarial prompts.

The benchmark tests several failure categories such as:

- hallucination
- prompt injection
- safety violations
- constraint following
- citation fabrication

The goal of this project is to provide a lightweight framework for testing model reliability.

## Repository Structure

dataset/
Contains adversarial prompts used for testing.

src/
Contains the evaluation logic and scoring functions.

notebooks/
Contains the script that runs the benchmark.

results/
Stores benchmark outputs.

## Running the Benchmark

1. Clone the repository
2. Install dependencies
3. Run the benchmark script
pip install -r requirements.txt
python notebooks/run_benchmark.py

## Safety Note

Some prompts reference harmful activities.  
They are included only to test whether models refuse unsafe requests.
