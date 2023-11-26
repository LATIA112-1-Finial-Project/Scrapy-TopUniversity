import pandas as pd

files = ["file_2021.csv", "file_2022.csv", "file_2023.csv", "file_2024.csv"]

common_universites = set(pd.read_csv(files[0])["name"])

for file in files[1:]:
    current_universites = set(pd.read_csv(file)["name"])
    common_universites.intersection_update(current_universites)

print("Common universities: ", len(common_universites))
