#Covid Scrapping Book Practice

pip install requests
pip install beautifulsoup4

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

#Need to make sure it works
website='https://www.nytimes.com/interactive/2021/us/iowa-covid-cases.html'
website_url=requests.get(website).text
soup = BeautifulSoup(website_url,'html.parser')

my_table = soup.find('tbody')

table_data = []
for row in my_table.findAll('tr'):
    row_data = []
    for cell in row.findAll('td'):
        row_data.append(cell.text)
    if(len(row_data) > 0):
        data_item = {"Country": row_data[0],
                     "TotalCases": row_data[1],
                     "Per 100,000": row_data[2],
                     "14 day change": row_data[3],
                     "Test Positivity": row_data[4],
                     "Hospitalized avg per 100,000": row_data[5],
                     "14 day change": row_data[6],
                     "Deaths Daily Avg": row_data[7],
                     "Per 100,000": row_data[8],
                     "Fully Vaccinated": row_data[9],
        }
        table_data.append(data_item)

df = pd.DataFrame(table_data)

df.head()

df.info()

df.to_excel('Covid19_data.xlsx', index=True)