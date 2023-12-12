#!/usr/bin/env python

import csv

years = ["2021", "2022", "2023", "2024"]

for year in years:
    # (1) 匯入CSV檔
    filename = f"Cleaned_files/{year}/overall_{year}.csv"

    # (2) 將CSV檔轉成LIST
    with open(filename, "r", newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)

        # 讀取標題行
        HEADER = next(csv_reader)

        # 檢查 "overall rank" 所在的欄位索引
        overall_rank_index = HEADER.index("overall rank")

        # 創建一個空的列表來存放資料
        data_list = [HEADER]  # 初始化時加入標題行

        # 迭代每一列資料
        for row in csv_reader:
            # 將 "overall rank" 的內容轉為數字
            row[overall_rank_index] = int(row[overall_rank_index])

            # 將該列加入列表
            data_list.append(row)

    # (3) 將LIST每項的第二個項次從小到大進行排列
    data_list_sorted = sorted(data_list[1:], key=lambda x: x[1])

    # (4) 刪除每項第二個項次超過500的內容
    filtered_data = [row for row in data_list_sorted if row[1] <= 500]

    # (5) 輸成CSV，記得補上HEADER再將剛剛的內容接續在後面
    output_filename = f"Top_500_University_Data/{year}/top_500_overall_{year}.csv"

    with open(output_filename, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)

        # 寫入 HEADER
        csv_writer.writerow(HEADER)

        # 寫入 filtered_data
        csv_writer.writerows(filtered_data)

    print(f"CSV 檔案 {output_filename} 已成功輸出。")


# In[ ]:
