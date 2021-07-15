#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1#Create a null vector of size 10 but the fifth value which is 1.


# In[1]:


import numpy as np
x=np.zeros(10)
x[4]=1


# In[2]:


print(x)


# In[ ]:


#Create a vector with values ranging from 10 to 49.


# In[4]:


z=np.arange(10,50)
print(z)


# In[ ]:


#Create a 3x3 matrix with values ranging from 0 to 8


# In[9]:


y=np.arange(0,9).reshape(3,3)
print(y)


# In[ ]:


#Find indices of non-zero elements from [1,2,0,0,4,0]


# In[17]:


import numpy as np
p=np.array([1,2,0,0,4,0])
result=np.where(p!=0)[0]
print(result)


# In[ ]:


#Create a 10x10 array with random values and find the minimum and maximum values


# In[21]:


import numpy as np
b=np.random.random((10,10))
bmax,bmin=b.max(),b.min()
print(b)
print('maximum and minimum values are')
print(bmax,bmin)


# In[ ]:


#Create a random vector of size 30 and find the mean value.


# In[22]:


w=np.random.random(30)


# In[23]:


print(w)


# In[25]:


np.mean(w)


# In[ ]:




