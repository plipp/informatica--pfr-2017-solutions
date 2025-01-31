
# coding: utf-8

# # Birds Migration

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


birds = pd.read_csv('../../data/bird_tracking.csv')


# In[3]:


birds.head()


# ## Exercise 1
# The migration data of which birds (`bird_name`s) are in the tracking dataset?

# In[4]:


birds.bird_name.unique()


# ## Exercise 2
# Draw a basic plot of the track(x-axis: latitude, y-axis:longitude) of each bird:
# 
# - The `title` of the plot should be `Bird Migration`.
# - The axes should be named.
# - A legend should show to which bird the single tracks belong.

# In[5]:


for bird in birds.bird_name.unique():
    plt.plot(birds[birds.bird_name==bird].longitude, birds[birds.bird_name==bird].latitude,'.', label=bird)
    
plt.title('Birds Migration')
plt.legend()
plt.xlabel('Latitude')
plt.ylabel('Longitude');


# ### Exercise 3
# 
# Draw the flight route on [Cartopy](http://scitools.org.uk/cartopy/)
# 
# ```bash
# conda install -c scitools cartopy
# # or (if former does not work)
# conda install -c conda-forge cartopy=0.15.1
# ```

# In[6]:


import cartopy.crs as ccrs


# ### Exercise 3.1
# 
# Draw the flight route with [PlateCarree-Projection](http://scitools.org.uk/cartopy/docs/latest/matplotlib/intro.html#adding-data-to-the-map)
# 
# See `TODO`s, where to change/insert your code.

# In[7]:


plt.figure(figsize=(10,10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# TODO 1: comment in/out and see, what happens
# ax.set_extent((-25,20,52,10))


# TODO 2: draw the single tracks with title and legend as in Exercise 2
for bird in birds.bird_name.unique():
    x,y = birds[birds.bird_name==bird].longitude, birds[birds.bird_name==bird].latitude
    plt.plot(x, y, linewidth=1, transform=ccrs.Geodetic(), label=bird)
    
plt.title('Birds Migration')    
plt.legend();


# ### Exercise 3.2
# 
# Draw the flight route with [Mercator-Projection](http://scitools.org.uk/cartopy/docs/latest/crs/projections.html#cartopy.crs.Mercator)
# 
# Use [Features](http://scitools.org.uk/cartopy/docs/latest/matplotlib/feature_interface.html) to show
# - LAND
# - OCEAN
# - COASTLINE
# - BORDERS
# - LAKES
# - RIVERS
# 
# See `TODO`s, where to change/insert your code.

# In[8]:


import cartopy.feature as cfeature

# TODO 1 set the right projection
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)

# TODO 2 set the features: LAND, OCEAN....
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)

ax.set_extent((-25,20,52,10))

# TODO 3: draw the single tracks with title and legend as in Exercise 2
for bird in birds.bird_name.unique():
    x,y = birds[birds.bird_name==bird].longitude, birds[birds.bird_name==bird].latitude
    plt.plot(x,y,'.', transform = ccrs.Geodetic(),label=bird)
    
plt.title('Birds Migration')
_ = plt.legend()

