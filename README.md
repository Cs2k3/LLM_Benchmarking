# 🧪 LLM Benchmarking Tool

This project benchmarks the performance of open-source LLMs (like LLaMA 3.1 8B, Qwen 2.5, and Gemma 2B) on local hardware.

## 📌 Features
- Benchmark LLMs for latency, memory usage, and tokens-per-minute (TPM)
- Lightweight benchmarking script for local environments
- YAML-based config system for easy model switching
- Results logging (coming soon)

## 📂 Folder Structure
```
LLM_Benchmarking/
├── configs/         # YAML config files
├── models/          # Pre-downloaded models (not versioned)
├── results/         # Benchmark logs/output
├── scripts/         # Python benchmark logic
├── requirements.txt # Dependency list
└── README.md
```

## 🚀 Setup Instructions

### 1. Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate   # Mac/Linux
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Benchmark
```bash
cd scripts
python run_all.py
```

## 🧹 Important: Exclude Large Files

This repo **does not** track:
- `venv/`
- `.pyc`, `.pkl`, `.log`
- Model binaries

> Make sure your `.gitignore` file includes these to avoid GitHub push issues.

## 🧠 Models in Use
```yaml
- meta-llama/Llama-3-8B-Instruct
- Qwen/Qwen-2B-Instruct
- google/gemma-2b-it
```

## 📜 License
MIT License © 2025
