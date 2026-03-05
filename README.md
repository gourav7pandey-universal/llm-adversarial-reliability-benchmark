# llm-adversarial-reliability-benchmark
Adversarial evaluation harness for testing LLM reliability, hallucination resistance, prompt injection robustness, and safety boundary adherence.
## Safety Note

This dataset contains adversarial prompts that reference harmful or illegal activities.
These prompts are included solely for the purpose of evaluating whether language models
appropriately refuse unsafe requests.

The benchmark does not encourage, endorse, or provide instructions for harmful activities.
All such prompts are expected to trigger refusal responses from evaluated models.

# LLM Adversarial Reliability Benchmark

A lightweight benchmark for evaluating the reliability and safety behavior of large language models under adversarial prompts.

This repository provides a small evaluation harness that tests how language models respond to prompts designed to expose common failure modes.

The goal is to make it easy to evaluate models across categories such as hallucination resistance, prompt injection robustness, safety boundary adherence, and instruction following.

---

## Evaluation Categories

The dataset includes adversarial prompts across several reliability dimensions:

- Hallucination resistance  
- Prompt injection robustness  
- Safety violation refusal  
- Constraint following  
- Citation fabrication detection  
- Reasoning consistency  
- Policy boundary adherence  

Each prompt includes an expected behavior (for example: refusal).

---

## Repository Structure

