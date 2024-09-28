#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


data = pd.read_csv("Desktop\Classes\ExcelR\Assignments\Assignment - 5\EDA1\Cardiotocographic.csv", encoding = 'unicode_escape')


# In[3]:


data.info()


# In[4]:


data.count()


# In[5]:


data.head(10)


# In[6]:


data.tail(10)


# In[7]:


data1 = data.copy()


# In[8]:


data1


# In[9]:


# removing the duplicated values
data1.duplicated().sum()


# In[10]:


data_cleaned = data1.drop_duplicates()


# In[11]:


data1=data_cleaned


# In[12]:


data1


# In[13]:


data1.isnull().sum()


# In[14]:


data2 = data1.fillna(data1.mean())


# In[15]:


data2.info()


# In[16]:


data2.describe()


# In[17]:


data2.boxplot()


# In[18]:


### Detecting outlier in all columns
def find_outliers_iqr(data2):
    q1 = data2.quantile(0.25)
    q3 = data2.quantile(0.75)
    iqr = q3-q1
    upperlimit = q3 + (1.5*iqr)
    lowerlimit = q1 - (1.5*iqr)
    return((data2<lowerlimit)|(data2>upperlimit))
outliers = find_outliers_iqr(data2)
print(outliers.sum())


# In[19]:


##caping outlier in data set
def cap_outliers(data2):
    q1 = data2.quantile(0.25)
    q3 = data2.quantile(0.75)
    iqr = q3-q1
    lowercap= q1 - 1.5*iqr
    uppercap= q3 + 1.5*iqr
    
    data2_capped = data2.apply(lambda x:np.where(x<lowercap[x.name],lowercap[x.name],x))
    data2_capped = data2_capped.apply(lambda x:np.where(x>uppercap[x.name],uppercap[x.name],x))
    return data2_capped
data2_capped = cap_outliers(data2)
print(data2_capped.sum())


# In[20]:


sns.boxplot(data2_capped)


# In[21]:


data3 = data2_capped


# In[22]:


data3.info()


# In[23]:


data3.describe()


# In[24]:


data3.boxplot()


# In[25]:


data3.corr()


# In[26]:


corr_matrix = data3.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()


# In[27]:


data3.hist(bins=20, figsize=(15, 10))
plt.show()


# In[28]:


import sweetviz as sv


# In[29]:


sweet_report = sv.analyze(data3)
sweet_report.show_html('weather_report.html')


# In[ ]:




