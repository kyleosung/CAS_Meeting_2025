import os
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "../data"
MODEL_DIR = BASE_DIR / "./models"
IMG_DIR = BASE_DIR / "./img"

ORIGINAL_DATASET = DATA_DIR / "Predictive Modeling Dataset.csv"

COVERAGE_TYPES = [
    "Personal Property",
    "Additional Living Expense",
    "Guest Medical",
    "Liability",
]

BINARY_COLUMNS = ["greek", "off_campus", "gender", "sprinklered", "holdout"]

SEED = 42
