#!/usr/bin/env python
# coding: utf-8

# In[2]:


import urllib.request
from bs4 import BeautifulSoup


# In[10]:


with urllib.request.urlopen(https://www.nasdaq.com/market-activity/stocks/aapl/historical) as response:
    DATA = response.read()
SOUP = BeautifulSoup(DATA)


# In[11]:


def stockPrices():
    stockData = []
    stockInfo = SOUP.find('table', {'class': 'yfnc_datamodoutline1'})
    rows = stockInfo.findAll('tr')
    
    for row in rows:
        try:
            cells = row.find_all('td')
            date = cells[0].get_text()
            close = cells[4].get_text()
            stockData.append({'date': date, 'close': close})
        except:
            continue

    for line in stockData[1:]:
        print(line['date'] + '  '        + line['close'])

stockPrices()

