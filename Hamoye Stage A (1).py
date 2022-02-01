#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install seaborn ')
import numpy as np
import pandas as pd



# In[19]:


#Read file
df = pd.read_csv (r'C:\Users\LENOVO\FoodBalanceSheets_E_Africa_NOFLAG.csv')
df


# In[6]:


# Total sum of Animal fats produced in 2014 and 2017


# In[20]:


Animalfats_2014= df.groupby('Item')['Y2014', 'Y2017']. sum()
Animalfats_2014


# In[98]:


# What is the mean and standard deviation across the whole dataset for the year 2015
print(df.mean())
print(df.std())


# In[38]:


# What is the total number and percentage of missing data in 2016 to 2 decimal places
missing_data= df.isnull().sum()
print(missing_data)
per_missing_data = df.isnull().sum() * 100/len(df)
print(per_missing_data)
# Answer = 1535 and 2.52%


# In[35]:


#which year has the highest correlation with element code


# In[58]:


#What year has the highetst sum of import quantity
df.groupby('Element')['Y2014' , 'Y2015' , 'Y2016' , 'Y2017']. max()   
# Answer = 2016


# In[60]:


NSWER = 1931287.75


# In[93]:


#Which of these element had the highest sum in 2018
highest_sum = df.groupby('Element')['Y2018']. sum()
highest_sum.n


# In[97]:


#Which of these elements had the 3rd lowest sum in 2018
LOWEST_sum = df.groupby('Element')['Y2018']. sum()
LOWEST_sum
 # Answer = protein supply quantity (g/capita/day)


# In[83]:


#What is the total import quantity in Algeria in 2018
import_quantity2018 = df.groupby(['Area', 'Element'])['Y2018']. sum()
import_quantity = import_quantity2018.head(10)
import_quantity

# Answer = 36238.29


# In[84]:


#Whal number of unique countries are in the dataset
df.nunique()
# Answer = 49


# In[ ]:





# In[ ]:




