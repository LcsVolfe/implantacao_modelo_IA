import pandas as pd


def load_dataset(path='assets/dataset.csv'):
    df = pd.read_csv(path, header=None, on_bad_lines='skip')
    return df
