# -*- coding: iso-8859-15 -*-
'''
-RSS de noticias, tomar titulares y primer p�rrafo. Imprimirlo

-P�rrafos donde se mencione algo en concreto. raw_input.

'''
from bs4 import BeautifulSoup
import urllib2
import re
feeds = {'http://ep00.epimg.net/rss/elpais/portada.xml',
         'http://elmundo.feedsportal.com/elmundo/rss/portada.xml',
         'http://www.abc.es/rss/feeds/abcPortada.xml'
         }

search_input = raw_input('Inserte t�rmino de b�squeda: ')

for feed in feeds:
    soup = BeautifulSoup (urllib2.urlopen(feed))
    print soup.title.text
    items = soup.find_all(text=re.compile(search_input))
    for item in items:
        if isinstance(item.title,BeautifulSoup.CData):
            print item.title.data