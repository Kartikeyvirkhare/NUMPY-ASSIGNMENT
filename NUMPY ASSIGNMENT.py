#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


##Create an array of 10 zeros


# In[3]:


np.zeros(10)


# In[4]:


##Create an array of 10 ones


# In[5]:


np.ones(10)


# In[6]:


##Create an array of 10 fives


# In[7]:


np.ones(10)*5


# In[8]:


##Create an array of the integers from 10 to 50


# In[10]:


np.arange(10,51)


# In[11]:


##Create an array of all the even integers from 10 to 50


# In[13]:


np.arange(10,51,2)


# In[14]:


##Create a 3x3 matrix with values ranging from 0 to 8


# In[15]:


np.arange(9).reshape(3,3)


# In[16]:


##Create a 3x3 identity matrix


# In[17]:


np.identity(3)


# In[18]:


##Use NumPy to generate a random number between 0 and 1


# In[22]:


np.random.rand(2,2)


# In[23]:


##Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution


# In[24]:


np.random.randn(1,25)


# In[25]:


##Create the following matrix:


# In[27]:


np.arange(0.01, 1.01, 0.01).reshape(10, 10)


# In[28]:


#Create an array of 20 linearly spaced points between 0 and 1:


# In[30]:


np.linspace(0,1,20)


# # Numpy Indexing and Selection

# In[31]:


#Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:


# In[32]:


arr=np.arange(1,26).reshape(5,5)


# In[33]:


arr


# In[39]:


arr=np.eye(12,26).reshape(3,4)    ###did'nt understand how to solve this one


# In[37]:


arr


# In[41]:


arr=np.arange(1,26).reshape(5,5)


# In[42]:


arr


# In[47]:


arr[0:3,1:2]


# In[51]:


arr=np.arange(21,26)   #New Question


# In[49]:


arr


# In[55]:


arr=np.arange(16,26).reshape(2,5) #new Question


# In[56]:


arr


# In[57]:


##Get the sum of all the values in mat


# In[58]:


arr=np.arange(1,26).reshape(5,5)


# In[59]:


arr


# In[60]:


np.sum(arr)


# In[61]:


#Get the standard deviation of the values in mat


# In[62]:


np.std(arr)


# In[63]:


#Get the sum of all the columns in mat


# In[66]:


np.sum(arr,axis=1)


# In[67]:


##
arr[:,4:]


# In[68]:


np.sum(arr,axis=0)


# In[ ]:




