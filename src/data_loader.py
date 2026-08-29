import pandas as pd
from pathlib import Path


# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folder path
DATA_DIR = BASE_DIR / "data"


def load_maintenance_tasks():
    """Load maintenance tasks dataset."""
    file_path = DATA_DIR / "maintenance_tasks.csv"
    return pd.read_csv(file_path)


def load_train_schedule():
    """Load train schedule dataset."""
    file_path = DATA_DIR / "train_schedule.csv"
    return pd.read_csv(file_path)


def load_goods_forecast():
    """Load goods forecast dataset."""
    file_path = DATA_DIR / "goods_forecast.csv"
    return pd.read_csv(file_path)


def load_corridor_config():
    """Load corridor configuration dataset."""
    file_path = DATA_DIR / "corridor_config.csv"
    return pd.read_csv(file_path)


def load_resources():
    """Load resources dataset."""
    file_path = DATA_DIR / "resources.csv"
    return pd.read_csv(file_path)


def load_all_data():
    """Load all datasets and return them as a dictionary."""

    data = {
        "maintenance_tasks": load_maintenance_tasks(),
        "train_schedule": load_train_schedule(),
        "goods_forecast": load_goods_forecast(),
        "corridor_config": load_corridor_config(),
        "resources": load_resources()
    }

    return data
