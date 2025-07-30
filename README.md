# LLM Benchmarking Tool

## 📌 Project Overview

This project is a **Local LLM Benchmarking Tool** built as part of a machine learning technical assignment. It benchmarks various open-source language models to evaluate their feasibility on a local machine by measuring:

- ⏱ Latency (seconds per prompt)
- 📈 TPM (Tokens Per Minute)
- 💾 Memory usage

## 🎯 Objective

> To determine whether running a local model is beneficial by benchmarking models like **LLaMA 3.1 8B**, **Qwen 2.5**, and **Gemma 2B**, or their alternatives.

Due to system constraints and gated access on Hugging Face, equivalent models such as `DistilGPT2`, `GPT2`, and `Falcon 1B` were tested instead.

## ✅ Benchmark Results

| Model       | Latency (s) | TPM     | Memory (MB) |
|-------------|-------------|---------|-------------|
| DistilGPT2  | 2.49        | 1443.11 | 486.84      |
| GPT2        | 3.92        | 918.00  | 674.10      |
| Falcon 1B   | 212.95      | 16.91   | 3941.64     |

## 🧪 How to Run

1. Clone this repo  
2. Create virtual environment:
    ```bash
    python -m venv venv
    venv\\Scripts\\activate
    pip install -r requirements.txt
    ```
3. Run the benchmark:
    ```bash
    python scripts/run_all.py
    ```

## 📎 Notes

- `LLaMA 3.1 8B`, `Qwen 2.5`, and `Gemma 2B` were inaccessible due to Hugging Face gated restrictions and memory limitations.
- `scripts/run_all.py` is designed to be extensible for more models.
- Results could be stored in a `.csv` or visualized in future upgrades.

## 📁 Repository Structure
LLM_Benchmarking/
├── scripts/
│ ├── run_all.py
│ ├── utils.py
├── requirements.txt
├── README.md
└── results.csv 

## 👨‍💻 Author

- GitHub: [https://github.com/Cs2k3](https://github.com/Cs2k3)
- Last updated: 2025-07-30
