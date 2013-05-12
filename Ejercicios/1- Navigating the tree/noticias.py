# -*- coding: iso-8859-15 -*-
'''
Cuidado con CDATA - Parsear con "xml"
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
    for feed in feeds:
        xml = urllib2.urlopen(feed)
        soup = BeautifulSoup(xml,"xml")
        items = soup.find_all("item") 
        print '- '+soup.title.text
        for item in items:
            if item.find(["title","description"], text=re.compile(search_input,re.IGNORECASE)):
                title = item.title.string
                description = re.sub(r'(<img .+>|<a.+>)','',item.description.string)
                link = item.link.string
                date = item.pubDate.string
                print date
                print title
                print description
                print link
                print '\n'
            
    print '\n'