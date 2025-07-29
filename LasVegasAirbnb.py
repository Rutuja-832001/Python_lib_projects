#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#Importing Dataset
data = pd.read_csv("C:/Users/0024au/Downloads/las_vegas_dataset.csv", encoding_errors='ignore')


# In[4]:


#Data Exploration
data.head()


# In[5]:


data.tail()


# In[6]:


data.shape


# In[7]:


data.info()


# In[8]:


data.describe()


# In[9]:


#Data Cleaning
data.isnull().sum()

# dropping all missing values rows
data.dropna(inplace=True)

# data.fillna()
data.isnull().sum()


# In[10]:


# Dealing with duplicates rows
data.duplicated().sum()

# Deleting duplicated rows
# data[data.duplicated()]

data.drop_duplicates(inplace=True)
data.duplicated().sum()


# In[11]:


#Type Casting and changing Data Types
data.dtypes

data['id'] = data['id'].astype(object)
data.dtypes

data['host_id'] = data['host_id'].astype(object)
data.dtypes


# In[12]:


# Identifying Outliers

df = data[data['price'] < 1500]

sns.boxplot(data=df, x='price')


# In[13]:


#Price distribuion

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='price', bins=100)
plt.title('Price Distribuition')
plt.ylabel("Frequency")
plt.show()


# In[15]:


#Availability distribuion
plt.figure(figsize=(6, 3))
sns.histplot(data=df, x='availability_365')
plt.title('availability_365 Distribuition')
plt.ylabel("Frequency")
plt.show()


# In[16]:


df.groupby(by='neighbourhood_group')['price'].mean()


# In[17]:


# ['price per bed']

df['price per bed']= df['price']/df['beds']
df.head()


# In[18]:


# average price per bed
df.groupby(by='neighbourhood_group')['price per bed'].mean()


# In[19]:


df.columns


# In[20]:


# price dependency on neighbourhood
sns.barplot(data=df, x='neighbourhood_group', y='price', hue='room_type')


# In[21]:


# number of reviews and price rel
plt.figure(figsize=(8, 5))
plt.title("Locality and Review Dependency")
sns.scatterplot(data=df, x='number_of_reviews', y='price', hue='neighbourhood_group')
plt.show()


# In[22]:


sns.pairplot(data=df, vars=['price', 'minimum_nights', 'number_of_reviews', 'availability_365'], hue='room_type')


# In[23]:


# heat map - correlation of one variable with others for numerical column

corr = df[['latitude', 'longitude', 'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365', 'beds']].corr()
corr

plt.figure(figsize=(8, 6))
sns.heatmap(data=corr, annot=True)


# In[24]:


#Geographical Distribution of AirBnb Listing
plt.figure(figsize=(10, 7))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='room_type')
plt.title("Geographical Distribution of AirBnb Listing")
plt.show()

