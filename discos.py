from bs4 import BeautifulSoup
import urllib2


url = urllib2.urlopen('http://www.demartina.com/lego-star-wars-c-73_29_50.html')
soup = BeautifulSoup(url)

def class_item_no_style(tag):
    return tag.has_key('class') and "item_box" in tag.get('class') and not tag.parent.has_key('style')

products = soup.find_all(class_item_no_style)

i=1
for product in products:
    print str(i)+'-'+product.find('div', {'class' : 'name l'}).string.encode('8859') #String, siguiente hijo de la etiqueta.
    i = i+1
