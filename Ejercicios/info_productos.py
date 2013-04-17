from bs4 import BeautifulSoup
import urllib2

'''
Imprima el nombre, la referencia y el/los precio/precios de todos los productos que aperecen en la galeria. Algunos precios pueden tener un descuento, considere el precio nuevo y el antiguo.
Evite aquellos productos que esten envueltos en un 'div' con clase 'blueknow-item'.
 
Que aprendemos?
1- Abrir una url.
2- Realizar un filtro a partir de una funcion para find_all().
3- Aplicar busquedas a partir de un nodo que no sea la raiz.
4- Usar diferentes codificaciones para caracteres extranios que no sean unicode.
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
    if price_tag.find('div', class_='old') is None:
        print price_tag.text
    else:
        print 'Old price '+product.find('div', class_='old').text
        print 'New Price '+product.find('div', class_='new').text

    print '\n'