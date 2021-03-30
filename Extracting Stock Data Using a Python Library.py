#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install yfinance')


# In[6]:


import yfinance as yf
import pandas as pd


# In[7]:


get_ipython().system('pip install yfinance')
import yfinance as yf
import pandas as pd
AMD = yf.Ticker("amd")

AMD_info=AMD.info
AMD_info


# In[8]:


AMD_info['country']


# In[9]:


AMD_info['sector']


# In[21]:


AMD_Volume = AMD.history(period="max")
AMD_Volume.head(1000000)
AMD_Volume.max()


# In[ ]:




