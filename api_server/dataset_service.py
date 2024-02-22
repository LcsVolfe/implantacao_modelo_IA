import pandas as pd


def load_dataset():
    df = pd.read_csv('assets/dataset.csv', header=None, on_bad_lines='skip')
    return df
