import csv
import os
import pandas as pd

from src.helpers.path_helper import make_dir


def read_raw_file(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(
        file_path,
        header=None,
        delimiter='\t',
        skip_blank_lines=False
    )
    
    return df


def transform_raw_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={0: 'translation'})
    df = df.assign(source=df['translation'])
    df['can_modify'] = 1
    
    return df


def save_df(df: pd.DataFrame, file_path: str) -> None:
    file_name, _ = os.path.splitext(file_path)
    new_file_path = f'{file_name}.csv'
    make_dir(os.path.dirname(file_path))
    
    df.to_csv(
        new_file_path,
        index=False,
        header=True,
        encoding='utf-8',
        quoting=csv.QUOTE_ALL
    )
