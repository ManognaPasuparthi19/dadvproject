import requests
import pandas as pd
from bs4 import BeautifulSoup

#scrapping data from website
page=requests.get('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
soup=BeautifulSoup(page.text,'html.parser')
x=soup.find_all('table')
countries=(x[1].find_all('span'))
rows=(x[1].find_all('tr'))
data=[]


#extracting data from table
for row in rows:
    cols = row.find_all('td')
    cols = [x.text.strip() for x in cols]
    data.append(cols)
print(data)

#writing data into csv file
df = pd.DataFrame(data=data)
df.drop(df.index[0:2], inplace=True,axis=0)
print(df)
df.to_csv('medals.csv')