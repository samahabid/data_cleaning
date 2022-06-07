#!/usr/bin/env python
# coding: utf-8

# **This notebook is an exercise in the [Data Cleaning](https://www.kaggle.com/learn/data-cleaning) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/scaling-and-normalization).**
# 
# ---
# 

# In this exercise, you'll apply what you learned in the **Scaling and normalization** tutorial.
# 
# # Setup
# 
# The questions below will give you feedback on your work. Run the following cell to set up the feedback system.

# In[2]:


from learntools.core import binder
binder.bind(globals())
from learntools.data_cleaning.ex2 import *
print("Setup Complete")


# # Get our environment set up
# 
# To practice scaling and normalization, we're going to use a [dataset of Kickstarter campaigns](https://www.kaggle.com/kemical/kickstarter-projects). (Kickstarter is a website where people can ask people to invest in various projects and concept products.)
# 
# The next code cell loads in the libraries and dataset we'll be using. 

# In[3]:


# modules we'll use
import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# read in all our data
kickstarters_2017 = pd.read_csv("../input/kickstarter-projects/ks-projects-201801.csv")

# set seed for reproducibility
np.random.seed(0)


# In[4]:


kickstarters_2017 


# Let's start by scaling the goals of each campaign, which is how much money they were asking for.  After scaling, all values lie between 0 and 1.

# In[5]:


# select the usd_goal_real column
original_data = pd.DataFrame(kickstarters_2017.usd_goal_real)

# scale the goals from 0 to 1
scaled_data = minmax_scaling(original_data, columns=['usd_goal_real'])

print('Original data\nPreview:\n', original_data.head())
print('Minimum value:', float(original_data.min()),
      '\nMaximum value:', float(original_data.max()))
print('_'*30)

print('\nScaled data\nPreview:\n', scaled_data.head())
print('Minimum value:', float(scaled_data.min()),
      '\nMaximum value:', float(scaled_data.max()))


# # 1) Practice scaling
# 
# We just scaled the "usd_goal_real" column. What about the "goal" column?
# 
# Begin by running the code cell below to create a DataFrame `original_goal_data` containing the "goal" column.

# In[10]:


# select the usd_goal_real column
original_goal_data = pd.DataFrame(kickstarters_2017.goal)


# Use `original_goal_data` to create a new DataFrame `scaled_goal_data` with values scaled between 0 and 1. You must use the `minmax_scaling()` function.

# In[15]:


# TODO: Your code here
scaled_goal_data = minmax_scaling(original_goal_data, columns=['goal'])



# Check your answer
q1.check()


# In[12]:


# Lines below will give you a hint or solution code
#q1.hint()
#q1.solution()


# # 2) Practice normalization
# 
# Now you'll practice normalization. We begin by normalizing the amount of money pledged to each campaign.

# In[17]:


# get the index of all positive pledges (Box-Cox only takes positive values)
index_of_positive_pledges = kickstarters_2017.usd_pledged_real > 0

# get only positive pledges (using their indexes)
positive_pledges = kickstarters_2017.usd_pledged_real.loc[index_of_positive_pledges]

# normalize the pledges (w/ Box-Cox)
normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0], 
                               name='usd_pledged_real', index=positive_pledges.index)

print('Original data\nPreview:\n', positive_pledges.head())
print('Minimum value:', float(positive_pledges.min()),
      '\nMaximum value:', float(positive_pledges.max()))
print('_'*30)

print('\nNormalized data\nPreview:\n', normalized_pledges.head())
print('Minimum value:', float(normalized_pledges.min()),
      '\nMaximum value:', float(normalized_pledges.max()))


# The values have changed significantly with normalization!
# 
# In the next code cell, you'll take a look at the distribution of the normalized data, where it should now resemble a normal distribution.

# In[18]:


# plot normalized data
ax = sns.histplot(normalized_pledges, kde=True)
ax.set_title("Normalized data")
plt.show()


# We used the "usd_pledged_real" column. Follow the same process to normalize the "pledged" column. 

# In[21]:


index_positive_pledges = kickstarters_2017.pledged >0
positive_pledges_only = kickstarters_2017.pledged.loc[index_positive_pledges]
normalized_values = pd.Series(stats.boxcox(positive_pledges_only)[0], name='pledged', index=positive_pledges_only.index)
ax = sns.histplot(normalized_values, kde=True)
ax.set_title("Normalized data")


# How does the normalized "usd_pledged_real" column look different from when we normalized the "pledged" column?  Or, do they look mostly the same?
# 
# Once you have an answer, run the code cell below.

# In[22]:


# Check your answer (Run this code cell to receive credit!)
q2.check()


# In[19]:


# Line below will give you a hint
q2.hint()


# # (Optional) More practice
# 
# Try finding a new dataset and pretend you're preparing to perform a [regression analysis](https://www.kaggle.com/rtatman/the-5-day-regression-challenge). 
# 
# [These datasets are a good start!](https://www.kaggle.com/rtatman/datasets-for-regression-analysis)
# 
# Pick three or four variables and decide if you need to normalize or scale any of them and, if you think you should, practice applying the correct technique.
# 
# # Keep going
# 
# In the next lesson, learn how to [**parse dates**](https://www.kaggle.com/alexisbcook/parsing-dates) in a dataset.

# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/data-cleaning/discussion) to chat with other learners.*
