import pandas as pd


def read_data(path: str) -> pd.DataFrame:
    dataframe = pd.read_csv(path)
    return dataframe
