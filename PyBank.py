#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import os


# In[15]:


file = os.path.join("budget_data.csv")


# In[16]:


data = pd.read_csv(file)
print (data)


# In[17]:


count = len(data)
print(count)


# In[18]:


#The net total amount of "Profit/Losses" over the entire period

column_sum = data.iloc[0:86,1].sum()
print (column_sum)


# In[19]:


#The average of the changes in "Profit/Losses" over the entire period

dif = data.iloc[85,1]-data.iloc[0,1]
average = dif/(count-1)
print (average)


# In[20]:


# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

df = pd.DataFrame(data)
column = df['Profit/Losses']
print (column)


# In[21]:


diff = column.diff()


# In[22]:


min = diff.min()
max = diff.max()
print (min)
print (max)


# In[23]:


df['Diff']=diff
df=df.drop(columns=['Profit/Losses'])
print (df)


# In[24]:


Greatest_Increase = df[df['Diff'].isin([max])]
print (Greatest_Increase)

Greatest_Decrease= df[df['Diff'].isin([min])]
print (Greatest_Decrease)

