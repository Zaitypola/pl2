# -*- coding: iso-8859-15 -*-
'''
Cuidado con CDATA - Parsear con "xml"
'''
from bs4 import BeautifulSoup
import urllib2
import re
from Tkinter import *

#Toma los XML donde debe buscar, el input de búsqueda y el campo donde dar la salida.
def search(feeds,search_input,t):
    #Por cada archivo XML...
    for feed in feeds:
        xml = urllib2.urlopen(feed)
        #Abrimos la URL y creamos el objeto.
        #Necesitamos usar el analizador sintáctico "xml" para poder saltarnos los CDATA.
        soup = BeautifulSoup(xml,"xml")
        #Buscamos las etiquetas <item> que contienen las noticias (RSS 2.0).
        items = soup.find_all("item")
        #Buscamos el primer campo <title> dentro del árbol para añadira la salida.
        t.insert(END,'- '+soup.title.text+'\n')
        #Por cada noticia encontrada...
        for item in items:
            #Si en su title o description encuentra el texto de búsqueda (ignorando mayúsculas).
            if item.find(["title","description"], text=re.compile(search_input,re.IGNORECASE)):
                #Sacamos de la noticia que cumplael requisito la información necesaria.
                title = item.title.string.encode('cp1252')
                description = re.sub(r'(<img .+>|<a.+>)','',item.description.string).encode('cp1252')
                link = item.link.string.encode('cp1252')
                date = item.pubDate.string.encode('cp1252')
                t.insert(END,date+'\n')
                t.insert(END,title+'\n')
                t.insert(END,description+'\n')
                t.insert(END,link+'\n')
    t.insert(END,'\n')