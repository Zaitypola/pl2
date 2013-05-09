# -*- coding: iso-8859-15 -*-
'''
-RSS de noticias, tomar titulares y primer párrafo. Imprimirlo

-Párrafos donde se mencione algo en concreto. raw_input.
buscar por text= en find o find_all, busca por atributo.string. si la etiqueta tiene .string a None como es en
el caso de item, la búsqueda no tendrá efecto. String es None cuando tiene texto encerrado en otras etiquetas.
title y description si tienen string directamente.

Cuidado con CDATA

'''
from bs4 import BeautifulSoup
import urllib2
import re

feeds = {'http://ep00.epimg.net/rss/elpais/portada.xml',
         'http://elmundo.feedsportal.com/elmundo/rss/portada.xml',
         'http://www.abc.es/rss/feeds/abcPortada.xml'
         }

while True:
    search_input = raw_input('Inserte término de búsqueda: ')
    
    xml = urllib2.urlopen('http://www.abc.es/rss/feeds/abcPortada.xml')
    soup = BeautifulSoup(xml)
    
    
    
    matches = soup.find_all(["title","description"],text=re.compile(search_input,re.IGNORECASE))
    
    for match in matches:
        item = match.parent
        title = item.title.string
        description = re.sub(r'(<img .+>|<a.+>)','',item.description.string)
        link = item.link.string
        date = item.pubdate.string
        print date
        print title
        print description
        print link
        print '\n'
