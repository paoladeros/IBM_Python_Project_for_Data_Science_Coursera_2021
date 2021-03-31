#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[8]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[7]:


url = 'https://finance.yahoo.com/quote/AMZN/history?period1=1451606400&period2=1612137600&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'
html_data = requests.get(url).text


# In[6]:


soup = BeautifulSoup(html_data, 'html.parser')


# In[5]:


soup.title


# In[10]:


amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date =col[0].text
    Open =col[1].text
    high =col[2].text
    low =col[3].text
    close =col[4].text
    adj_close =col[5].text
    volume =col[6].text

    
    print("{}--->{}".format(date, Open, high, low, close, adj_close, volume))
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)


# In[11]:


amazon_data.head()


# In[ ]:




