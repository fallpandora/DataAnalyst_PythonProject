#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Imports pandas and numpy and below we are loading our dataset CSV file 
iatrogenic_df = pd.read_csv(r"C:\Users\Reagan\Desktop\ca-oshpd-adveventhospitalizationspsi.csv", index_col=None, na_values=['NA'])


# In[44]:


iatrogenic_df.columns
#We are listing out columns


# In[45]:


iatrogenic_df.rename(columns={'Count': 'IncidentCount'}, inplace=True)
#Rename columns to give better insight and understanding


# In[46]:


iatrogenic_df.columns
#Showing output of renamed columns


# In[47]:


iatrogenic_df.loc[:]
#Indexing the top and bottom rows in the dataset


# In[48]:


iatrogenic_df.sort_values(['County','IncidentCount'],ascending=True).groupby('County').head(20)
# Sorting and grouping by alpha, counties with the with the lowest incident counts


# In[49]:


iatrogenic_df.describe(include='all')
#Displaying the description of each column and giving mean, min etc.


# In[50]:


iatrogenic_df = iatrogenic_df.replace(np.nan, 0)
dfg = iatrogenic_df.groupby(['County'])['ObsRate'].mean()

dfg.plot(kind='bar', title='Average Observation by County', ylabel='Mean Observation Rate',
         xlabel='County', figsize=(16, 15))
#Bar graph displaying the average observation rate for each county in California


# In[51]:


mask = iatrogenic_df['County'].isin(['Lake'])
#display the mask that will only show a table with the counties that include the name Lake
mask.head()


# In[52]:


iatrogenic_df[mask].head(60)
#Mask showing only Lake County rows


# In[53]:


mask1 = iatrogenic_df['County'].isin(['Lake'])
mask2 = iatrogenic_df['PSIDescription'].str.contains('Accidental', case=False, na=False)
iatrogenic_df[mask1 & mask2].head(11)
#Table that is displaying both Lake County and the PSIDescription that shows Accidental Puncture or Laceration


# In[54]:


lakecounty = iatrogenic_df.loc[(iatrogenic_df['County'] == 'Lake') & (iatrogenic_df['PSIDescription'] == 'Accidental Puncture or Laceration')]
#Using the loc function to access the data values for particular rows and columns


# In[55]:


lakecounty.shape
#Verifying the shape of our data. How many rows and columns pulled in


# In[56]:


fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot()
ax.plot(lakecounty.Year, lakecounty.ObsRate,)
ax.set_xlabel('Year')
ax.set_ylabel('Observation Rates per 100k')
ax.set_title('Lake county - Iatrogenic laceration rates')
#Line graph created using plt. Setting size, graph type, where to locate data, and labeling


# In[57]:


statewide = iatrogenic_df.loc[(iatrogenic_df['County'] == 'STATEWIDE') & (iatrogenic_df['PSIDescription'] == 'Accidental Puncture or Laceration')]
# Using the loc function to pull additional data


# In[58]:


fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot()
ax.plot(lakecounty.Year, lakecounty.ObsRate,)
ax.plot(statewide.Year, statewide.ObsRate)
ax.set_xlabel('Year', fontsize=20)
ax.set_ylabel('Observation Rates per 100k', fontsize=20)
ax.set_title('Lake County - Iatrogenic laceration rates VS Statewide', fontsize=20)
ax.legend(['Lake County', 'Statewide'],loc="lower left")
#Comparing two sets of data "Lake County" & "STATEWIDE"


# In[ ]:




