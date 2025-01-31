
# coding: utf-8

# # Self Employment Data 2015
# from [OECD](https://data.oecd.org/emp/self-employment-rate.htm#indicator-chart)

# In[1]:


countries = ['AUS', 'AUT', 'BEL', 'CAN', 'CZE', 'FIN', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'JPN', 
             'KOR', 'MEX', 'NLD', 'NZL', 'NOR', 'POL', 'PRT', 'SVK', 'ESP', 'SWE', 'CHE', 'TUR', 'GBR', 
             'USA', 'CHL', 'COL', 'EST', 'ISR', 'RUS', 'SVN', 'EU28', 'EA19', 'LVA']

male_selfemployment_rates = [12.13246, 15.39631, 18.74896, 9.18314, 20.97991, 18.87097, 
                             13.46109, 39.34802, 13.3356, 16.83681, 25.35344, 29.27118, 
                             12.06516, 27.53898, 31.6945, 19.81751, 17.68489, 9.13669, 
                             24.15699, 22.95656, 19.00245, 21.16428, 13.93171, 8.73181, 
                             30.73483, 19.11255, 7.48383, 25.92752, 52.27145, 12.05042, 
                             15.8517, 8.10048, 19.02411, 19.59021, 19.1384, 14.75558]

female_selfemployment_rates = [8.18631, 10.38607, 11.07756, 8.0069, 12.78461, 
                               9.42761, 7.75637, 29.56566, 8.00408, 7.6802, 8.2774, 18.33204, 
                               9.7313, 23.56431, 32.81488, 13.36444, 11.50045, 4.57464, 
                               17.63891, 13.92678, 10.32846, 12.82925, 6.22453, 9.28793, 
                               38.32216, 10.21743, 5.2896, 25.24502, 49.98448, 6.624, 
                               9.0243, 6.26909, 13.46641, 11.99529, 11.34129, 8.88987]

countries_by_continent = {'AUS':'AUS', 'AUT':'EUR', 'BEL':'EUR', 'CAN':'AM', 
                          'CZE':'EUR', 'FIN':'EUR', 'DEU':'EUR', 'GRC':'EUR', 
                          'HUN':'EUR', 'ISL':'EUR', 'IRL':'EUR', 'ITA':'EUR', 
                          'JPN':'AS',  'KOR':'AS',  'MEX':'AM',  'NLD':'EUR', 
                          'NZL':'AUS', 'NOR':'EUR', 'POL':'EUR', 'PRT':'EUR', 
                          'SVK':'EUR', 'ESP':'EUR', 'SWE':'EUR', 'CHE':'EUR', 
                          'TUR':'EUR', 'GBR':'EUR', 'USA':'AM' , 'CHL':'AM', 
                          'COL':'AM' , 'EST':'EUR', 'ISR':'AS',  'RUS':'EUR', 
                          'SVN':'EUR', 'EU28':'EUR','EA19':'AS', 'LVA':'EUR'}


# In[2]:


import pandas as pd

df_male_selfemployment_rates = pd.DataFrame({'countries':countries, 'selfemployment_rates':male_selfemployment_rates})
df_male_selfemployment_rates.head()


# In[3]:


df_female_selfemployment_rates = pd.DataFrame({'countries':countries, 'selfemployment_rates':female_selfemployment_rates})
df_female_selfemployment_rates.head()


# In[4]:


df_country_continent = pd.DataFrame(list(countries_by_continent.items()), columns=['country','continent'])
df_country_continent.head()


# # Solutions with Pandas
# 
# ## Basic Calculations and Statistics

# ### Exercise 1
# 
# Calculate for each country the overallselfemployment_rate:<br>
# `df_selfemployment_rate:=(male_selfemployment_rates+female_selfemployment_rates)/2`
# 
# (assumes that #women ~#men)

# In[5]:


df_s = pd.merge(df_male_selfemployment_rates, df_female_selfemployment_rates, on='countries')
df_s['selfemployment_rates'] = (df_s.selfemployment_rates_x+df_s.selfemployment_rates_y)/2
df_s.head()


# In[6]:


df_selfemployment_rate=df_s[['countries','selfemployment_rates']]
df_selfemployment_rate.head(5)


# ### Exercise 2
# Calculate
# - mean
# - standard deviation
# - maximum
# - minimum
# - sum
# 
# for/of all selfemployment_rates.

# In[7]:


print (df_selfemployment_rate.selfemployment_rates.min())
print (df_selfemployment_rate.selfemployment_rates.max())
print (df_selfemployment_rate.selfemployment_rates.sum())
print (df_selfemployment_rate.selfemployment_rates.mean())
print (df_selfemployment_rate.selfemployment_rates.std())


# In[8]:


df_selfemployment_rate.describe()


# ### Exercise 3
# Find the Country with the highest `selfemployment_rate`.

# In[9]:


df_selfemployment_rate.iloc[df_selfemployment_rate.selfemployment_rates.idxmax()]


# ### Exercise 4
# Find the the sum of all `selfemployment_rate`s, which are between `10-15`.

# In[10]:


df_selfemployment_rate[(df_selfemployment_rate.selfemployment_rates>10) & (df_selfemployment_rate.selfemployment_rates<15)].selfemployment_rates.sum()


# ### Exercise 5
# a) Plot a barchart of the `selfemployment_rate`s by country

# In[11]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

df_selfemployment_rate.plot.bar();


# In[12]:


# problem in plot above: x-axis are labeled with indices 0...35 => reindex
df_selfemployment_rate.head()


# In[13]:


df_s1 = df_selfemployment_rate.set_index('countries')
df_s1.head()


# In[14]:


df_s1.plot.bar(figsize=(12,8));


# b) Plot a barchart of the male vs. female `selfemployment_rate`s by country (as in [Basic-Plotting](1/5-Basic-Plotting-Exercise.ipynb), but using [pandas plotting facilities](https://pandas.pydata.org/pandas-docs/stable/visualization.html))

# In[15]:


dfs_2 = df_s[['countries','selfemployment_rates_x', 'selfemployment_rates_y']]     .rename(columns={'selfemployment_rates_x':'male', 'selfemployment_rates_y': 'female'})     .set_index('countries')
dfs_2.plot.bar(figsize=(12,8));


# ## Aggregetions

# In[16]:


df_cc = pd.merge(df_selfemployment_rate, df_country_continent, left_on='countries', right_on='country')
df_cc.head()


# In[17]:


df_sc = df_cc.drop('countries', axis=1).set_index('country')
df_sc.head()


# In[18]:


df_sc.groupby('continent').describe()


# In[19]:


df_sc.groupby('continent').mean()

