
import psutil
import time
import torch

def measure_memory():
    process = psutil.Process()
    mem_bytes = process.memory_info().rss
    return round(mem_bytes / (1024 ** 2), 2)  # MB

def measure_latency_and_tpm(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
    start_time = time.time()
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=50)
    end_time = time.time()
    elapsed = end_time - start_time
    generated_tokens = output.shape[-1]
    tpm = (generated_tokens / elapsed) * 60
    return elapsed, tpm
