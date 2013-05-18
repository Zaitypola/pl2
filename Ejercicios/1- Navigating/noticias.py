# -*- coding: iso-8859-15 -*-
'''
Cuidado con CDATA - Parsear con "xml"
'''
from bs4 import BeautifulSoup
import urllib2
import re
from Tkinter import *


def search(feeds,search_input,t):
    for feed in feeds:
        xml = urllib2.urlopen(feed)
        soup = BeautifulSoup(xml,"xml")
        items = soup.find_all("item")
        t.insert(END,'- '+soup.title.text+'\n')
        for item in items:
            if item.find(["title","description"], text=re.compile(search_input,re.IGNORECASE)):
                title = item.title.string.encode('cp1252')
                description = re.sub(r'(<img .+>|<a.+>)','',item.description.string).encode('cp1252')
                link = item.link.string.encode('cp1252')
                date = item.pubDate.string.encode('cp1252')
                t.insert(END,date+'\n')
                t.insert(END,title+'\n')
                t.insert(END,description+'\n')
                t.insert(END,link+'\n')
    t.insert(END,'\n')