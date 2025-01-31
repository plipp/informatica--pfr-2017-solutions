
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


# # Solutions with Basic Python
# 
# ## Basic Calculations and Statistics

# ### Exercise 1
# 
# Calculate for each country the overallselfemployment_rate:<br>
# `selfemployment_rate:=(male_selfemployment_rates+female_selfemployment_rates)/2`
# 
# (assumes that #women ~#men)

# In[2]:


# check preconditons
assert len(male_selfemployment_rates)==len(female_selfemployment_rates)
n = len(male_selfemployment_rates)


# In[3]:


# Alternative 1: With for loops
selfemployment_rate = []
for i in range(n):
    selfemployment_rate.append((male_selfemployment_rates[i]+female_selfemployment_rates[i])/2)
        

# check postcondition
assert n==len(selfemployment_rate)

selfemployment_rate[:5]


# In[4]:


# Alternative 2: With list comprehension
selfemployment_rate = [(msr+fsr)/2 for msr, fsr in zip(male_selfemployment_rates,female_selfemployment_rates)]

# check postcondition
assert n==len(selfemployment_rate)

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

# In[5]:


max(selfemployment_rate)


# In[6]:


min(selfemployment_rate)


# In[7]:


sum(selfemployment_rate)


# In[8]:


# Alternative 1: mean
sum(selfemployment_rate)/len(selfemployment_rate)


# In[9]:


# Alternative 2: mean
from statistics import mean
mean(selfemployment_rate)


# In[10]:


# Alternative 1: by hand
from math import sqrt
m = mean(selfemployment_rate)
sqrt(sum([(v - m)**2 for v in selfemployment_rate])/len(selfemployment_rate))


# In[11]:


# Alternative 2: using statistics module
from statistics import pstdev
pstdev(selfemployment_rate)


# ### Exercise 3
# Find the Country with the highest `selfemployment_rate`.

# In[12]:


countries[selfemployment_rate.index(max(selfemployment_rate))]


# ### Exercise 4
# Find the the sum of all `selfemployment_rate`s, which are between `10-15`.

# In[13]:


sum(list(filter(lambda r: r>10 and r<15, selfemployment_rate)))


# ## Aggregetions

# ### Exercise 5
# Calculate the mean of the selfemployment-rates per continent.

# In[14]:


continent_with_rate = [(countries_by_continent[country], rate) for country,rate in zip(countries,selfemployment_rate)]
print ('continent_with_rate = {}'.format(continent_with_rate))

# ------------------------------------------
from collections import defaultdict

rate_by_continent = defaultdict(list)
for c,r in continent_with_rate:
    rate_by_continent[c].append(r)
    
print('AM -> {}'.format(rate_by_continent['AM']))

# ------------------------------------------
mean_rates_by_continent = {c:mean(r) for c,r in rate_by_continent.items()}
mean_rates_by_continent

