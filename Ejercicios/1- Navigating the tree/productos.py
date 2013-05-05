# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup
import urllib2
'''
Imprima el nombre, la referencia y el/los precio/precios de todos los productos que aperecen en la galeria. Algunos precios pueden tener un descuento, considere el precio nuevo y el antiguo.
Evite aquellos productos que esten envueltos en un 'div' con clase 'blueknow-item'.
 
Qué aprendemos?
1- Abrir una url.
2- Realizar un filtro a partir de una funcion para find_all().
3- Aplicar busquedas a partir de un nodo que no sea la raiz.
4- Usar diferentes codificaciones para caracteres extranios que no sean unicode.
5- Diferentes formas de llamar a find().
'''


url = urllib2.urlopen('http://www.demartina.com/lego-star-wars-c-73_29_50.html')
soup = BeautifulSoup(url)

def class_itembox_no_blueknow(tag):
    return tag.has_key('class') and "item_box" in tag.get('class') and not "blueknow-item" in  tag.parent.get('class')

products = soup.find_all(class_itembox_no_blueknow)

for product in products:
    name = product.find('div', {'class' : 'name'}).text.encode('8859')
    price_tag = product.find('div', {'class' : 'price'})
    reference = product.find('div', {'class' : 'reference'}) 
    
    print name
    print reference.text
    
    if len(price_tag.contents) == 1:
        print price_tag.string
    else:
        old_price = product.find('div', class_='old').text
        new_price = product.find('div', class_='new').text
        old_float = float(old_price.replace('€',''))
        new_float = float(new_price.replace('€',''))    
        print 'Old price '+old_price
        print 'New Price '+new_price
        print 'Discount '+str(round(100-(new_float*100)/old_float,2))+'%'
    print '\n'
    
    