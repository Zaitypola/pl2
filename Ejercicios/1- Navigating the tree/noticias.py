# -*- coding: iso-8859-15 -*-
'''
-RSS de noticias, tomar titulares y primer párrafo. Imprimirlo

-Párrafos donde se mencione algo en concreto. raw_input.

'''
from bs4 import BeautifulSoup
import urllib2
import re
feeds = {'http://ep00.epimg.net/rss/elpais/portada.xml',
         'http://elmundo.feedsportal.com/elmundo/rss/portada.xml',
         'http://www.abc.es/rss/feeds/abcPortada.xml'
         }

search_input = raw_input('Inserte término de búsqueda: ')

for feed in feeds:
    print '=============================='
    soup = BeautifulSoup (urllib2.urlopen(feed))

    
    items = soup.find_all("item")    
    for item in items:
        if len(item.find_all(text=re.compile(search_input))) > 0:
            print item.title.text
            print item.description.text
        