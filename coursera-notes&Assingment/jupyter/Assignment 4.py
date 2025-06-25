#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[8]:


df= pd.read_csv('C:\coursera\Assignment 4 Data.csv',skiprows=1)
df.columns=['Week','Python','Java Script','Java','C++']
df.head()


# In[9]:


i=[df['Week'][x] for x in range(0,261,261//5) ]
l=['2015-Aug','2016-Aug','2017-Aug','2018-Aug','2019-Aug','2020-Aug']


# In[11]:


i=[df['Week'][x] for x in range(0,261,261//5) ]
l=['2015-Aug','2016-Aug','2017-Aug','2018-Aug','2019-Aug','2020-Aug']


plt.plot(df['Week'],df['Python'],'b-',label='python',alpha=0.75)
plt.plot(df['Week'],df['Java'],'g-',label='Java',alpha=0.75)
plt.plot(df['Week'],df['Java Script'],'r-',label='Java Script',alpha=0.75)
plt.plot(df['Week'],df['C++'],'y-',label='C++',alpha=0.75)

plt.plot(df['Week'],[80]*261,'k--',alpha=0.2)
plt.plot(df['Week'],[60]*261,'k--',alpha=0.2)
plt.plot(df['Week'],[40]*261,'k--',alpha=0.2)
plt.plot(df['Week'],[30]*261,'k--',alpha=0.2)


plt.ylabel('Number of Google Queries')
plt.title('Trends of common Programming Languages over a period of five years')
plt.legend(loc=9,frameon=False)

plt.xticks(i)
plt.xticks(i,l);


# In[ ]:




