
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


# In[2]:


import numpy as np

np_male_selfemployment_rates = np.array(male_selfemployment_rates)
np_male_selfemployment_rates


# In[3]:


np_female_selfemployment_rates = np.array(female_selfemployment_rates)
np_female_selfemployment_rates


# # Solutions with numpy
# 
# ## Basic Calculations and Statistics

# ### Exercise 1
# 
# Calculate for each country the overallselfemployment_rate:<br>
# `selfemployment_rate:=(male_selfemployment_rates+female_selfemployment_rates)/2`
# 
# (assumes that #women ~#men)

# In[18]:


assert len(np_male_selfemployment_rates) == len(female_selfemployment_rates)

selfemployment_rate = (np_male_selfemployment_rates + np_female_selfemployment_rates)/2

assert len(selfemployment_rate)==len(np_male_selfemployment_rates)
selfemployment_rate[:5]


# ### Exercise 2
# Calculate
# - maximum
# - minimum
# - sum
# - mean
# - [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation)
# 
# for/of all selfemployment_rates.

# In[19]:


np.max(selfemployment_rate)


# In[20]:


np.min(selfemployment_rate)


# In[23]:


np.sum(selfemployment_rate)


# In[24]:


np.mean(selfemployment_rate)


# In[25]:


np.std(selfemployment_rate)


# ### Exercise 3
# Find the Country with the highest `selfemployment_rate`.

# In[27]:


countries[selfemployment_rate.argmax()]


# ### Exercise 4
# Find the the sum of all `selfemployment_rate`s, which are between `10-15`.

# In[30]:


selfemployment_rate[(selfemployment_rate>10) & (selfemployment_rate<15)].sum()


# ## Aggregetions

# In[ ]:


# not easier than with simple python => Won't do here (again)

