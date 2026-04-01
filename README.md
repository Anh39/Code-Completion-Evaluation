# Code Completion Evaluation

This repository provides a framework for evaluating code completion models across multiple benchmarks, including both similarity-based and execution-based metrics.

## 📌 Requirements

* Linux (Ubuntu recommended)
* GPU with CUDA installed
* Python 3.11 (or sudo access to install)

---

## ⚙️ Installation

### Step 1: Clone Repository

```bash
mkdir -p /root/workspace
cd /root/workspace

git clone https://github.com/Anh39/Code-Completion-Evaluation temp_repo
mv temp_repo/* temp_repo/.* .
rm -rf temp_repo
```

---

### Step 2: Setup Environment

⚠️ **Important:** Do NOT run all commands at once. Execute them step-by-step.

#### Install Python 3.11 (if not available)

```bash
bash setup_python.sh
```

#### Setup main environment

```bash
bash setup_environment.sh
```

#### Setup execution environment for ExecRepo benchmark

```bash
bash setup_exec.sh
```

---

## 🚀 Usage

Navigate to the `source` directory:

```bash
cd source
```

### Run by Benchmark

* **CCEval**

  ```bash
  bash cceval.sh
  bash cclongeval.sh
  ```

* **RepoEval**

  ```bash
  bash repoeval.sh
  ```

* **HumanEval-Infilling**

  ```bash
  bash human-eval-fim-sim.sh
  bash human-eval-fim-pass.sh
  ```

* **ExecRepoBench**

  ```bash
  bash execrepobench.sh
  ```

---

### Run by Evaluation Metric

* **Code Similarity**

  ```bash
  bash eval_sim.sh
  ```

* **Code Correctness (Pass@1)**

  ```bash
  bash eval_pass.sh
  ```

---

### Run Full Evaluation

```bash
bash eval.sh
```

---

## 📊 Output

If executed successfully, results will be stored in:

```
/root/workspace/outputs
```

---

## 📖 Notes

* Ensure CUDA and GPU drivers are properly configured before running benchmarks.
* Some benchmarks (e.g., ExecRepoBench) require additional execution environments, so make sure all setup scripts are completed. Maximum accuracy for pass@1 is around 83.7% due to some missing environment.

---
