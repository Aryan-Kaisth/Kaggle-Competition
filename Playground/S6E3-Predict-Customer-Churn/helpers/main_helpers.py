from pathlib import Path
import pandas as pd


def load_train_data() -> pd.DataFrame:
    ROOT_PATH = Path.cwd()
    file_name = 'data/train.csv'
    return pd.read_csv(ROOT_PATH / file_name)

def load_test_data() -> pd.DataFrame:
    ROOT_PATH = Path.cwd()
    file_name = 'data/test.csv'
    return pd.read_csv(ROOT_PATH / file_name)