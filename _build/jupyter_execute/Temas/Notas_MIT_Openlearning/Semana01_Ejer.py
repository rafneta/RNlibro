#!/usr/bin/env python
# coding: utf-8

# # Ejercicios semana 1 (MIT OLL)
# 
# ## 2) Introducción a Numpy
# 
# - `np.array`
# 
# - np.transpose
# 
# - np.ndarray.shape
# 
# - np.dot
# 
# - np.sign
# 
# - np.sum
# 
# - Operaciones aritméticas +,-,*,/
# 
# 
# 

# In[1]:


import numpy as np


# ### 2.1) Arreglo

# In[2]:


A = np.array([[1,2.4,5],[-1.8,9,2]])
A


# In[3]:


A.shape


# ### 2.2) Transpuesta

# In[17]:


def tp(A):
    return np.transpose(A)

def tp1(A):
    return (np.transpose(A),A.T)

a, b = tp1(A)
a
b


# ### 2.4)

# In[16]:


def rv(value_list):
    return np.array([value_list])

a = rv([1,2,3])
a.shape


# ### 2.5)

# In[19]:


def cv(value_list):
    return tp(rv(value_list))

cv([1,2,3,4,5,6,7,8])


# ### 2.6)

# In[20]:


def length(col_v):
    v2 = col_v * col_v
    v2_s = np.sum(v2)
    norm = v2_s ** 0.5
    return norm

length(cv([3,4]))


# ### 2.7) 

# In[21]:


def normalize(col_v):
    norm = length(col_v)
    col_v_u = (1/norm) * col_v 
    return col_v_u

normalize(cv([3,4]))


# In[22]:


a = normalize(cv([3,4]))

length(a)


# In[ ]:




