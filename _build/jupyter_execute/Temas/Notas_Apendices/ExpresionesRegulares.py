![](https://raw.githubusercontent.com/rafneta/CienciaDatosPythonCIDE/master/imagenes/banner.png)


# Expresiones regulares

import re

cadena = "cadena que tiene\n dos partes"
cadena

print(cadena)

cadena.splitlines()

sepcad = cadena.splitlines()
sepcad

"-------".join(sepcad)

cadena.find("oso")

help(str.find)

cadena.find("a",6)

cadena.find("tien")

cadena.count("a")

cadena.replace("a","-----")

cadena


Una expresión regular es una cadena que contiene

- Caraceteres "s" "st"
- Metacaracteres \d \s \w describen secuencias 
- Cuantificadores + * 


re.findall(r"c",cadena)

re.split(r"a",cadena)

re.sub(r"a","---",cadena)

**Metacaracter \d Digito**


re.findall(r"c\d",cadena)

**Metacaracter \D No digito**


re.findall(r"c\D",cadena)

**Metacaracter \w palabra**


re.findall(r"\w",cadena)

**Metacaracetr \W no-palabra**


re.findall(r"\W",cadena)

cadena

re.findall(r"a\w",cadena)

re.findall(r"a\W",cadena)

**Metacaracter \s espacio**


re.findall(r"a\s",cadena)

**Metacaracter \S no espacio**

re.findall(r"a\S",cadena)

**Cuantificador {} repetición**

re.findall(r"a{2}",cadena+ "aa aar")

**Cuantificador + uno o más**


re.findall(r"\w+\s",cadena)

**Cuantificador * cero o más**


re.findall(r"\w*\s",cadena)

**Cuantificador {n,m} por lo menos _n_ a lo más _m_**


re.findall(r"a{1,2}",cadena+"aa arr")

**Caracter especial ? estar o no**


re.findall(r"ar?",cadena)

**Caracter especial . cualquier caraceter excepto nueva lineal**


re.findall(r"a.+",cadena)

**Caracter especial ^ comienzo de la cadena**


re.findall(r"^a.+",cadena)

**Caracter especial $ al final de la cadena**

re.findall(r"a.+$",cadena)

**Caracter especial \ para el caracter especial**


re.findall(r"s?",cadena+"?")

re.findall(r"s\?",cadena+"?")

**Operador or |**


re.findall(r"c|a",cadena)

**Conjunto []**

re.findall(r"[a-z]+\s",cadena)

**Conjunto y negación**

cadena

re.findall(r"a[^\s]",cadena)

re.findall(r"a\s",cadena)

**Agrupar ()**

texto = "Ana tienen 2 primos que con los que platica. Victor tiene 3 hermanos mientras que Julio tiene 2 perros"

re.findall(r'[A-Za-z]+\s\w+\s\d+\s\w+', texto)

**[A-Za-z]+ -> Ana Victor Julio**


re.findall(r'([A-Za-z]+)\s\w+\s\d+\s\w+', texto)

res = re.findall(r'([A-Za-z]+)\s\w+\s\d+\s\w+', texto)

res[0][0]

**Repeticiones** 

re.findall(r'(\d)+', "el numero es 55 213422")

re.findall(r'(\d+)', "el numero es 55 213422")

