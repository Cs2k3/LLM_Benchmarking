
import yaml
import csv
import os
import time
from transformers import AutoTokenizer, AutoModelForCausalLM
from scripts.utils import measure_memory, measure_latency_and_tpm

def load_models_from_yaml(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)["models"]

def benchmark_model(name, repo_id):
    tokenizer = AutoTokenizer.from_pretrained(repo_id)
    model = AutoModelForCausalLM.from_pretrained(repo_id)
    prompt = "Explain the benefits of using local LLMs."

    latency, tpm = measure_latency_and_tpm(model, tokenizer, prompt)
    memory = measure_memory()
    return latency, tpm, memory

def save_results(name, latency, tpm, memory):
    file_path = "results/benchmark_results.csv"
    header = ["Model", "Latency (s)", "TPM", "Memory (MB)"]
    write_header = not os.path.exists(file_path)
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(header)
        writer.writerow([name, round(latency, 2), round(tpm, 2), memory])

if __name__ == "__main__":
    models = load_models_from_yaml("configs/models.yaml")
    for model_info in models:
        name = model_info["name"]
        repo_id = model_info["repo_id"]
        print(f"\n[INFO] Benchmarking {name}")
        try:
            latency, tpm, memory = benchmark_model(name, repo_id)
            save_results(name, latency, tpm, memory)
            print(f"[RESULT] Latency: {latency:.2f}s, TPM: {tpm:.2f}, Memory: {memory}MB")
        except Exception as e:
            print(f"[ERROR] Failed to benchmark {name}: {e}")
