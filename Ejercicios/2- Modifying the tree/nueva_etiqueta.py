'''
Cada vez que la palabra Google en un parrafo, convertirlo en un link.
Aniaadir nuevas etiquetas al arbol.
'''

from bs4 import BeautifulSoup
import urllib2
import re


url=urllib2.urlopen('http://www.elmundotoday.com/2013/04/los-filtros-de-instagram-se-declaran-cansados-de-ocultar-tanta-miseria/')
soup = BeautifulSoup(url)
a_tag = soup.new_tag('a', href='http://www.instagram.com')
a_tag.string = soup.new_string('Instagram')

p_tags = soup.find_all('p',text=re.compile('.+Instagram.+'))

for p_tag in p_tags:
    print p_tag.parent
    print '\n'