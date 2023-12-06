# LATIA112-1 HW02

## Virtual Environment

Recommend to use venv to isolate your environment.

```bash
$ python3.9 -m venv venv
$ source venv/bin/activate
```

## Dependancy

- Requirements.txt

  - ```bash
    $ pip install -r requirements.txt
    ```

- Chromedriver for MacOS
  - ```bash
    $ brew install --cask chromedriver
    ```

## How To Use My Scrapy Code

1. Install the dependancies
2. Modify the year that you want at line 13 in `universities.py`, default is "2024". (2021~2024)
3. Note that `file.csv` already exist in codebase, hence you **MAY CHANGE THE NAME TO THE OTHER** so as not to keep writing the data into `file.csv`.
   ```bash
   $ cd Scrapy_topUniversity
   $ scrapy crawl topUniversity -o file.csv
   ```
4. Use the command below to clean the dirty data in the file. This script removes all `=` and `+` symbols from the data and eliminating duplicates universities. Additionaly, it will create a codex of universities.

   ```bash
   $ python csv_cleaner.py
   ```

   The file `cleaned_file_<year>.csv` represents the resulting CSV file that has been cleaned and is ready for use in a database table.

5. Use the following command to split the cleaned CSV file into multiple CSV files based on attribute types and years.

   ```bash
   $ python attribute_splitter.py
   ```

   The resulting CSV files are stored in folders named after the corresponding years `ex. 2021/`, and each file is named after the attribute type and year `ex. overall_2021.csv`.

---

In my code, I am dealing with a Dynamic JS Website, where the data in the table is loaded dynamically. To retrieve the corresponding data, I have opted to use the website's API endpoint.

The method to obtain the endpoint involves opening the Network tab, selecting the Fetch/XHR filter tag, refreshing the webpage, and identifying the relevant keyword in the name file associated with the endpoint. By choosing the header, the request URL, which is the desired API endpoint, can be found. This approach allows for the successful retrieval of data in JSON content type.

### Yield Format

```py
"2024": {
    "name": university["title"].strip(),
    "overall rank": university["rank"],
    "overall score": university["overall_score"],
    "academic reputation rank": university["scores"][0]["rank"],
    "academic reputation score": university["scores"][0]["score"],
    "employer reputation rank": university["scores"][1]["rank"],
    "employer reputation score": university["scores"][1]["score"],
    "faculty student rank": university["scores"][2]["rank"],
    "faculty student score": university["scores"][2]["score"],
    "citations per faculty rank": university["scores"][3]["rank"],
    "citations per faculty score": university["scores"][3]["score"],
    "international faculty rank": university["scores"][4]["rank"],
    "international faculty score": university["scores"][4]["score"],
    "international students rank": university["scores"][5]["rank"],
    "international students score": university["scores"][5]["score"],
    "international Research Network rank": university["scores"][6]["rank"],
    "international Research Network score": university["scores"][6]["score"],
    "employment outcomes rank": university["scores"][7]["rank"],
    "employment outcomes score": university["scores"][7]["score"],
    "sustainability rank": university["scores"][8]["rank"],
    "sustainability score": university["scores"][8]["score"],
}

"2023": {
    "name": university["title"].strip(),
    "overall rank": university["rank"],
    "overall score": university["overall_score"],
    "academic reputation rank": university["scores"][0]["rank"],
    "academic reputation score": university["scores"][0]["score"],
    "employer reputation rank": university["scores"][1]["rank"],
    "employer reputation score": university["scores"][1]["score"],
    "faculty student rank": university["scores"][3]["rank"],
    "faculty student score": university["scores"][3]["score"],
    "citations per faculty rank": university["scores"][2]["rank"],
    "citations per faculty score": university["scores"][2]["score"],
    "international faculty rank": university["scores"][5]["rank"],
    "international faculty score": university["scores"][5]["score"],
    "international students rank": university["scores"][4]["rank"],
    "international students score": university["scores"][4]["score"],
    "international Research Network rank": university["scores"][6]["rank"],
    "international Research Network score": university["scores"][6]["score"],
    "employment outcomes rank": university["scores"][7]["rank"],
    "employment outcomes score": university["scores"][7]["score"],
    "sustainability rank": "n/a",
    "sustainability score": "n/a",
}

"2022": {
    "name": university["title"].strip(),
    "overall rank": university["rank"],
    "overall score": university["overall_score"],
    "academic reputation rank": university["scores"][4]["rank"],
    "academic reputation score": university["scores"][4]["score"],
    "employer reputation rank": university["scores"][5]["rank"],
    "employer reputation score": university["scores"][5]["score"],
    "faculty student rank": university["scores"][2]["rank"],
    "faculty student score": university["scores"][2]["score"],
    "citations per faculty rank": university["scores"][3]["rank"],
    "citations per faculty score": university["scores"][3]["score"],
    "international faculty rank": university["scores"][1]["rank"],
    "international faculty score": university["scores"][1]["score"],
    "international students rank": university["scores"][0]["rank"],
    "international students score": university["scores"][0]["score"],
    "international Research Network rank": "n/a",
    "international Research Network score": "n/a",
    "employment outcomes rank": "n/a",
    "employment outcomes score": "n/a",
    "sustainability rank": "n/a",
    "sustainability score": "n/a",
}

"2021": {
    "name": university["title"].strip(),
    "overall rank": university["rank"],
    "overall score": university["overall_score"],
    "academic reputation rank": university["scores"][4]["rank"],
    "academic reputation score": university["scores"][4]["score"],
    "employer reputation rank": university["scores"][5]["rank"],
    "employer reputation score": university["scores"][5]["score"],
    "faculty student rank": university["scores"][2]["rank"],
    "faculty student score": university["scores"][2]["score"],
    "citations per faculty rank": university["scores"][3]["rank"],
    "citations per faculty score": university["scores"][3]["score"],
    "international faculty rank": university["scores"][1]["rank"],
    "international faculty score": university["scores"][1]["score"],
    "international students rank": university["scores"][0]["rank"],
    "international students score": university["scores"][0]["score"],
    "international Research Network rank": "n/a",
    "international Research Network score": "n/a",
    "employment outcomes rank": "n/a",
    "employment outcomes score": "n/a",
    "sustainability rank": "n/a",
    "sustainability score": "n/a",
}
```

## Demo Video

- [HW02 - Scrapy_topUniversity](https://youtu.be/BhOQm14mPn4)

## Material

- [QS World University Rankings 2024: Top global universities](https://www.topuniversities.com/university-rankings/world-university-rankings/2024)
