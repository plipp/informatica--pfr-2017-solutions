
# coding: utf-8

# # Basic Plotting

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib inline')


# In[2]:


plt.plot([1, 2, 1, 2]); # ; to supress text-output


# In[3]:


plt.plot(np.array([1, 2, 1, 2]));


# In[4]:


x = np.linspace(-4, 10, 29)
print(x)


# In[5]:


a = 1
b = 1
c = -6
x = np.linspace(-4, 4, 100)
y = a * x ** 2 + b * x + c
plt.plot(x, y);


# In[6]:


plt.plot([2, 4, 6], [2, 4, 3], '-', linewidth=6, color='red');


# In[7]:


a5 = np.arange(5)
plt.plot(a5,a5**3,'ro');


# In[8]:


# find out more about supported parameters like 'color', 'linewidth'...
get_ipython().magic('pinfo plt.plot')


# ### Exercise 1
# 
# Plot $y=(x+2)(x-3)(x+1)$ for $x$ going from $-5$ to $5$ using a dashed green line. 
# 
# On the same figure, plot a blue circle for every point where $y$ equals zero. Set the size of the circles to 8.
# 
# Label the axes as 'x-axis' and 'y-axis'. 
# Add the title 'y=(x+2)(x-3)(x+1)'
# 
# Check out the official [matplotlib documentation](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot) and the output of `plt.plot?` for help.

# In[9]:


x = np.linspace(-5,5,100)
y = (x+2)*(x-3)*(x+1)

plt.plot(x,y, 'g--')
plt.plot([-2,3,-1],[0,0,0],'o', markersize=8)
plt.xlabel('x')
plt.ylabel('y')

plt.title('y = (x+2)*(x-3)*(x+1)');


# ### Exercise 2
# #### Load Weather (Temperature) Data from Basel and plot them
# 
# You are provided with 3 data files containing the mean montly temperature of Basel for 1900, 1950, 2000. 
# 
# Year 1900 is already loaded, load also that one for 1950 and 2000.
# 
# Plot the temperature for each year against the number of the month (starting with 1 for January) all in a single graph. Add a legend by using the function `plt.legend(['line1','line2'])` (of course with more descriptive names).
# 
# Use `plt.legend?` and the matplotlib documentation to get help if you are stuck.

# In[10]:


get_ipython().system('ls ../../data/homog_mo*')


# In[11]:


basel_temperatures_1900 = np.genfromtxt('../../data/homog_mo_BAS-1900.csv', delimiter=',', skip_header=1) # Month -> mean Temperature
basel_temperatures_1900[:3]


# In[12]:


basel_temperatures_1950 = np.genfromtxt('../../data/homog_mo_BAS-1950.csv', delimiter=',', skip_header=1) # Month -> mean Temperature
basel_temperatures_2000 = np.genfromtxt('../../data/homog_mo_BAS-2000.csv', delimiter=',', skip_header=1) # Month -> mean Temperature

plt.plot(basel_temperatures_1900[:,0], basel_temperatures_1900[:,1])
plt.plot(basel_temperatures_1950[:,0], basel_temperatures_1950[:,1])
plt.plot(basel_temperatures_2000[:,0], basel_temperatures_2000[:,1])

plt.xlabel('month')
plt.ylabel('°C')
plt.legend(['1900','1950','2000']);


# ### Exercise 4, Subplots
# 
# #### 4.1 Subplot-Command
# Load the average monthly temperature 1900, 1950, 2000 for Basel. Create one plot with 3 graphs above each other using the subplot command (use `plt.subplot?`). On the top graph, plot the temperature for 1900, next 1950, next 2000. 
# 
# Label the ticks on the horizontal axis as 'jan', 'feb', 'mar', etc., rather than 0,1,2,etc. Use `plt.xticks?` to find out how. Add legends, axes labels.

# In[13]:


plt.subplot(3,1,1)
plt.plot(basel_temperatures_1900[:,0], basel_temperatures_1900[:,1])
plt.xticks([])
plt.ylabel('°C 1900')

plt.subplot(3,1,2)
plt.plot(basel_temperatures_1950[:,0], basel_temperatures_1950[:,1])
plt.xticks([])
plt.ylabel('°C 1950')

plt.subplot(3,1,3)
plt.plot(basel_temperatures_2000[:,0], basel_temperatures_2000[:,1])

from calendar import month_abbr
plt.xticks(np.arange(12), month_abbr[1:13], rotation=17 )
plt.ylabel('°C 2000')
plt.xlabel('month');


# #### 4.2 Subplots-Command
# Load the average monthly temperature 1900, 1950, 2000 for Basel. Create one plot with 3 graphs above each other using the subplot command (use `plt.subplots?`). On the top graph, plot the temperature for 1900, next 1950, next 2000. 
# 
# Label the ticks on the horizontal axis as 'jan', 'feb', 'mar', etc., rather than 0,1,2,etc. Use `plt.xticks?` to find out how. In the bottom graph, plot the difference between the 2000 and 1900 temperature. Add legends, axes labels.

# In[14]:


f,(ax1,ax2,ax3) = plt.subplots(3,1,sharex=True)
ax1.plot(basel_temperatures_1900[:,0], basel_temperatures_1900[:,1])
ax1.set_ylabel('°C 1900')

ax2.plot(basel_temperatures_1950[:,0], basel_temperatures_1950[:,1])
ax2.set_ylabel('°C 1950')

ax3.plot(basel_temperatures_2000[:,0], basel_temperatures_2000[:,1])

from calendar import month_abbr
plt.xticks(np.arange(12), month_abbr[1:13], rotation=17 )
ax3.set_ylabel('°C 2000')

plt.xlabel('month');


# ### Exercise 5, Pie Chart
# 
# At the 2012 London Olympics, the top ten countries with gold medals were<br> 
# `['USA', 'CHN', 'GBR', 'RUS', 'KOR', 'GER', 'FRA', 'ITA', 'HUN', 'AUS', 'OTHER']`. 
# They received  <br>
# `[46, 38, 29, 24, 13, 11, 11, 8, 8, 7, 107]` gold medals. 
# 
# Make a pie chart (type `plt.pie?` or go to the pie charts in the matplotlib gallery) of the top 10 gold medal winners plus the others at the London Olympics.
# 
# Take a look in the [Matplotlib Gallery](http://matplotlib.org/gallery.html) for further samples.

# In[15]:


plt.pie(x=[46, 38, 29, 24, 13, 11, 11, 8, 8, 7, 107] , labels=['USA', 'CHN', 'GBR', 'RUS', 'KOR', 'GER', 'FRA', 'ITA', 'HUN', 'AUS', 'OTHER']);

