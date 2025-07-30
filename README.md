# 🧪 Local LLM Benchmarking Tool

## 📌 Project Overview

This project provides a **Local Language Model (LLM) Benchmarking Tool** designed to evaluate the feasibility of running open-source models on local machines. It measures performance metrics such as:

- ⏱ **Latency** – Time taken to generate a response (in seconds)
- 📈 **TPM (Tokens Per Minute)** – Speed of token generation
- 🛠️ **Status** – Success or failure of the benchmark

## 🎯 Objective

> To determine whether running local LLMs is beneficial by benchmarking models like **LLaMA 3.1 8B**, **Qwen 2.5**, and **Gemma 2B** (or their accessible variants), and to assess their latency and throughput on a constrained system **without relying on Hugging Face**.

## ✅ Benchmark Results

| Model        | Latency (s) | TPM   | Status   |
|--------------|-------------|-------|----------|
| LLaMA 3 8B   | 30.91       | 11.65 | ✅ Success |
| Qwen 1.5B    | 1.97        | 0.00  | ✅ Success |
| Gemma 2B     | 110.83      | 8.66  | ✅ Success |

---

## 🧪 How to Run This Benchmark

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Cs2k3/LLM_Benchmarking.git
cd LLM_Benchmarking

 Set Up Python Environment

python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt

cd scripts
python run_all.py


📁 Project Structur

LLM_Benchmarking/
│
├── configs/
│   └── models.yaml        # YAML config for models
│
├── results/
│   └── benchmark_results.csv  # Output results
│
├── scripts/
│   └── run_all.py         # Main benchmark script
│
└── README.md              # You are here


📎 Notes
This project does not require Hugging Face or internet access.

Uses ollama CLI to run models locally.

Designed for minimal resource usage while capturing key benchmarking metrics.

Extendable by simply adding more models to models.yaml.

👨‍💻 Author
GitHub: https://github.com/Cs2k3

🗓 Last updated: 2025-07-29