#!/usr/bin/env python
# coding: utf-8

# ![](https://raw.githubusercontent.com/rafneta/RNlibro/master/imagenes/banner.png)
# 
# ```{contents}
# :depth: 4
# ```
# 
# # Instalación Anaconda
# 
# El [nucleo de Python](https://www.python.org/downloads/) no cuenta con todo el ambiente de programación cientifica. Instalar este nucleo y después instalar cada módulo no es una buena opción. 
# 
# Anaconda instala las librerias para programación cientifica y te permite administrar Python de forma sencilla. Además, Anaconda es  multiplataforma (disponible para Linux, macOS y Windows ) 
# 

# ## Anaconda instalación individual
# 
# Anaconda® es un administrador de paquetes, un administrador de entorno, una distribución de ciencia de datos Python / R y una colección de más de 7500 paquetes de código abierto. 
# 
# Se utilizará Python 3 para este laboratorio, para ello descarga el instalador para tu equipo (Linux, macOS, Windows)
# 
# 
# - [Instaladores Anaconda](https://www.anaconda.com/products/individual#Downloads)
# 
# ```{admonition} Si no tienes mucho espacio
# :class: tip
# 
# Si por alguna razón se quiere mantener el equipo con lo fundamental de Python e instalar conforme se requieran los paquete, se puede instalar [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
# 
# ```
# 
# De acuerdo a tu equipo, selecciona la pestaña indicada
# 
# 
# 
# ```{tabbed} macOS
# La documentación oficial de [instalación macOS](https://docs.anaconda.com/anaconda/install/mac-os/), puede llegar a parecer muy complicada, pero si se requiere algo en especifico vale la pena seguir. 
# 
# Se presenta un resumen de los pasos. Las imagenes  pueden ser distintas dependiendo de la versión del instalador
# 
# - Doble click en el instalador gráfico
# 
# - instalar en el directorio ~/opt (recomendación)
# 
# <div class = "video-w">
# <img src="https://docs.anaconda.com/_images/osx-install-type.png" widht=60%>
# </div>
# 
# -  Dependiendo de los permisos (normalmente lo instalo para todos los usuarios)
# <div class = "video-w">
# <img src="https://docs.anaconda.com/_images/osx-install-destination.png" widht=60%>
# </div>
# 
# - Si la instalación fue éxitosa
# <div class = "video-w">
# <img src="https://docs.anaconda.com/_images/osx-install-success.png" widht=60%>
# </div>
# 
# - En el Launchpad ubicar el icono de Anaconda-Navigator <img src = "
# https://docs.anaconda.com/_images/Navigator_Launchpad_icon.png"  width="20" height="20"> y dar doble click
# 
# <div class = "video-w">
# <img src="https://raw.githubusercontent.com/rafneta/CienciaDatosPythonCIDE/master/imagenes/ana_mac.png" widht=60%>
# </div>
# 
# ```
# 
# 
# ```{tabbed} Windows
# 
# La documentación oficial de [instalación Windows](https://docs.anaconda.com/anaconda/install/windows/#installing-on-windows), puede llegar a parecer muy complicada, pero si se requiere algo en especifico vale la pena seguir. 
# 
# Se presenta un resumen de los pasos. Las imagenes  pueden ser distintas dependiendo de la versión del instalador
# 
# - Doble click en el instalador gráfico
# 
# -  Dependiendo de los permisos (normalmente lo instalo para todos los usuarios)
# 
# - instalar en el directorio usual, puede que el instalador de alguna recomendación 
# 
# <div class = "video-w">
# <img src="https://docs.anaconda.com/_images/win-install-destination.png" widht=60%>
# </div>
# 
# - Se sugiere dejar las opciones recomendadas
# 
# <div class = "video-w">
# <img src="https://docs.anaconda.com/_images/win-install-options.png" widht=60%>
# </div>
# 
# - Si la instalación fue éxitosa
# <div class = "video-w">
# <img src="https://docs.anaconda.com/_images/win-install-complete.png" widht=60%>
# </div>
# 
# - Ubicar Anaconda-Navigator <img src = "
# https://docs.anaconda.com/_images/win-navigator2.png"  width="40" height="60"> y dar doble click
# 
# <div class = "video-w">
# <img src="https://docs.anaconda.com/_images/nav-defaults.png" widht=60%>
# </div>
# 
# ```
# 
# 
# ```{tabbed} Linux
# La documentación oficial de [instalación Linux](https://docs.anaconda.com/anaconda/install/linux/#installing-on-linux). Creo que para un usuario de Linux, seguir la guía no será mayor problema. 
# ```
# 
# 
# ## Conda
# 
# Anaconda instala un administrador de paquetes: _conda_. Por ejemplo, para actualizar todos los paquetes de Anaconda. Se ejecuta la sigeuinte instrucción
# 
# ```{admonition} Para continuar...
# :class: tip
# -  En macOS abrimos una terminal
# - En Windows buscamos Anaconda Prompt
# ```
#     conda update anaconda
#     
# 
# Lo anterior se puede realizar desde [anaconda-navigator](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/). Para consultar de forma rápida las instrucciones de conda, se puede revisar la siguientes [cheat sheet](https://www.interactivechaos.com/sites/default/files/data/conda_cheatsheet.pdf)

