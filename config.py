# -*- coding: UTF-8 -*-
"""
XrPPG Configuration File.
Defines paths, dataset mappings, domain adaptation pairs, and hyperparameters.
"""
import os

# ---------- Paths ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(BASE_DIR)

# Dataset root resolution:
# Priority 1: Environment variable STMAP_PARENT_ROOT (or STMAP_DATA_ROOT)
# Priority 2: In current repo (./STMap_my)
# Priority 3: In parent directory (../STMap_my)
# Priority 4: In adjacent NEST-rPPG directory (../NEST-rPPG/STMap_my)
if os.environ.get('STMAP_PARENT_ROOT'):
    STMAP_PARENT_ROOT = os.environ['STMAP_PARENT_ROOT']
elif os.path.isdir(os.path.join(BASE_DIR, 'STMap_my')):
    STMAP_PARENT_ROOT = BASE_DIR
elif os.path.isdir(os.path.join(REPO_ROOT, 'STMap_my')):
    STMAP_PARENT_ROOT = REPO_ROOT
elif os.path.isdir(os.path.join(REPO_ROOT, 'NEST-rPPG', 'STMap_my')):
    STMAP_PARENT_ROOT = os.path.join(REPO_ROOT, 'NEST-rPPG')
else:
    STMAP_PARENT_ROOT = REPO_ROOT

STMAP_DATA_ROOT = os.environ.get('STMAP_DATA_ROOT', os.path.join(STMAP_PARENT_ROOT, 'STMap_my'))
STMAP_DATA_ROOT_REL = './'
STMAP_INDEX_BASE = os.environ.get('STMAP_INDEX_BASE', os.path.join(BASE_DIR, 'STMap_my', 'STMap_Index'))

# Output directories (under XrPPG root)
RESULT_DIR = os.path.join(BASE_DIR, 'Output')
RESULT_LOG_DIR = os.path.join(BASE_DIR, 'Training_Log')
WAVE_SORT_ROOT = os.path.join(BASE_DIR, 'Wave_sort')
MODEL_DIR = os.path.join(BASE_DIR, 'model')

# MLflow tracking (override via MLFLOW_TRACKING_URI / MLFLOW_EXPERIMENT_NAME env vars)
MLFLOW_ARTIFACT_ROOT = os.path.join(RESULT_LOG_DIR, 'mlruns')
MLFLOW_DB_PATH = os.path.join(RESULT_LOG_DIR, 'mlflow.db')
MLFLOW_TRACKING_URI = os.environ.get(
    'MLFLOW_TRACKING_URI',
    'sqlite:///' + os.path.abspath(MLFLOW_DB_PATH),
)
MLFLOW_EXPERIMENT_NAME = os.environ.get('MLFLOW_EXPERIMENT_NAME', 'xrppg')

# ---------- Domain & Training Config ----------
TGT_DOMAIN = 'BUAA_my_in'      # e.g. PURE_my_in, UBFC_my_in, BUAA_my_in
SRC_DOMAIN = 'PURE_my_in'      # single source
SPATIAL_AUG_RATE = 0.5
TEMPORAL_AUG_RATE = 0.1
LOSS_TYPE = 'One'              # One / TA / CM / DM / All
WEIGHT_INFO = 0.0              # InfoNCE alignment weight (0 = disabled)
WEIGHT_INFO_SWEEP = (0.01,)
OPTUNA_TAU_INFO_SWEEP = (0.01, 0.05, 0.1, 0.5)
SEED = 0

