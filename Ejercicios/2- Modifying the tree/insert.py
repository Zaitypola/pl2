# -*- coding: iso-8859-15 -*-
from bs4 import BeautifulSoup

'''

insert_before() a certain tag or element
 insert_after() same as above
insert() at the end of the parent's contents

'''
'''
url = urllib2.urlopen('http://www.accuweather.com/en/es/sevilla/306733/may-weather/306733?monyr=5/1/2013&view=table')
table = SoupStrainer("table")
soup = BeautifulSoup(url, "html.parser", parse_only=table)

#print soup.prettify()
'''
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
    
tag = soup.a
print tag.text
print tag.string
tag.string = "New link text."
