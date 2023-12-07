import pandas as pd

"""
This script cleans data in CSV files by removing all '=' and '+' symbols.
Additionally, it identifies the common set of universities across all files, create a codex of universities, and retains only the first occurrence of each university, eliminating duplicates.

Instructions:

1. Add all file names to the 'files' list.
2. To rename the output files, modify the 'get_output_file_name' function.
"""

# TODO: Add all file names here
files = ["file_2021.csv", "file_2022.csv", "file_2023.csv", "file_2024.csv"]


def get_output_file_name(file_name):
    # TODO: Rename the output file by modifying the return string.
    # Example: return f"cleaned_{file_name}"

    # Or, to overwrite the input file, use:
    # return file_name
    return f"cleaned_{file_name}"


def data_clean(value):
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


if __name__ == "__main__":
    # Clean data and create new csv files
    for file in files:
        df = pd.read_csv(file)

        df = df.drop_duplicates(subset="name", keep="first")
        df = df.apply(lambda x: x.map(data_clean))

        df.to_csv(get_output_file_name(file), index=False)

    # Get intersection data of all files by university name
    output_files = [get_output_file_name(file) for file in files]

    common_universities = set(pd.read_csv(output_files[0])["name"])

    for file in output_files[1:]:
        current_universities = set(pd.read_csv(file)["name"])
        common_universities.intersection_update(current_universities)

    common_universities = list(common_universities)

    # Create a codex of universities
    university_data = {
        "id": range(1, len(common_universities) + 1),
        "university_name": common_universities,
    }
    university_df = pd.DataFrame(university_data)
    university_df.to_csv("university.csv", index=False)

    # Filter data by common universities
    for file in output_files:
        df = pd.read_csv(file)
        df = df[df["name"].isin(common_universities)]
        df = pd.merge(
            university_df, df, left_on="university_name", right_on="name", how="inner"
        )
        df = df.drop(columns=["name", "university_name"])

        df.to_csv(file, index=False)