# ## Creación de entornos 
# 
# La creación de entornos es útil, por ejemplo, puede evitar el conflicto entre actualizaciones de paquetes no compatibles, trabajar con versiones especificas de los paquetes de forma independiente, etc.
# 
# 
# > Un entorno de anaconda es un directorio que contiene una colección especifica de paquetes y sus dependencias 
# 
# 
# Las siguientes instrucciones crean un ambiente y lo activan
# 
# ```{admonition} Para continuar...
# :class: tip
# -  En macOS abrimos una terminal
# - En Windows buscamos Anaconda Prompt
# ```
# 
# ````{panels}
# Código
# ^^^
# macOS
# 
#     conda create -n mientorno python=3.7
#     
#     conda activate mientorno
# 
# Windows
# 
#     conda create -n mientorno python=3.7
#     
#     activate mientorno
# 
# ---
# Explicación
# ^^^
# **_conda create_**. Es la instrucción de conda para crear el ambiente
# 
# **_-n_**. Es un argumento para indicar como se llamará el ambiente
# 
# **_mientorno_**. Es el nombre que se ha decido dar al ambiente
# 
# **_python =3.7_**. Este ambiente tendra instalado el nucleo de Python versión 3.7
# 
# **_conda activate mientorno_**. Instrucción para activar el entorno con nombre _mientorno_
# ````
# 
# Este entorno solo tiene instaldo el nucleo. Si se necesita realizar graficas, trabajar con arreglos, acceder a métodos númericos y realizar todo esto en un notebook, se instalan los paquetes correspondintes
# 
# ```{panels}
# Código
# ^^^
#     conda install numpy scipy matplotlib jupyter
# ---
# Explicación
# ^^^
# **_conda install_**. Es la instrucción para instarlar un paquete en el ambiente actualmente activo
# 
# **_numpy scipy matplotlib jupyter_**. Los cuatros pauqtees que se instalarán
# ```
# 
# Posiblemente se quiera instalar un paquete que se encuentre en un canal especifico.
# 
# > Los canales de conda son ubicaciones (direcciones especificas en internet) donde los paquetes están almacenados
# 
# 
# El canal _conda-forge_ contiene paquetes que podrían no estar en el canal pre establcecido de _conda_. Instalremos jupyterlab de este canal en el entorno (mientorno) activo actualmente  
# ```{panels}
# Código
# ^^^
#     conda install -c conda-forge jupyterlab
# ---
# Explicación
# ^^^
# **_conda install_**. Es la instrucción para instarlar un paquete en el ambiente actualmente activo
# 
# **_-c_**. Es un argumento para indicar el nombre del canal 
# 
# 
# **_conda-forge_**. Nombre del canal
# 
# **_jupyterlab_**. Paquete a instalar
# ```
# 
# Para desactivar el entorno activo, se ejecuta la siguiente instrucción
# 
# macOS
# 
#     conda deactivate
# 
# Windows
# 
#     deactivate
#     
# Lo anterior se puede realizar desde [anaconda-navigator](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/).
# 
# **Uso necesario de un entorno**. Actualmente hay un problema para ejecutar SPYDER (IDE similar a MATLAB y RStudio) en macOS 11 Big Sur, pero la creación de un entorno es una posible [solución a este problema](https://docs.spyder-ide.org/current/faq.html#troubleshooting-macos-bigsur).
# 
# ## Referencias
# 
# - Documentación de Anaconda [enlace](https://docs.anaconda.com/) 
# 
# - Documentación de Conda [enlace](https://conda.io/projects/conda/en/latest/)
