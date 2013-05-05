from bs4 import BeautifulSoup
import re
import urllib2

'''
Usted esta de becario en una empresa y le informan de que algunas imagenes que se muestran en la pagina web han de ser movidas a otra localizacion en el servidor.
Las imagenes seran aquellas que se encuentren en la ruta http://inapcache.boston.com/universal/site_graphics/, teniendo que moverlas a http://inapcache.boston.com/universal/new_site/.
Modifique la localizacion de cada imagen en la galeria que se encuentre en la ruta original por la nueva localizacion e imprima los cambios.

Que aprendemos?
1- Abrir url externa.
2- Busqueda en el arbol aplicando un filtro de etiquetas por valores de atributos que cumplen una expresion regular simple.
3- Modificacion del atributo en el arbol original.
'''

url = urllib2.urlopen('http://www.boston.com/bigpicture/2013/03/daily_life_february_2013.html')
soup = BeautifulSoup(url)

for link in soup.find_all('img', src=re.compile('^http://inapcache.+/site_graphics/.+')):
    result = re.split('site_graphics', link.get('src'))
    link['src']=result[0]+'new_site'+result[1]
    print link.get('src')
