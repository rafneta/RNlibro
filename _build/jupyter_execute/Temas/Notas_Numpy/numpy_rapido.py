#!/usr/bin/env python
# coding: utf-8

# ![](https://raw.githubusercontent.com/rafneta/RNlibro/master/imagenes/banner.png)
# 
# ```{contents}
# :depth: 4
# ```
# 
# # NumPy

# - [Página principal de NumPy](https://numpy.org/)
# - [Documentación](https://numpy.org/doc/stable/)
# 
# 
# ![Image](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41586-020-2649-2/MediaObjects/41586_2020_2649_Fig2_HTML.png?as=webp)
# 
# 

# In[2]:


import numpy as np


# In[24]:


dir(np)


# In[25]:


help(np.linalg)


# In[13]:


help(np.shape)


# In[14]:


a = np.arange(15)
a


# In[15]:


np.shape(a)


# In[5]:


type(a)


# In[6]:


dir(a)


# In[11]:


help(np.ndarray.shape)


# In[8]:


a.shape


# In[17]:


help(np.ndarray.reshape)


# In[20]:


help(a.reshape)


# In[19]:


help(np.reshape)


# In[21]:


a.reshape((5,3))


# In[27]:


a.reshape((5,3),order='F')


# ## Arreglos
# 
# ![Image](https://www.pythoninformer.com/img/numpy/2d-array.png) ![Image](https://www.pythoninformer.com/img/numpy/3d-array-stack.png) 
# 
# 

# In[154]:


a = np.linspace(1,10,3)
a


# In[33]:


a.shape


# In[45]:


b = np.linspace(1,15,15)
print(b)
print(b.shape)
b = b.reshape((3,5))
print(b)
b.shape


# In[47]:


c = np.linspace(1,30,30)
print(c)
print(c.shape)
c = c.reshape((2,3,5))
print(c)
c.shape


# In[51]:


d = np.ones((2,3,5))
print(d.shape)
d


# ![Image](https://media.geeksforgeeks.org/wp-content/uploads/Numpy1.jpg)

# In[52]:


c


# In[53]:


c[1,1,2]


# In[57]:


e = np.linspace(1,8,8)
e.reshape((2,2,2))


# In[59]:


e = np.array([[[1., 2.],[3., 4.]],[[5., 6.],[7., 8.]]])
e


# In[61]:


e[0,:,:]*e[1,:,:]


# In[62]:


e[0,:,:]@e[1,:,:]


# In[63]:


e[0,:,:].dot(e[1,:,:])


# In[67]:


help(np.linalg.multi_dot)


# In[68]:


np.linalg.multi_dot([e[0,:,:],e[1,:,:]])


# In[79]:


print(a)
print(c[0,:,:])
r = a.dot(c[0,:,:])
print(r)
print(r.shape)
r.ndim


# In[80]:


ap = a.reshape((1,3))
print(ap)
ap.shape
rp = ap.dot(c[0,:,:])
print(rp)
print(rp.shape)
rp.ndim


# In[84]:


at = a.T
print(at)
at.shape


# In[85]:


apt = ap.T
print(apt)
apt.shape


# In[93]:


print(at)
r = np.ones((3,3)).dot(at)
print(r)
print(r.shape)
r.ndim


# In[94]:


print(apt)
r = np.ones((3,3)).dot(apt)
print(r)
print(r.shape)
r.ndim

