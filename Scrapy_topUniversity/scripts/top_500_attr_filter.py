import pandas as pd

years = ["2021", "2022", "2023", "2024"]
attrs = ["employer reputation", "academic reputation", "overall"]

if __name__ == "__main__":
    all_universities = set()

    # 過濾出前 500 名的大學
    for year in years:
        for attr in attrs:
            attr_file = attr.replace(" ", "_")
            file_path = f"Cleaned_files/{year}/{attr_file}_{year}.csv"
            df = pd.read_csv(file_path)

            df = df.sort_values(by=[f"{attr} rank"], ascending=True)
            df = df[df[f"{attr} rank"] <= 500]

            all_universities.update(df["name"])

            df.to_csv(
                f"Top_500_University_Data/{year}/top_500_{attr_file}_{year}.csv",
                index=False,
            )

    # 建立 ID 表
    id_table = pd.DataFrame(list(all_universities), columns=["university_name"])
    id_table["id"] = range(1, len(id_table) + 1)

    id_table = id_table[["id", "university_name"]]
    id_table.to_csv("Top_500_University_Data/university.csv", index=False)

    # 將大學名稱替換成對應的 ID
    for year in years:
        for attr in attrs:
            attr_file = attr.replace(" ", "_")
            file_path = f"Top_500_University_Data/{year}/top_500_{attr_file}_{year}.csv"
            df = pd.read_csv(file_path)

            df = pd.merge(
                id_table,
                df,
                left_on="university_name",
                right_on="name",
                how="inner",
            )
            df = df.drop(columns=["name", "university_name"])
            df = df.rename(columns={"id": "university_id"})
            df = df.sort_values(by=[f"{attr} rank"], ascending=True)

            new_file_path = (
                f"Top_500_University_Data/{year}/top_500_{attr_file}_{year}.csv"
            )
            df.to_csv(new_file_path, index=False)
