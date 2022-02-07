![](https://raw.githubusercontent.com/rafneta/RNlibro/master/imagenes/banner.png)

```{contents}
:depth: 4
```

# Pandas


- [Página principal de Pandas](https://pandas.pydata.org/docs/index.html)
- [Documentación](https://pandas.pydata.org/docs/reference/index.html)

Tomamos una muestra de la guía rápida de Pandas ([10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)), junto con un par de complementos.


## Creamos objetos


import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

dates = pd.date_range("20130101", periods=6)
dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df

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

df2.dtypes

Dependiendo del editor de texto, se puede utilizar `<TAB>` para tener un despliegue de métodos.
   
Normalmente tenemos un archivo (local o remoto), con los datos. Tomaremos un ejemplo del repositorio de datos de [UCI, Machine Learning Repository](https://archive-beta.ics.uci.edu/)


Se tomará el siguiente conjunto de datos [Adult](https://archive-beta.ics.uci.edu/ml/datasets/adult) (1996). UCI Machine Learning Repository.

- age: continuous.

- workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.

- fnlwgt: continuous.

- education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.

- education-num: continuous.

- marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.

- occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.

- relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.

- race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.

- sex: Female, Male.

- capital-gain: continuous.

- capital-loss: continuous.

- hours-per-week: continuous.

- native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.



datos = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
datos

datos = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
    header = None)
datos

columnas = ["age", "workclass", "fnlwgt", "education", "education_num",
            "marital_status", "occupation","relationship", "race", "sex",
            "capital_gain","capital_loss","hours-per-week", "native-country", "class"]

datos = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
    header = None,
    names = columnas
    )
datos

## Desplegar los datos



df.head()

df.tail()

df.to_numpy()

df2.to_numpy()

df.describe()

df.T

df.sort_index(axis = 1, ascending = False)

df.sort_values(by="B")

## Selección

df["A"]

df[0:3]

df["20130102":"20130104"]

### Selección con etiqueta

df.loc[dates[0]]

df.loc[:, ["A", "B"]]

df.loc["20130102":"20130104", ["A", "B"]]

df.loc["20130102", ["A", "B"]]

df.loc[dates[0], "A"]

### Selección por posición 

df.iloc[3]

df.iloc[3:5, 0:2]

df.iloc[[1, 2, 4], [0, 2]]

df.iloc[1:3, :]

### Indexado lógico

df[df["A"] > 0]

df[df > 0]

### Asignación

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
s1

df.loc[:, "D"] = np.array([5] * len(df))
df

## Datos Faltantes

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
df1

df1.dropna(how="any")

df1.fillna(value=5)

pd.isna(df1)

## Operaciones

df.mean()

df.mean(1)

df.apply(np.cumsum)

## Gráficas

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot(); # Investigar tarea moral

df = pd.DataFrame(

    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]

)

df = df.cumsum()
df.plot();


## Guardar

df.to_csv("foo.csv")

df.to_excel("foo.xlsx", sheet_name="Sheet1")

