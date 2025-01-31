
# coding: utf-8

# # Predicting Earnings from Census Data with Decision Tree
# taken from [The Analytics Edge](https://www.edx.org/course/analytics-edge-mitx-15-071x-3)

# # The Task
# 
# The United States government periodically collects demographic information by conducting a census.
# 
# In this problem, we are going to use census information about an individual to predict how much a person earns -- in particular, whether the person earns more than $50,000 per year. This data comes from the UCI Machine Learning Repository.
# 
# The file `census.csv` contains 1994 census data for 31,978 individuals in the United States.
# 
# The dataset includes the following 13 variables:
# 
# - age = the age of the individual in years
# - workclass = the classification of the individual's working status (does the person work for the federal government, work for the local government, work without pay, and so on)
# -  education = the level of education of the individual (e.g., 5th-6th grade, high school graduate, PhD, so on)
# - maritalstatus = the marital status of the individual
# - occupation = the type of work the individual does (e.g., administrative/clerical work, farming/fishing, sales and so on)
# - relationship = relationship of individual to his/her household
# - race = the individual's race
# - sex = the individual's sex
# - capitalgain = the capital gains of the individual in 1994 (from selling an asset such as a stock or bond for more than the original purchase price)
# - capitalloss = the capital losses of the individual in 1994 (from selling an asset such as a stock or bond for less than the original purchase price)
# - hoursperweek = the number of hours the individual works per week
# - nativecountry = the native country of the individual
# - over50k = whether or not the individual earned more than $50,000 in 1994
# 
# **Predict whether an individual's earnings are above $50,000 (the variable "over50k") using all of the other variables as independent variables.**

# In[53]:


import pandas as pd
import numpy as np


# # Exercise 1
# 
# 1. Read the dataset `census-2.csv`.
# 2. find out the name and the type of the single colums

# In[54]:


census = pd.read_csv('../../data/census-2.csv')
census.head()


# In[55]:


census.columns


# In[56]:


census.info()


# # Exercise 2
# sklearn classification can only work with numeric values. Therefore we first have to convert all not-numeric values to numeric values.
# 
# 1. copy the dataframe
# 2. in the copy: convert the target column `over50k` to a boolean
# 3. in the copy: convert the not-numeric independent variables (aka features, aka predictors) via `sklearn.LabelEncoder`.
# 
# See http://pbpython.com/categorical-encoding.html how to use the `sklearn.LabelEncoder` and for further alternatives to convert not-numeric values to numeric values.

# In[57]:


census2 = census.copy()


# In[58]:


print(census.over50k.unique())
census2.over50k = census2.over50k==' >50K'
print("{0:.2f}% over 50k".format(100*np.mean(census2.over50k)))


# In[59]:


not_numeric_columns = ['workclass', 'education', 'maritalstatus', 'occupation',
       'relationship', 'race', 'sex', 'nativecountry']


# In[60]:


from sklearn.preprocessing import LabelEncoder

for col in not_numeric_columns:
    le = LabelEncoder()
    census2[col] = le.fit_transform(census2[col])
    
census2.head()


# # Exercise 3
# Separate target variable `over50k` from the independent variables (all others): 
# `over50k -> y, all others -> X`

# In[61]:


X = census2.drop(['over50k'], axis=1)
y = census2['over50k']
census2.shape, X.shape, y.shape


# # Exercise 4
# Then, split the data randomly into a training set and a testing set, setting the `random_state` to 2000 before creating the split. Split the data so that the training set contains 60% of the observations, while the testing set contains 40% of the observations.

# In[62]:


from sklearn.model_selection import train_test_split


# In[63]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=2000)


# In[64]:


X_train.shape, X_test.shape, y_train.shape, y_test.shape


# # Exercise 5
# Let us now build a classification tree to predict "over50k". Use the training set to build the model, and all of the other variables as independent variables. Use `max_depth=3` and the default parameters else.

# In[65]:


from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train)


# # Exercise 6
# 
# Plot the decision tree using `plotting_utilities.plot_decision_tree`
# - Which are the most important feature? (Root of the Tree)
# - Which is the next important feature? (2nd Level)

# In[66]:


from plotting_utilities import plot_decision_tree, plot_feature_importances
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')


# In[67]:


plot_decision_tree(clf, X_train.columns,y_train.name)


# # Exercise 7
# 
# Plot Top 5 most important features with `plotting_utilities.plot_feature_importances`.
# 
# Are these features also the most important in the Decision Tree?

# In[74]:


idx = np.argsort(clf.feature_importances_)[:-6:-1]
print('Top 5 Feature importances: {}'.format(clf.feature_importances_[idx]))
plot_feature_importances(clf, X_train.columns, 5)


# In[75]:


print ("kinds of relationship: {}".format(census.relationship.unique()))
print ('kinds of education   : {}'.format(census.education.unique()))


# # Exercise 7
# - Predict for the test data and 
# - compare with the actual outcome: 
#   - Therefore plot the confusion matrix for the test-data and 
#   - calculate the accuracy
#       - for the trainings-data
#       - for the test-data

# In[78]:


y_pred = clf.predict(X_test)

from sklearn.metrics import confusion_matrix

print(" ------ Predicted ")
print(" Actual ")
confusion_matrix(y_test, y_pred)


# In[80]:


print('Accuracy of Decision Tree classifier on train set with "score"-function: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of Decision Tree classifier on test set with "score"-function: {:.2f}'
     .format(clf.score(X_test, y_test)))

