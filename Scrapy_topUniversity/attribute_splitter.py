import pandas as pd
import re
import os

"""
This script organizes university data from multiple CSV files, extracting information based on attribute types.
The resulting CSV files are stored in folders named after the corresponding years, and each file is named after the attribute type and year.

Instructions:

1. Add all file names to the 'files' list.

"""

files = [
    "cleaned_file_2021.csv",
    "cleaned_file_2022.csv",
    "cleaned_file_2023.csv",
    "cleaned_file_2024.csv",
]


def extract_year_from_filename(filename):
    match = re.search(r"\d{4}", filename)
    if match:
        return match.group()
    else:
        return "unknown"


def build_filepath(year, attribute):
    attr = attribute.split()[:-1]
    attr = "_".join(attr)

    return os.path.join(year, f"{attr}_{year}.csv")


if __name__ == "__main__":
    for file in files:
        df = pd.read_csv(file)

        attrs_dfs = []

        # Split the dataframe into multiple dataframes by attributes
        for i in range(1, len(df.columns), 2):
            subset_df = df.iloc[:, i : i + 2].copy()
            attrs_dfs.append(subset_df)

        # Combine the attribute dataframes with the name dataframe and save
        for attrs_df in attrs_dfs:
            result_df = pd.concat([df["name"], attrs_df], axis=1)

            year = extract_year_from_filename(file)
            file_path = build_filepath(year, attrs_df.columns[0])

            os.makedirs(year, exist_ok=True)
            result_df.to_csv(file_path, index=False)
