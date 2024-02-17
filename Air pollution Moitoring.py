
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import seaborn as sns
import datetime 
import matplotlib.dates as md


# In[71]:


df=pd.read_csv('pollution.csv')
df.head()


# In[72]:


df.drop("entry_id",axis=1,inplace=True)
df.head()


# In[73]:


#finding out the time when max. pollution occurs at Vijayawada
df[df['Vijayawada']==3.0235897439999997].drop([' Hyderabad','Vizag'],axis=1)


# In[74]:


#finding out the time when max. pollution occurs at  Hyderabad
df[df[' Hyderabad']==3.0235897439999997].drop(['Vijayawada','Vizag'],axis=1)


# In[75]:


#finding out the time when max. pollution occurs at Vizag
df[df['Vizag']==3.0235897439999997].drop(['Vijayawada',' Hyderabad'],axis=1)


# In[96]:


#finding out pollution level at Vijayawada by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Vijayawada']
plt.plot_date(x, y)
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Vijayawada")


# In[97]:


#finding out pollution level at  Hyderabad by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df[' Hyderabad']
plt.plot_date(x, y,color='green')
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at  Hyderabad")


# In[98]:


#finding out pollution level at Vizag by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Vizag']
plt.plot_date(x, y,color='red')
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Vizag")


# In[95]:


#pairplotting
sns.set(font_scale=1.5)
g=sns.pairplot(df,hue="Vijayawada")
g.fig.set_size_inches(15,15)


# In[108]:


sns.jointplot(x="Vijayawada",y=" Hyderabad",data=df,color='green')


# In[109]:


sns.jointplot(x="Vijayawada",y="Vizag",data=df,color='red')


# In[113]:


sns.jointplot(x="Vizag",y=" Hyderabad",data=df,color='k')
