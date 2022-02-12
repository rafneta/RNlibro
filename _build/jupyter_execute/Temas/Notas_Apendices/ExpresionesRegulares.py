#!/usr/bin/env python
# coding: utf-8

# ![](https://raw.githubusercontent.com/rafneta/RNlibro/master/imagenes/banner.png)
# 
# 

# # Expresiones regulares

# In[1]:


import re


# In[2]:


cadena = "cadena que tiene\n dos partes"
cadena


# In[3]:


print(cadena)


# In[4]:


cadena.splitlines()


# In[5]:


sepcad = cadena.splitlines()
sepcad


# In[6]:


"-------".join(sepcad)


# In[7]:


cadena.find("oso")


# In[8]:


help(str.find)


# In[9]:


cadena.find("a",6)


# In[10]:


cadena.find("tien")


# In[11]:


cadena.count("a")


# In[12]:


cadena.replace("a","-----")


# In[13]:


cadena


# 
# Una expresión regular es una cadena que contiene
# 
# - Caraceteres "s" "st"
# - Metacaracteres \d \s \w describen secuencias 
# - Cuantificadores + * 
# 

# In[14]:


re.findall(r"c",cadena)


# In[15]:


re.split(r"a",cadena)


# In[16]:


re.sub(r"a","---",cadena)


# **Metacaracter \d Digito**
# 

# In[17]:


re.findall(r"c\d",cadena)


# **Metacaracter \D No digito**
# 

# In[18]:


re.findall(r"c\D",cadena)


# **Metacaracter \w palabra**
# 

# In[19]:


re.findall(r"\w",cadena)


# **Metacaracetr \W no-palabra**
# 

# In[20]:


re.findall(r"\W",cadena)


# In[21]:


cadena


# In[22]:


re.findall(r"a\w",cadena)


# In[23]:


re.findall(r"a\W",cadena)


# **Metacaracter \s espacio**
# 

# In[24]:


re.findall(r"a\s",cadena)


# **Metacaracter \S no espacio**

# In[25]:


re.findall(r"a\S",cadena)


# **Cuantificador {} repetición**

# In[26]:


re.findall(r"a{2}",cadena+ "aa aar")


# **Cuantificador + uno o más**
# 

# In[27]:


re.findall(r"\w+\s",cadena)


# **Cuantificador * cero o más**
# 

# In[28]:


re.findall(r"\w*\s",cadena)


# **Cuantificador {n,m} por lo menos _n_ a lo más _m_**
# 

# In[29]:


re.findall(r"a{1,2}",cadena+"aa arr")


# **Caracter especial ? estar o no**
# 

# In[30]:


re.findall(r"ar?",cadena)


# **Caracter especial . cualquier caraceter excepto nueva lineal**
# 

# In[31]:


re.findall(r"a.+",cadena)


# **Caracter especial ^ comienzo de la cadena**
# 

# In[32]:


re.findall(r"^a.+",cadena)


# **Caracter especial $ al final de la cadena**

# In[33]:


re.findall(r"a.+$",cadena)


# **Caracter especial \ para el caracter especial**
# 

# In[34]:


re.findall(r"s?",cadena+"?")


# In[35]:


re.findall(r"s\?",cadena+"?")


# **Operador or |**
# 

# In[36]:


re.findall(r"c|a",cadena)


# **Conjunto []**

# In[37]:


re.findall(r"[a-z]+\s",cadena)


# **Conjunto y negación**

# In[38]:


cadena


# In[39]:


re.findall(r"a[^\s]",cadena)


# In[40]:


re.findall(r"a\s",cadena)


# **Agrupar ()**

# In[41]:


texto = "Ana tienen 2 primos que con los que platica. Victor tiene 3 hermanos mientras que Julio tiene 2 perros"


# In[42]:


re.findall(r'[A-Za-z]+\s\w+\s\d+\s\w+', texto)


# **[A-Za-z]+ -> Ana Victor Julio**
# 

# In[43]:


re.findall(r'([A-Za-z]+)\s\w+\s\d+\s\w+', texto)


# In[44]:


res = re.findall(r'([A-Za-z]+)\s\w+\s\d+\s\w+', texto)


# In[45]:


res[0][0]


# **Repeticiones** 

# In[46]:


re.findall(r'(\d)+', "el numero es 55 213422")


# In[47]:


re.findall(r'(\d+)', "el numero es 55 213422")


# In[ ]:




