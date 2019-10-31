#!/usr/bin/env python
# coding: utf-8

# In[2]:


import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.nasdaq.com/symbol/spx/historical').read()
soup = bs.BeautifulSoup(source,'lxml')


# In[26]:


import pandas as pd


# In[12]:


table = soup.find('tbody')


# In[13]:


table_rows = table.find_all('tr')


# In[14]:


table_rows 


# In[25]:


for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)


# In[94]:


#df = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'last'])
df= []
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.strip() for i in td]
    #print(row[0:5])
    #print(type(row))
    df.append(row)


# In[96]:


df = pd.DataFrame(df, columns=['time', 'open', 'high', 'low', 'last', '0'])


# In[103]:


df = df.drop(['0'], axis=1)


# In[104]:


df.to_csv('S&P500.csv')


# In[105]:


df.head()

