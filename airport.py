from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://www.oag.com/on-time-performance-star-ratings-2018?airport_name='
# url = 'https://data.variflight.com/analytics/OTPRankingbyAirport'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
tables = soup.select('table')
df_list = []
# for table in tables:
df_list.append(pd.concat(pd.read_html(tables[1].prettify())))
df = pd.concat(df_list)
df.to_excel('result.xlsx')

