# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup
import re
import urllib2


#Abrimos la url con urllib2
url = urllib2.urlopen('http://www.boston.com/bigpicture/2013/03/daily_life_february_2013.html')
#Creamos el árbol a partir de la URL.
soup = BeautifulSoup(url)
#Iteramos sobre las imágenes. Elegimos aquellas cuyo 'src' (la URL de la imagen) cumplen el requisito de la expresión regular.
for link in soup.find_all('img', src=re.compile('^http://inapcache.+/site_graphics/.+')):
    #Guardamos en 'result' las partes de la cadena de la URL de la imagen quitándole la parte a modificar.
    result = re.split('site_graphics', link.get('src'))
    #Modificamos el 'src' cambiando site_graphics con new_site.
    link['src']=result[0]+'new_site'+result[1]
    #Imprimimos la fuente para ver los resultados.
    print link.get('src')
