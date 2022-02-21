#!/usr/bin/env python
# coding: utf-8

# # Tarea Semana 1 (MIT OLL)
# 
# La ditancia de un punto a un plano esta dada por 
# 
# $$
# \frac{\theta^{T} \mathbf{p}+\theta_{0}}{\|\theta\|}
# $$

# In[1]:


import numpy as np


# ## 1.2)
# 
# - Entrada: punto y parametros del plano
# - Salida: distancia del punto a la recta

# In[13]:


def signed_dist(x, th, th0):
    num = np.transpose(th) @ x + th0
    den = np.linalg.norm(th)
    dis = num / den
    return dis


# In[14]:


# funciones auxiliares

def rv(value_list):
    return np.array([value_list])

def tp(A):
    return np.transpose(A)

def cv(value_list):
    return tp(rv(value_list))


# In[17]:


th = cv([1,1])
th0 = 0
x = cv([3,4])
print(signed_dist(x,th,th0))

x = cv([-3,-4])
print(signed_dist(x,th,th0))


# ## 1.3)
# 
# - Entradas: punto, parametros del hiperplano, en formato columna
# - Salidas: arrglo de $1\times 1$ (2D), con +1 lado positivo, -1 lado nedativo, 0 sobre el plano 

# In[18]:


def positive(x, th, th0):
    dist = signed_dist(x, th, th0)
    return np.sign(dist)


# In[40]:


th = cv([1,1])
th0 = 0
x = cv([3,4])
print(positive(x,th,th0))

x = cv([-3,-4])
print(positive(x,th,th0))

x = cv([-1,1])
print(positive(x,th,th0))


# In[42]:


th = cv([1,-1,2,-3])
th0 = 0
data = np.transpose(np.array([[1,-1,2,-3],[1,2,3,4],[-1,-1,-1,-1],[1,1,1,1]]))

positive(data,th,th0)


# ## 1.4) 
# 
# ```
# data = np.transpose(np.array([[1, 2], [1, 3], [2, 1], [1, -1], [2, -1]]))
# labels = rv([-1, -1, +1, +1, +1])
# ```
# 
# Dados los parametros del hiperplanp aplicar positive a `data`
# y verificar que tanto se parecen a las etiquetas dadas

# In[24]:


data = np.transpose(np.array([[1, 2], [1, 3], [2, 1], [1, -1], [2, -1]]))
labels = rv([-1, -1, +1, +1, +1])


# In[25]:


th = cv([1,1])
th0 = -2
clasi = positive(data,th,th0)
clasi


# In[26]:


clasi == labels


# ## 1.5)
# 
# Automatizar lo anterior. Regresa el número de clasificaciones correctas

# In[27]:


def score(data, labels, th, th0):
    compara = positive(data,th,th0) == labels
    return compara.sum()


# In[29]:


score(data, labels, th, th0)


# ## 1.6) 
# 
# Dados un conjunto de hiperpalno, elegir al mejor entre una cantidad dada. El mejor es aquel que genere mayor score
#     

# In[38]:


def best_separator(data, labels, ths, th0s):
    _, c = ths.shape
    lista = []
    for i in range(c):
        lista.append(score(data, labels, th, th0))
    maxi = max(lista)
    idx = lista.index(maxi)
    vec = ths[:,idx]
    return (cv(vec), th0s[:,idx:idx+1])


# In[39]:


ths = np.transpose(np.array([[-1, 2], [1, -2], [-2, -1]]))
th0s = np.array([[-1,1,-2]])
                   
best_separator(data, labels, ths, th0s)

