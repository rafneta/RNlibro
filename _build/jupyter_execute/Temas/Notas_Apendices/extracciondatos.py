#!/usr/bin/env python
# coding: utf-8

# ![](https://raw.githubusercontent.com/rafneta/RNlibro/master/imagenes/banner.png)
# 
# ```{contents}
# :depth: 4
# ```
# 
# # Extracción de datos
# 
# Con _pandas_ reaizamos una adquisición de datos de un archivo que directamente estaba disposible en la web. Los datos pueden estar en diferentes fuentes
# 
# - archivos locales manipulables (xls, csv, tsv, dta, docs, txt, etc.)
# - archivos remotos manipulables (url de repositorios) 
# - Acceso mediante una API (Application Programming Interface, kaggle, etc.)
# - En páginas web (Web Scraping)
# - archivos no manipulables (por ejemplo: pdf)
# - Bases de datos
# 
# En particular, se tomará un ejemplo sencillo de Web Scraping, para lo cual se hablará un poco sobre expresiones regulares, para ello es necesario tener instalado los modulos _re_, _request_, y _beautifulsoup4_. El módulo _re_ es estándar
# 
# ```
# pip install requests
# conda install -c anaconda requests 
# pip install beautifulsoup4
# conda install -c anaconda beautifulsoup4
# ```
# 
# Como ejemplo adicional se puede revisar
# 
# - [Lectura de pdf](https://www.youtube.com/watch?v=s8XjEuplx_U&t=3229s)
# 
# 
