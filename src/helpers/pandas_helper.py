import csv
import os
import pandas as pd
import numpy as np

from src.helpers.path_helper import get_all_files, make_dir


def read_raw_file(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(
        file_path,
        header=None,
        delimiter='\t',
        skip_blank_lines=False
    )
    
    return df


def read_csv_file(file_path: str, line_index=0) -> pd.DataFrame:
    df = pd.read_csv(
        file_path,
        header=0,
        dtype=str,
        skipfooter=0,
        engine='python',
        keep_default_na=False,
        skiprows=line_index
    )

    return df


def transform_raw_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={0: 'translation'})
    df = df.assign(source=df['translation'])
    df['can_modify'] = 1
    
    return df


def save_df_csv(
    df: pd.DataFrame | pd.Series,
    file_path: str
) -> None:
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


def save_df_txt(
    df: pd.DataFrame | pd.Series,
    file_path: str
) -> None:
    file_name, _ = os.path.splitext(file_path)
    new_file_path = f'{file_name}.txt'
    make_dir(os.path.dirname(file_path))
    
    with open(new_file_path, 'w', newline='', encoding='utf-8') as file:
        np.savetxt(file, df.values, fmt = "%s", encoding='utf-8')
        
    with open(new_file_path, 'r+', encoding='utf-8') as file:
        file.seek(0, os.SEEK_END)
        file.truncate(file.tell() - 1)


def concatenate_csv_files(folder_path: str) -> pd.DataFrame:
    dfs = []
    
    for file in get_all_files(folder_path):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df = read_csv_file(file_path)
            dfs.append(df)
    
    return pd.concat(dfs, ignore_index=True)
