
# coding: utf-8

# # Social Network Analysis
# ## Analysis of the [Marvel Comic Universe](http://syntagmatic.github.io/exposedata/marvel/)
# 
# A description of all characters of the Marvel Universe can be found [here](http://marvel.com/characters/browse).

# ### Preparation: Install `networkx`
# 
# ```bash
# conda install networkx
# pip install python-louvain
# ```
# 
# The `networkx` documentation can be found [here](http://networkx.readthedocs.io/)

# In[1]:


import networkx as nx
import csv


# In[2]:


G = nx.Graph(name="Hero Network")
with open('../../data/hero-network.csv', 'r') as data:
    reader = csv.reader(data)
    for row in reader:
        G.add_edge(*row)


# In[3]:


nx.info(G)


# In[4]:


G.order() # number of nodes


# In[5]:


G.size() # number of edges


# # Graph Visualization
# 
# ![The whole Universe](http://syntagmatic.github.io/exposedata/marvel/screenshots/dataset1.png)
# 
# => Nice, but Hairball-Effect
# 
# => Let's try out [Ego-Graphs](http://networkx.readthedocs.io/en/stable/reference/generated/networkx.generators.ego.ego_graph.html)

# ## Ego Graph of an arbitrary Hero

# In[6]:


hero = 'MACE'


# In[7]:


ego=nx.ego_graph(G,hero,radius=1)
nx.info(ego)


# In[8]:


import networkx as nx
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import warnings; warnings.simplefilter('ignore')


# In[9]:


pos = nx.spring_layout(ego)
nx.draw(ego,pos,node_color='b',node_size=50, with_labels=True)

# ego large and red
nx.draw_networkx_nodes(ego,pos,nodelist=[hero],node_size=300,node_color='r');


# # Most important Heros
# 
# ## What means 'important'?
# 
# - **Degree**:<br>
#     Number of connections: Measure of popularity.<br>
#     It is useful in determining nodes that can quickly spread information.
# 
# - **Betweenness**:<br>
#     Shows which nodes are likely pathways of information, and can 
#     be used to determine where the graph will break apart if the node is removed.
#     
# - **Closeness**:<br> 
#     This is a measure of reach, that is, how fast information will spread to all
#     other nodes from this particular node. Nodes with the most central closeness enjoy
#     short durations during broadcast communication.
# 
# - **Eigenvector**:<br>
#     Measure of related influence. Who is closest to the most
#     important people in the graph? This can be used to show the power behind the
#     scenes, or to show relative influence beyond popularity.
#     
# (Taken from [Packt - Practical Datascience Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/practical-data-science-cookbook))

# ## 1. Degree Concept
# 
# * **Degrees** == number of connections of a node
# * **Degree Centrality** == percent of nodes in the graph that a node is connected to
# 
# ![Degree Concept](../images/4-1-degreeCentralitySamples.png) *CD here is the Degree Centrality of the whole Graph.

# In[10]:


G.degree() # see also ego-graph above


# In[11]:


G.degree('MACE')


# In[12]:


nx.degree_centrality(G)


# ## 2. Betweenness Concept
# 
# - on how many (shortest) paths does a node lie and thus enables brookerage?
# ![Brookerage](../images/4-1-brokerage.png)
# - Calculation ![Betweenness Calculation](../images/4-1-betweenness-sample-1.png)

# In[13]:


get_ipython().magic('pinfo nx.betweenness_centrality')


# ## 3. Closeness Concept
# 
# - Intuition: One still wants to be in the middle of things, not too far from the center
# ![Closeness != Brookerage](../images/4-1-closeness-1.png)
# - Calculation: Sum of Reciprokal Shortest Paths ![Closeness Calculation](../images/4-1-closeness-sample-1.png)

# In[14]:


get_ipython().magic('pinfo nx.closeness_centrality')


# ## 3. Eigenvector Concept
# 
# - Page Rank => Pages, which are linked by popular pages, have a higher Page Rank
# - finds the most influential nodes

# In[15]:


nx.eigenvector_centrality(G)


# # 1. Exercise
# 
# - Determine the 20 most popular Heros by their degrees
# - Draw the overall Degree Distribution (`plt.hist`)

# In[16]:


degrees = sorted(G.degree().items(), key=lambda deg:deg[1], reverse=True)


# In[17]:


top20 = degrees[:20]
top20


# In[18]:


all_degrees = list(G.degree().values())
                   
plt.hist(all_degrees, bins=500)
plt.title('Degree distribution')
plt.ylabel('freq')
plt.xlabel('degree');


# In[19]:


# Cut of the hightest values

plt.hist(all_degrees, bins=500, range=(0,500))
plt.title('Degree distribution')
plt.ylabel('freq')
plt.xlabel('degree');


# # 2. Exercise
# 
# - Determine the 20 most influential Heros by their eigenvector-centrality
# - Determine also their degrees and compare with the degree distribution: Are the most influential also the most popular heros?

# In[35]:


eigenvectors = sorted( nx.eigenvector_centrality(G).items(), key=lambda ev:ev[1], reverse=True)


# In[36]:


eigenvectors[:20]


# # Communities

# ## Connected Components (Graph Theorie)

# In[20]:


cc = list(nx.connected_components(G))


# In[21]:


len(cc)


# In[22]:


[len(c) for c in cc]


# In[23]:


[list(c)[:10] for c in cc]


# In[24]:


cc[3]


# ## 'Real' Communities
# 
# - Cliques: Every member is connected with each other members
# - k-Cores: Every member is connected with at least k other members
# 
# - ... n-Cliques, n-Clubs, ... (more restrictive than k-Cores)

# In[25]:


import community


# In[26]:


partition = community.best_partition(G)
partition # hero -> partion-no.


# # 3. Exercise
# 
# - how many communities/partions have been found?
# - how many heros are in each community/partition?
# - how small is the smallest community and who are its members?
# - draw an histogram, which shows the sizes of the single communities.

# In[27]:


len(set(partition.values())) # number of partitions


# In[28]:


from collections import Counter

counter = Counter(partition.values())
counter.most_common() # sorts


# In[29]:


[k for k, v in partition.items() if v==30] # members of the smallest community


# In[30]:


plt.hist(list(partition.values()))
plt.title('Members per community')
plt.xlabel('No. of community')
plt.ylabel('Number of members');

