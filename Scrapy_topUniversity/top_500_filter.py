import pandas as pd

years = ["2021", "2022", "2023", "2024"]

if __name__ == "__main__":
    for year in years:
        file_path = f"{year}/employer_reputation_{year}.csv"
        df = pd.read_csv(file_path)

        df = df.sort_values(by=["employer reputation rank"], ascending=True)
        df = df[df["employer reputation rank"] <= 500]

        df.to_csv(f"{year}/top_500_employer_reputation_{year}.csv", index=False)
