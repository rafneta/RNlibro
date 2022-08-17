#!/usr/bin/env python
# coding: utf-8

# ![](https://raw.githubusercontent.com/rafneta/RNlibro/master/imagenes/banner.png)
# 
# ```{contents}
# :depth: 4
# ```
# 
# # Machine Learning
# 
# 
# 
# > Alan Turing:  ["Computing Machinery and Intelligence"](https://www.csee.umbc.edu/courses/471/papers/turing.pdf) ¿Las máquinas pueden pensar? 
# 
# > "Inteligencia Artificial: Es la ciencia y la ingeniería para fabricar máquinas inteligentes, especialmente programas informáticos inteligentes. Está relacionado con la tarea similar de usar computadoras para comprender la inteligencia humana, pero la IA no tiene que limitarse a métodos que son biológicamente observables. "
#                                                                                           – Jhon MAcCarthy (2004) [WHAT IS ARTIFICIAL INTELLIGENCE?](https://homes.di.unimi.it/borghese/Teaching/AdvancedIntelligentSystems/Old/IntelligentSystems_2008_2009/Old/IntelligentSystems_2005_2006/Documents/Symbolic/04_McCarthy_whatisai.pdf)
# 
# 
# > "Machine Learning: Campo de estudio que da a las computadoras la habilidad para aprender sin ser explicitamente programadas"
#                                                                                                – Arthur L. Samuel (1959)  
# 
# 
# > "El aprednizaje denota cambios en el sistema, estos son adaptables en el sentido que permiten al sistema realizar la misma tarea o tareas una y otra vez más eficiente para la misma población"
#                                                                                          – Herbert Alexander Simon (1984)  
# 
# 
# > "Un programa de computadora se dice que aprende de la experiencia E con respecto a alguna  clase de tareas T y una medida de desempeño P y mejora con la experiencia E"
#                                                                                                       – Tom M. Mitchell (1998)
# 
# 
# 
# 
# 
# ![](https://i0.wp.com/smartboost.com/wp-content/uploads/2020/07/Deep-Learning-vs-Neural-Network.ai-06-2048x1152.png)
# Tomado de: _Deep Learning vs Neural Network: What’s the Difference?_ [](https://smartboost.com/blog/deep-learning-vs-neural-network/)

# ## Ciencia de datos
# 
# ![](https://sitiobigdata.com/wp-content/uploads/2018/08/Los-tres-n%C3%BAcleos-de-Data-Science.png)
# Tomado de: [Los tres nucleos de Data Science](https://sitiobigdata.com/2018/08/27/los-tres-nucleos-de-data-science/#)
# 
# 
# ![](https://pbs.twimg.com/media/DzAlXGBWwAAJjdz?format=jpg&name=large)
# Tomado del siguiente [twit](https://twitter.com/frederikbussler/status/1094415790349127680?lang=es)

# ## Machine Learning
# 
# ![](https://balkantimes.press/wp-content/uploads/2021/05/mail-2-10.jpg)
# 
# Tomado de [A taxonomy of machine learning and deep learning algorithms](https://balkantimes.press/en/artificial-intelligence-5-a-taxonomy-of-machine-learning-and-deep-learning-algorithms/)
# 
# ![](https://ars.els-cdn.com/content/image/1-s2.0-S157401372030071X-gr3.jpg)
# 
# Tomado de [Julia language in machine learning: Algorithms, applications, and open issues](https://www.sciencedirect.com/science/article/pii/S157401372030071X)

# Otra definición de ML es la siguiente:
# 
# > "El machine learning es un método de análisis de datos que automatiza  la construcción de modelos analíticos. Es una rama de la inteligencia  artificial basada en la idea de que los sistemas pueden aprender de  datos, identificar patrones y tomar decisiones con mínima intervención  humana"  [enlace](https://www.sas.com/es_mx/insights/analytics/machine-learning.html)
# 
# Simplificando bastante esta definición, el ML es un conjunto de  algoritmos diseñados para resolver problemas con el uso de datos. Estos  problemas se pueden clasificar en tres grandes grupos:
# 
# - **Aprendizaje supervisado.** Un modelo se ajusta  conociendo las entradas y las salidas asociadas. El objetivo es hacer  predicciones en presencia de incertidumbre. Este tipo de aprendizaje se  puede dividir en: 
# 
#   - **Clasificación.** Predecir respuestas discretas.
#   - **Regresión.** Predecir respuestas continuas.
# 
# - **Aprendizaje no supervisado.** Encuentra patrones  intrínsecos en datos de entrada que no estan asociados a ninguna salida. Este tipo de aprendizaje se puede dividir en
# 
#   - **Agrupación.** Agrupar los datos de acuerdo a sus características intrínsecas.
#   - **Reducción de dimensiones.** Reducir el número de características de los datos bajo algún criterio.
# 
# - **Otros algoritmos de aprendizaje.** Destacan los algoritmos de Reinformcement Learning. Este tipo de algoritmos determinan qué acciones debe escoger un agente  de software en un entorno dado con el fin de maximizar alguna noción de  “recompensa” o premio acumulado.

# ## Flujo de trabajo
# 
# Dependiendo del problema que se quiera resolver, hay un procedimiento genérico para abordarlo. Existen varias sugerencias y métodos para esto. Pienso que entre más sencillo se piense el procedimiento es mejor de entender, pero sin olvidar que una propuesta de solución se puede complicar de distintas formas.
# 
# ![](https://miro.medium.com/max/1400/1*bFZ1dIQ2ROifPt6YlyL6uA.png)
# 
# Esto no es exclusivo de una área de la ciencia, es un enfoque retomado en distintos áreas (Diseño mecatrónico, telmática, Biónica, Administración, etc.)
# 
# 
# En este curso, nos interesa el **modelo** y la **evaluación**. Pero es bueno saber que existen otras fases (no sólo las que se pueden observar) en la imagen anterior. En ese sentido, se verán algunas herramientas de las fases que no son nuestro objetivo, pero sin porfundizar en los temas.
# 
# Está información se encuentra en los Apéndices. 
# 
# 
# 

# In[ ]:




