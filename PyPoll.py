#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


file = os.path.join("election_data.csv")
election  = pd.read_csv(file)
print (election)


# In[3]:


# The total number of votes cast
voters=(len(election))
print(voters)


# In[4]:


# A complete list of candidates who received votes
candidates = election.drop_duplicates(['Candidate'])
column = candidates['Candidate']
for name in column:
    print(name)


# In[5]:


# The total number of votes each candidate won
# sorry still don't know how to use loop here

votersfork=election[election['Candidate'].isin(['Khan'])]
votersforc=election[election['Candidate'].isin(['Correy'])]
votersforl=election[election['Candidate'].isin(['Li'])]
votersforo=election[election['Candidate'].isin(["O'Tooley"])]

print(len(votersfork))
print(len(votersforc))
print(len(votersforl))
print(len(votersforo))


# In[13]:


# The percentage of votes each candidate won
percentagek= len(votersfork)/voters
percentagec=len(votersforc)/voters
percentagel=len(votersforl)/voters
percentageo=len(votersforo)/voters
list=[percentagek,percentagec,percentagel,percentageo]
print(list)


# In[11]:


# The winner of the election based on popular vote
winner = max(list)
print(winner)


# In[ ]:




