![](https://raw.githubusercontent.com/rafneta/CienciaDatosPythonCIDE/master/imagenes/banner.png)


# Scraping, HTML

Los componentes de una página web, archivo html, css y javascript (en su forma más sencilla)

archivo.html

     <html>
     <head>
     </head>
     <body>
     <p >
    Parrafo 1
    </p>
    <p >
    Parrafo 2
    </p>
    </body>
    </html>

archivo.css

    .verde{
     background:green;
      }

    .rojo{
    background:red;
     }


import re
import requests
from bs4 import BeautifulSoup


link = "http://rafneta.github.io/Notas/NotasSyS/index.html"
pagina = requests.get(link)
#pagina.content
pagina.content[0:500]

pes1=re.findall(r"(<p>[\s+|\n+|\w+]?.+</p>)",str(pagina.content,'utf-8'))
print(len(pes1))
pes1[0:3]

soup = BeautifulSoup(pagina.content, 'html.parser')
pes=soup.findAll("p")
print(len(pes))
pes[0:3]

a=soup.findAll("p", class_ = "justo")
a

help(a[1])

a[1].text

texto=re.findall(r"[^\n].+",a[1].text)
texto=re.findall(r"\w+\s?",texto[0])
" ".join(texto)

link = "https://www.amazon.com.mx/"
pagina = requests.get(link)
#pagina.content
pagina.content

