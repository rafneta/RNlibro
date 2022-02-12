#!/usr/bin/env python
# coding: utf-8

# ![](https://raw.githubusercontent.com/rafneta/RNlibro/master/imagenes/banner.png)
# 
# ```{contents}
# :depth: 4
# ```
# 
# # Pandas
# 

# - [Página principal de Pandas](https://pandas.pydata.org/docs/index.html)
# - [Documentación](https://pandas.pydata.org/docs/reference/index.html)
# 
# Tomamos una muestra de la guía rápida de Pandas ([10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)), junto con un par de complementos.
# 

# ## Creamos objetos
# 

# In[70]:


import numpy as np
import pandas as pd


# In[3]:


s = pd.Series([1, 3, 5, np.nan, 6, 8])
s


# In[6]:


dates = pd.date_range("20130101", periods=6)
dates


# In[7]:


df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df


# In[8]:


df2 = pd.DataFrame(

    {

        "A": 1.0,

        "B": pd.Timestamp("20130102"),

        "C": pd.Series(1, index=list(range(4)), dtype="float32"),

        "D": np.array([3] * 4, dtype="int32"),

        "E": pd.Categorical(["test", "train", "test", "train"]),

        "F": "foo",

    }

)

df2


# In[9]:


df2.dtypes


# Dependiendo del editor de texto, se puede utilizar `<TAB>` para tener un despliegue de métodos.
#    
# Normalmente tenemos un archivo (local o remoto), con los datos. Tomaremos un ejemplo del repositorio de datos de [UCI, Machine Learning Repository](https://archive-beta.ics.uci.edu/)
# 
# 
# Se tomará el siguiente conjunto de datos [Adult](https://archive-beta.ics.uci.edu/ml/datasets/adult) (1996). UCI Machine Learning Repository.
# 
# - age: continuous.
# 
# - workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
# 
# - fnlwgt: continuous.
# 
# - education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
# 
# - education-num: continuous.
# 
# - marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
# 
# - occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
# 
# - relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
# 
# - race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
# 
# - sex: Female, Male.
# 
# - capital-gain: continuous.
# 
# - capital-loss: continuous.
# 
# - hours-per-week: continuous.
# 
# - native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
# 
# 

# In[12]:


datos = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
datos


# In[13]:


datos = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
    header = None)
datos


# In[23]:


columnas = ["age", "workclass", "fnlwgt", "education", "education_num",
            "marital_status", "occupation","relationship", "race", "sex",
            "capital_gain","capital_loss","hours-per-week", "native-country", "class"]

datos = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
    header = None,
    names = columnas
    )
datos


# ## Desplegar los datos
# 
# 

# In[24]:


df.head()


# In[25]:


df.tail()


# In[27]:


df.to_numpy()


# In[28]:


df2.to_numpy()


# In[29]:


df.describe()


# In[30]:


df.T


# In[31]:


df.sort_index(axis = 1, ascending = False)


# In[32]:


df.sort_values(by="B")


# ## Selección

# In[33]:


df["A"]


# In[34]:


df[0:3]


# In[41]:


df["20130102":"20130104"]


# ### Selección con etiqueta

# In[36]:


df.loc[dates[0]]


# In[37]:


df.loc[:, ["A", "B"]]


# In[38]:


df.loc["20130102":"20130104", ["A", "B"]]


# In[39]:


df.loc["20130102", ["A", "B"]]


# In[40]:


df.loc[dates[0], "A"]


# ### Selección por posición 

# In[42]:


df.iloc[3]


# In[43]:


df.iloc[3:5, 0:2]


# In[44]:


df.iloc[[1, 2, 4], [0, 2]]


# In[45]:


df.iloc[1:3, :]


# ### Indexado lógico

# In[46]:


df[df["A"] > 0]


# In[47]:


df[df > 0]


# ### Asignación

# In[49]:


s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
s1


# In[52]:


df.loc[:, "D"] = np.array([5] * len(df))
df


# ## Datos Faltantes

# In[53]:


df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
df1


# In[54]:


df1.dropna(how="any")


# In[55]:


df1.fillna(value=5)


# In[56]:


pd.isna(df1)


# ## Operaciones

# In[58]:


df.mean()


# In[59]:


df.mean(1)


# In[60]:


df.apply(np.cumsum)


# ## Gráficas

# In[64]:


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot(); # Investigar tarea moral


# In[67]:


df = pd.DataFrame(

    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]

)

df = df.cumsum()
df.plot();


# ## Guardar

# In[68]:


df.to_csv("foo.csv")


# In[69]:


df.to_excel("foo.xlsx", sheet_name="Sheet1")


# In[ ]:




