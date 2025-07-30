import subprocess
import time
import yaml
import csv
import os

def load_models_from_yaml(path):
    with open(path, "r") as file:
        data = yaml.safe_load(file)
    return data["models"]

def benchmark_model(model_name, prompt):
    start_time = time.time()

    try:
        result = subprocess.run(
    ["ollama", "run", model_name, prompt],
    capture_output=True,
    text=True,
    encoding="utf-8",         # <--- Fix: force UTF-8
    errors="replace",         # <--- Replace any unreadable chars
    timeout=300
)

        latency = time.time() - start_time
        output = result.stdout
        tpm = len(output.split()) / (latency / 60) if latency > 0 else 0
        return round(latency, 2), round(tpm, 2), "Success"

    except Exception as e:
        return 0, 0, f"Failed: {str(e)}"

def main():
    models = load_models_from_yaml("../configs/models.yaml")

    os.makedirs("../results", exist_ok=True)
    results_path = "../results/benchmark_results.csv"

    with open(results_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Model", "Latency (s)", "TPM", "Status"])

        for model in models:
            print(f"\n[INFO] Benchmarking {model['label']}")
            latency, tpm, status = benchmark_model(model["name"], model["prompt"])
            print(f"[RESULT] Latency: {latency}s, TPM: {tpm}, Status: {status}")
            writer.writerow([model["label"], latency, tpm, status])

if __name__ == "__main__":
    main()
