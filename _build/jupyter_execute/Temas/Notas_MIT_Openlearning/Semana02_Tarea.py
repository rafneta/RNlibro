#!/usr/bin/env python
# coding: utf-8

# # Tarea Semana 2 (MIT OLL)

# In[2]:


import numpy as np


# In[3]:


# funciones auxiliares

def rv(value_list):
    return np.array([value_list])

def tp(A):
    return np.transpose(A)

def cv(value_list):
    return tp(rv(value_list))


# In[82]:


def actualiza(theta,x,y,origen = True):
    if origen:
        if y * (theta.T @ x) <= 0:
            return theta + y*x
        else:
            print("no es necesario actualizar")
            return theta

def verifica(theta,X,Y,origen= True):
    if origen:
        return np.sign(theta.T @ X) == Y.T


# In[83]:


X = np.array([[1,-1],[0,1],[-1.5,-1]]).T
Y = np.array([[1],[-1],[1]])


# In[84]:


# COmenzar con X_1

x = X[:,0:1]
theta = cv([0,0])
y = Y[0,0]
theta = actualiza(theta,x,y)
theta


# In[85]:


verifica(theta,X,Y)


# In[86]:


x = X[:,1:2]
y = Y[1,0]
theta = actualiza(theta,x,y)


# In[87]:


verifica(theta,X,Y)


# In[88]:


x = X[:,2:3]
y = Y[2,0]
theta = actualiza(theta,x,y)


# In[89]:


theta


# In[90]:


verifica(theta,X,Y)


# In[93]:


# COmenzar con x^2

x = X[:,1:2]
y = Y[1,0]
theta = cv([0,0])
theta = actualiza(theta,x,y)
theta


# In[94]:


verifica(theta,X,Y)


# ## 1.2a)

# In[95]:


# 1.2a)
X = np.array([[1,-1],[0,1],[-10,-1]]).T
Y = np.array([[1],[-1],[1]])


# In[96]:


# COmenzar con X_1

x = X[:,0:1]
theta = cv([0,0])
y = Y[0,0]
theta = actualiza(theta,x,y)
theta


# In[97]:


verifica(theta,X,Y)


# In[98]:


x = X[:,1:2]
y = Y[1,0]
theta = actualiza(theta,x,y)
theta


# In[99]:


x = X[:,2:3]
y = Y[2,0]
theta = actualiza(theta,x,y)
theta


# In[100]:


verifica(theta,X,Y)


# In[101]:


x = X[:,0:1]
y = Y[0,0]
theta = actualiza(theta,x,y)
theta


# In[102]:


verifica(theta,X,Y)


# In[103]:


x = X[:,1:2]
y = Y[1,0]
theta = actualiza(theta,x,y)
theta


# In[104]:


x = X[:,2:3]
y = Y[2,0]
theta = actualiza(theta,x,y)
theta


# In[105]:


x = X[:,0:1]
y = Y[0,0]
theta = actualiza(theta,x,y)
theta


# In[106]:


verifica(theta,X,Y)


# In[107]:


x = X[:,1:2]
y = Y[1,0]
theta = actualiza(theta,x,y)
theta


# In[108]:


x = X[:,2:3]
y = Y[2,0]
theta = actualiza(theta,x,y)
theta


# In[109]:


x = X[:,0:1]
y = Y[0,0]
theta = actualiza(theta,x,y)
theta


# In[110]:


verifica(theta,X,Y)


# In[111]:


x = X[:,1:2]
y = Y[1,0]
theta = actualiza(theta,x,y)
theta


# In[112]:


x = X[:,2:3]
y = Y[2,0]
theta = actualiza(theta,x,y)
theta


# In[113]:


x = X[:,0:1]
y = Y[0,0]
theta = actualiza(theta,x,y)
theta


# In[114]:


verifica(theta,X,Y)


# ## Problemas 7 a 10 
# 
# Los problemas 7 a 10 [son programas en colab](https://colab.research.google.com/drive/1kIWGi2TEZ0Agd_qQt1KiD2uZw_5AJFHT)
# 
# 

# In[ ]:




