#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv("C:\\coursera\\fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv")
df.head()


# In[4]:


import mplleaflet
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')
df = pd.read_csv("C:\\coursera\\fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv")
df = df.set_index('Date')
df.index = pd.to_datetime(df.index)
df['doy'] = df.index.dayofyear
df['year'] = df.index.year


# In[5]:


df = df[~((df.index.month == 2) & (df.index.day == 29))]


# In[6]:


mins = df[df['Element'] == 'TMIN']
maxs = df[df['Element'] == 'TMAX']

#mins = mins.groupby(['Date', 'Element'])['Data_Value'].min().unstack()
#maxs = maxs.groupby(['Date', 'Element'])['Data_Value'].max().unstack()
mins = mins.groupby(mins.index.dayofyear)['Data_Value'].min()
maxs = maxs.groupby(maxs.index.dayofyear)['Data_Value'].max()

by_day = pd.DataFrame({'min':mins, 'max':maxs})

min_15 = df.loc[(df['year'] == 2015) & (df['Element'] == 'TMIN'), 'Data_Value'] 
max_15 = df.loc[(df['year'] == 2015) & (df['Element'] == 'TMAX'), 'Data_Value']

min_0514 = df.loc[(df['year'] != 2015) & (df['Element'] == 'TMIN'), 'Data_Value'].min()
max_0514 = df.loc[(df['year'] != 2015) & (df['Element'] == 'TMAX'), 'Data_Value'].max()


# In[33]:


# Set indexes to days
below_rec_15 = min_15[min_15 < min_0514]
above_rec_15 = max_15[max_15 > max_0514]

below_rec_15.index = below_rec_15.index.dayofyear
above_rec_15.index = above_rec_15.index.dayofyear
by_day.index;



# In[32]:


get_ipython().magic('matplotlib notebook')
import datetime as dt



fig, ax = plt.subplots(figsize=(15,8), dpi=150)

plt.plot(mins.index, mins, c='#53868b', lw=1, zorder=1)
plt.plot(maxs.index, maxs, c='#ee7621', lw=1, zorder=1)

plt.scatter(below_rec_15.index, below_rec_15, c='r', marker='o', s=10, zorder=2)
plt.scatter(above_rec_15.index, above_rec_15, c='blue', marker='o', s=10, zorder=2)

plt.axhline(min_0514, lw=1.5, color='blue')
plt.axhline(max_0514, lw=1.5, color='red')
ax.set_title('Historical Temperature Range in Ann Arbor')

ax.legend(['Daily Min', 'Daily Max',
           'Historical Minimum', 'Historical Maximum',
           'Record Low Broken in 2015', 'Record High Broken in 2015'],
           fontsize=10, frameon=False, loc=8, ncol=3)

ax.set_ylabel('Temperature (tenths of $^\circ$C)')
ax.set_xlabel('Month of the Year')

m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticklabels(m)

fig.gca().xaxis.set_major_locator(plt.MaxNLocator(12))


plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.fill_between(by_day.index,
                 mins, maxs,
                 facecolor='orange',
                 alpha=.5)

# Fixes from discussion board.
fig.patch.set_facecolor('white')
fig.patch.set_alpha(1)


# In[33]:


get_ipython().magic('matplotlib inline')
import matplotlib.dates as dates
get_ipython().run_line_magic('matplotlib', 'inline')
fig = plt.figure(figsize=(12,6))


plt.plot(by_day.index, by_day['min'],
         c='#53868b', lw=1, zorder=2)

plt.plot(by_day.index, by_day['max'],
         c='#ee7621', lw=1, zorder=2)

# days below 2005-2014 record min
plt.scatter(below_min_15.index, below_min_15['TMIN'],
            c='#ee7621', marker='v', s=15, zorder=3)

# days above 2005-2014 record max
plt.scatter(above_max_15.index, above_max_15['TMAX'],
            c='#53868b', marker='^', s=15, zorder=3)

plt.title('Historical Temperatures in Ann Arbor, MI')
plt.legend(['Daily Min', 'Daily Max', 'Record Low Broken in 2015', 'Record High Broken in 2015'],
           frameon=False, loc=0)

# Bar at 0 celcius for reference
plt.plot(by_day.index, [0 for i in range(len(by_day))],
         c='black', lw=0.5, zorder=1, alpha=0.5)
plt.plot(by_day.index, [record_min for i in range(len(by_day))],
         c='black', lw=0.5, zorder=1, alpha=0.5)
plt.plot(by_day.index, [record_max for i in range(len(by_day))],
         c='black', lw=0.5, zorder=1, alpha=0.5)

plt.ylim([-50, 50])
plt.xlabel('Day of the Year')
plt.ylabel('Temperature - C$^\circ$')



plt.fill_between(by_day.index,
                 by_day['TMIN'], by_day['TMAX'],
                 facecolor='y',
                 alpha=0.5)

# Fixes from discussion board.
fig.patch.set_facecolor('white')
fig.patch.set_alpha(1)


# In[ ]:




