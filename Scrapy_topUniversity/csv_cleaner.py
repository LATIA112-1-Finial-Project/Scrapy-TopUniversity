import pandas as pd

"""
Remove all '=' and '+' from the csv file elements. 

- To add more files to clean, add the file name to the file_names list.
- To rename the output file, change the string in the df.to_csv() function.
"""

# TODO: Add all file names here
file_names = ["file_2021.csv", "file_2022.csv", "file_2023.csv", "file_2024.csv"]


def csv_clean(value):
    if pd.isnull(value):
        return "n/a"

    try:
        numeric_value = pd.to_numeric(value)
        return numeric_value
    except ValueError:
        pass

    cleaned_value = value.replace("=", "").replace("+", "")

    try:
        cleaned_value = pd.to_numeric(cleaned_value)
    except ValueError:
        # print(f"Could not convert {value} to numeric")
        pass

    return cleaned_value


for file_name in file_names:
    df = pd.read_csv(file_name)
    df = df.apply(lambda x: x.map(csv_clean))

    # TODO: Rename the output file by modifying the string inside df.to_csv()
    # Example: df.to_csv(f"cleaned_{file_name}", index=False)

    # Or, to overwrite the input file, uncomment the line below, and comment the original line.
    # df.to_csv(file_name, index=False)
    df.to_csv(f"cleaned_{file_name}", index=False)
