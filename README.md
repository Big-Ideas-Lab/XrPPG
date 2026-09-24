# XrPPG: Region-Aware Remote Photoplethysmography

Official PyTorch implementation of **XrPPG**: Region-Aware Domain Adaptation and Contrastive Alignment for Remote Photoplethysmography (rPPG).

---

## 📁 Repository Structure

```
XrPPG/
├── run_regions.sh          # Main script to run region-aware training & evaluation
├── train_regions.py        # Region-aware training with InfoNCE contrastive alignment
├── eval_from_bvp.py        # Post-training evaluation on BVP waveforms (FFT / PSD HR metrics)
├── config.py               # Central project configuration & dataset path management
├── model.py                # Neural network architectures (rPPGNet, TemporalAwareStem, etc.)
├── MyDataset.py            # Dataset loader, spatial/temporal augmentations & index generation
├── MyLoss.py               # Loss functions: Pearson loss, Spectral loss, InfoNCE loss
├── utils/
│   ├── __init__.py
│   ├── core.py             # CLI parser, Logger, and general utilities
│   ├── train_utils.py      # Waveform sorting (wave_sort_from_index) & figure visualization
│   ├── eval_utils.py       # FIR filtering, FFT heart rate metrics, summary logging
│   └── mlflow_utils.py     # MLflow experiment tracking integration
├── environment.yml         # Conda environment specification
├── requirements.txt        # Pip dependencies
└── .gitignore              # Clean gitignore for logs, caches, and checkpoints
```

---

## ⚙️ Installation

### Option 1: Using Conda (Recommended)

```bash
# Clone the repository
git clone https://github.com/Big-Ideas-Lab/XrPPG.git
cd XrPPG

# Create and activate conda environment
conda env create -f environment.yml
conda activate xrppg
```

### Option 2: Using Pip

```bash
pip install -r requirements.txt
```

---

## 🗂️ Dataset Layout

XrPPG expects spatial-temporal maps (STMaps) organized by dataset domain (e.g. `PURE_my`, `UBFC_my`, `BUAA_my`) and region subfolders (`*_rm`, `*_in`, `*_eye`):

```
STMap_my/
├── PURE_my_in/
│   ├── 01-01/
│   │   ├── STMap/STMap_RGB.png
│   │   └── Label/BVP.mat, Label/HR.mat
├── UBFC_my_in/
│   └── ...
└── BUAA_my_in/
    └── ...
```

> **Note**: You can customize the dataset location by setting the environment variable `STMAP_PARENT_ROOT` or `STMAP_DATA_ROOT`, e.g.:
> ```bash
> export STMAP_PARENT_ROOT=/path/to/dataset/parent_dir
> ```

---

## 🚀 Running Training and Evaluation

### 1. Run the Full Cross-Dataset Benchmark

Execute all cross-dataset evaluation pairs using `run_regions.sh`:

```bash
bash run_regions.sh
```

### 2. Run a Single Domain Adaptation Pair

To train from source domain (e.g., `BUAA_my_in`) to target domain (e.g., `PURE_my_in`) with InfoNCE alignment:

```bash
python train_regions.py \
  --src 'BUAA_my_in' \
  -t 'PURE_my_in' \
  --regions all \
  --tau-info 0.05 \
  --weight_info 0.01 \
  --GPU 0
```

### 3. Evaluate Predictions

Evaluate saved BVP waveforms and compute Heart Rate metrics (MAE, RMSE, Std, ME):

```bash
python eval_from_bvp.py
```

Results are logged to `Training_Log/regions_eval_summary.csv` and saved under `Wave_sort/<test_domain>/.../feature/`.

---

## 📊 Evaluation Metrics

Evaluation calculates:
- **ME** (Mean Error in BPM)
- **Std** (Standard Deviation of Error)
- **MAE** (Mean Absolute Error in BPM)
- **RMSE** (Root Mean Square Error in BPM)

---

## 📜 License

This project is released under the [MIT License](LICENSE).
