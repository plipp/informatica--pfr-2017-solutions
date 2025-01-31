
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt


# ## Self Employment Data 2015
# from [OECD](https://data.oecd.org/emp/self-employment-rate.htm#indicator-chart)

# In[2]:


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


# In[3]:


get_ipython().magic('pinfo plt.bar')


# ## Exercise 1
# 
# Create a histogram, which shows the selfemployment-rates for men-women by country.
# Outcome should look similar to:
# 
# ![Histogram Sample](../images/1-2-selfemployment-histo-exercise.png)

# In[24]:


import numpy as np

bar_width = 0.35

n = len(male_selfemployment_rates)

x = np.arange(n)

plt.figure(figsize=(12,8))
plt.bar(x, male_selfemployment_rates, bar_width, label='Men');
plt.bar(x+bar_width, female_selfemployment_rates, bar_width, label='Women');

plt.legend()
plt.xlabel('country')
plt.ylabel('selfemployment-rate')
plt.title('selfemployment-rate by country and gender')
plt.xticks(x,countries, rotation=45);

