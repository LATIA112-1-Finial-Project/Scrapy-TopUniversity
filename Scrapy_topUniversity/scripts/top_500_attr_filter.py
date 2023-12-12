import pandas as pd

years = ["2021", "2022", "2023", "2024"]
attrs = ["employer reputation", "academic reputation"]

if __name__ == "__main__":
    for year in years:
        for attr in attrs:
            attr_file = attr.replace(" ", "_")
            file_path = f"{year}/{attr_file}_{year}.csv"
            df = pd.read_csv(file_path)

            df = df.sort_values(by=[f"{attr} rank"], ascending=True)
            df = df[df[f"{attr} rank"] <= 500]

            df.to_csv(f"{year}/top_500_{attr_file}_{year}.csv", index=False)