# Mapping from target domain to list of source region domains
TARGET_DOMAIN = {
    'VIPL': ['V4V', 'PURE', 'BUAA', 'UBFC'],
    'V4V': ['VIPL', 'PURE', 'BUAA', 'UBFC'],
    'PURE': ['VIPL', 'V4V', 'BUAA', 'UBFC'],
    'BUAA': ['VIPL', 'V4V', 'PURE', 'UBFC'],
    'UBFC': ['VIPL', 'V4V', 'PURE', 'BUAA'],
    'PURE_my': ['BUAA_my', 'UBFC_my'],
    'UBFC_my': ['PURE_my', 'BUAA_my'],
    'UBFC_my_in': ['PURE_my_rm', 'PURE_my_in', 'PURE_my_eye'],
    'PURE_my_in': ['BUAA_my_rm', 'BUAA_my_in', 'BUAA_my_eye'],
    'BUAA_my_in': ['PURE_my_rm', 'PURE_my_rm', 'PURE_my_rm'],
    'BUAA_my_eye': ['UBFC_my_eye', 'UBFC_my_eye', 'UBFC_my_eye'],
}

# Subfolder and STMap file name mappings
FILEA_NAME = {
    # Original STMap folders
    'VIPL': ['STMap/VIPL', 'VIPL', 'STMap_RGB_Align_CSI'],
    'V4V': ['STMap/V4V', 'V4V', 'STMap_RGB'],
    'PURE': ['STMap/PURE', 'PURE', 'STMap'],
    'BUAA': ['STMap/BUAA', 'BUAA', 'STMap_RGB'],
    'UBFC': ['STMap/UBFC', 'UBFC', 'STMap'],
    # STMap_my variants (PURE_my, UBFC_my, BUAA_my)
    'PURE_my': ['STMap_my/PURE_my', 'PURE_my', 'STMap_RGB'],
    'UBFC_my': ['STMap_my/UBFC_my', 'UBFC_my', 'STMap_RGB'],
    'BUAA_my': ['STMap_my/BUAA_my', 'BUAA_my', 'STMap_RGB'],
    # Region / subfolder variants
    'PURE_my_rm': ['STMap_my/PURE_my_rm', 'PURE_my_rm', 'STMap_RGB'],
    'PURE_my_in': ['STMap_my/PURE_my_in', 'PURE_my_in', 'STMap_RGB'],
    'PURE_my_eye': ['STMap_my/PURE_my_eye', 'PURE_my_eye', 'STMap_RGB'],
    'UBFC_my_rm': ['STMap_my/UBFC_my_rm', 'UBFC_my_rm', 'STMap_RGB'],
    'UBFC_my_in': ['STMap_my/UBFC_my_in', 'UBFC_my_in', 'STMap_RGB'],
    'UBFC_my_eye': ['STMap_my/UBFC_my_eye', 'UBFC_my_eye', 'STMap_RGB'],
    'BUAA_my_rm': ['STMap_my/BUAA_my_rm', 'BUAA_my_rm', 'STMap_RGB'],
    'BUAA_my_in': ['STMap_my/BUAA_my_in', 'BUAA_my_in', 'STMap_RGB'],
    'BUAA_my_eye': ['STMap_my/BUAA_my_eye', 'BUAA_my_eye', 'STMap_RGB'],
    'PURE_trans_row0': ['STMap/PURE_trans_row0', 'PURE_trans_row0', 'STMap'],
}

STMAP_NAME = 'STMap_RGB.png'
EXP_NAME = 'PURE_my_region_align'


def get_index_dir(domain: str) -> str:
    """Index dir for a domain (e.g. PURE_my, UBFC_my) under STMAP_INDEX_BASE."""
    return os.path.join(STMAP_INDEX_BASE, domain)


def build_run_name(tgt=None, src=None, weight_info=None):
    """Build rPPGNet run name: rPPGNet_<tgt>_src<src>_w<weight_info>."""
    tgt = tgt or TGT_DOMAIN
    src = src or SRC_DOMAIN
    w = float(WEIGHT_INFO if weight_info is None else weight_info)
    return f"rPPGNet_{tgt}_src{src}_w{'%g' % w}"


def canonical_data_name(domain: str) -> str:
    """Map region-level domain to base dataset name used by MyDataset."""
    if domain.startswith('PURE_my'):
        return 'PURE_my'
    if domain.startswith('UBFC_my'):
        return 'UBFC_my'
    return domain


EVAL_SAVE_PATH = os.path.join(WAVE_SORT_ROOT, TGT_DOMAIN, build_run_name(weight_info=WEIGHT_INFO))
