
# coding: utf-8

# # [Optional] More Pandas Exercises
# 
# Original Source: Coursera [Introduction to Data Science in Python: Assignment 3](https://www.coursera.org/learn/python-data-analysis/home/week/3)
# 
# ## Additional Requirements
# ```bash
# pip install xlrd
# ```

# # Exercise 1
# Load the energy data from the file `Energy Indicators.xls`, which is a list of indicators of [energy supply and renewable electricity production](Energy%20Indicators.xls) from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013, and should be put into a DataFrame with the variable name of **energy**.
# 
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
# 
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']`
# 
# Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
# 
# Rename the following list of countries (for use in later questions):
# 
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# 
# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, 
# 
# e.g. 
# 
# `'Bolivia (Plurinational State of)'` should be `'Bolivia'`, 
# 
# `'Switzerland17'` should be `'Switzerland'`.
# 
# <br>
# 
# Next, load the GDP data from the file `world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**. 
# 
# Make sure to skip the header, and rename the following list of countries:
# 
# ```"Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```
# 
# <br>
# 
# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
# 
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15). 
# 
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# 
# *This function should return a DataFrame with 20 columns and 15 entries.*

# In[1]:


import pandas as pd
import numpy as np

def read_and_clean_energy():
    country_translation = {
        "Republic of Korea": "South Korea",
        "United States of America": "United States",
        "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
        "China, Hong Kong Special Administrative Region": "Hong Kong"
    }

    energy = (pd.read_excel('../../data/Energy Indicators.xls', header=None, skiprows=18, skip_footer=38)
              .drop([0,1], axis=1)
              .rename(columns={2:'Country', 3:'Energy Supply', 4:'Energy Supply per Capita', 5:'% Renewable'})
              .replace(r'...','',regex=False)
              .replace(r'^\s*$', np.nan, regex=True)
    )

    energy['Country'].replace(r'\(.*\)','', regex=True, inplace=True)
    energy['Country'].replace(r'\d','', regex=True, inplace=True)
    energy['Country'] = energy['Country'].apply(lambda country : country_translation[country] if country in country_translation else country)
    energy['Country'] = energy['Country'].str.strip()

    energy['Energy Supply'] = 1E6*energy['Energy Supply']
    return energy

def read_gdp():
    country_translation = {
        "Korea, Rep.": "South Korea", 
        "Iran, Islamic Rep.": "Iran",
        "Hong Kong SAR, China": "Hong Kong"
    }
    GDP = pd.read_csv('../../data/world_bank.csv', skiprows=4, header=0)
    GDP['Country Name'] = GDP['Country Name'].apply(lambda country : country_translation[country] if country in country_translation else country)
    return GDP    

# globals
energy = read_and_clean_energy()
GDP = read_gdp()
ScimEn = pd.read_excel('../../data/scimagojr-3.xlsx')

def top15_countries():
    GDP_reduced = GDP[['Country Name','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
           '2014', '2015']]
    eng_scimEng = pd.merge(ScimEn.head(15), energy, how='left', left_on='Country', right_on='Country')
    return pd.merge(eng_scimEng.set_index('Country'), GDP_reduced.set_index('Country Name'), how='left', left_index=True, right_index=True)

Top15 = top15_countries()
Top15


# # Exercise 2
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# 
# *This function should return a single number.*

# In[2]:


get_ipython().run_cell_magic('HTML', '', '<svg width="800" height="300">\n  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


# In[3]:


def missed_entries():
    scimEnEnergy = pd.merge(ScimEn,energy,how='outer',on='Country')
    outer_len = pd.merge(scimEnEnergy,GDP,how='outer',left_on='Country',right_on='Country Name').shape[0]
    scimEnEnergy = pd.merge(ScimEn,energy,how='inner',on='Country')
    inner_len = pd.merge(scimEnEnergy,GDP,how='inner',left_on='Country',right_on='Country Name').shape[0]
    return outer_len-inner_len
    
missed_entries()


# <br>
# 
# Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka Top15)

# # Exercise 3
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*

# In[4]:


def average_gdp(Top15):
    avgGDP = Top15[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013','2014', '2015']].mean(axis=1).sort_values(ascending=False)
    avgGDP.rename('avgGDP')
    return avgGDP

average_gdp(Top15)


# # Exercise 4
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[5]:


def delta_gdp(Top15):
    country6 = average_gdp(Top15).index[5]
    Top6 = Top15.loc[country6,]
    return Top6['2015'] - Top6['2006']

delta_gdp(Top15)


# # Exercise 5
# What is the mean `Energy Supply per Capita`?
# 
# *This function should return a single number.*

# In[6]:


def mean_energy_supply_per_capita(Top15):
    return Top15['Energy Supply per Capita'].mean(axis=0) #('Energy Supply per Capita', axis=1)

mean_energy_supply_per_capita(Top15)


# # Exercise 6
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[7]:


def country_pct_with_max_renewals(Top15):
    max_renewable = Top15['% Renewable'].idxmax()
    return (max_renewable, Top15.loc[max_renewable,'% Renewable'])

country_pct_with_max_renewals(Top15)


# # Exercise 7
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[8]:


def ratio_self_to_total_citation(Top15):
    Top15['ratio'] = Top15['Self-citations']/Top15['Citations']
    return (Top15['ratio'].idxmax(), Top15['ratio'].max())

ratio_self_to_total_citation(Top15)
    


# ### Exercise 8
# 
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return a single string value.*

# In[9]:


def third_most_populated(Top15):
    Top15PopEst = (Top15['Energy Supply'] / Top15['Energy Supply per Capita']).sort_values(ascending=False)
    return Top15PopEst.index[2]

third_most_populated(Top15)


# # Exercise 9
# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[10]:


def corr_citation_energy_supply(Top15):
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    return Top15.corr().loc['Energy Supply per Capita','Citable docs per Capita']

corr_citation_energy_supply(Top15)


# In[11]:


def plot9():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    
    Top15 = top15_countries()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# In[12]:


plot9()


# # Exercise 10
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[13]:


def calc_high_renew(Top15):
    median = np.median(Top15['% Renewable'])
    HighRenew = (Top15['% Renewable']>=median).astype(int).sort_index()
    return HighRenew.rename('HighRenew')

calc_high_renew(Top15)


# # Exercise 11
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[14]:


ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}

def stats_for_pop_est(Top15):
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    continent_df = Top15.groupby(ContinentDict).agg(['size', 'sum', 'mean', 'std'])['PopEst']
    continent_df.index.name='Continent'
    return continent_df

stats_for_pop_est(Top15)


# # Exercise 12
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a __Series__ with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*

# In[15]:


def count_by_renewable(Top15):
    renew_bins = pd.cut(Top15['% Renewable'], bins=5)
    continent_renew_df = Top15.groupby([ContinentDict,renew_bins]).agg(['count']).iloc[:,0]
    continent_renew_df
    return continent_renew_df

count_by_renewable(Top15)


# # Exercise 13
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# 
# e.g. 317615384.61538464 -> 317,615,384.61538464
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[16]:


def formatted_pop_est(Top15):
    popEst = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    return popEst.apply(lambda n: "{0:,}".format(n))

formatted_pop_est(Top15)


# # Exercise 14
# 
# Use the built in function `plot_14()` to see an example visualization.

# In[17]:


def plot_14(Top15):
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")


# In[18]:


plot_14(Top15)

