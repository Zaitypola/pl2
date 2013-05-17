# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup
import urllib2
'''
Imprima el nombre, la referencia y el/los precio/precios de todos los productos que aperecen en la galeria. Algunos precios pueden tener un descuento, considere el precio nuevo y el antiguo.
Evite aquellos productos que esten envueltos en un 'div' con clase 'blueknow-item'.
'''

#Abro la URL usando la librería urllib2.
url = urllib2.urlopen('http://www.demartina.com/lego-star-wars-c-73_29_50.html')

#Genero el árbol a partir de la URL abierta.
soup = BeautifulSoup(url)

#Función filtro. La función filtro recibe una variable (tag) que es la que debe cumplir las siguientes
#condiciones: 
#- Debe tener definido el atributo class (has_key('class'))
#- 'item_box' debe estar dentro de la lista de clases aplicadas.
#- la clase 'blueknow-item' no debe estar dentro de la clase de la etiqueta padre.
# Los elementos dentro del div 'blueknow-item' son productos que se generan aleatoriamente
#y no están incluídos en el DOM original, por lo que realizar una búsqueda daría como resultado
#un conjunto de carácteres sin sentido ya que BeautifulSoup no sabe identificarlos.
def class_itembox_no_blueknow(tag):
    return tag.has_key('class') and "item_box" in tag.get('class') and not "blueknow-item" in  tag.parent.get('class')

#Hago una búsqueda aplicando la función filtro que hemos creado.
products = soup.find_all(class_itembox_no_blueknow)
#Itero sobre los productos encontrados.
for product in products:
    #Recojo los datos que deseo imprimir, nombre, precio y referencia. Aplico codificación necesaria para los carácteres especiales.
    #Busco los <div> con clase CSS 'name', 'price' y 'reference'. Uso  find ya que quiero la primera coincidencia que encuentre.
    name = product.find('div', {'class' : 'name'}).text.encode('8859')
    price_tag = product.find('div', {'class' : 'price'})
    reference = product.find('div', {'class' : 'reference'}) 
    
    print name
    #También podemos llamar a .text desde la variable. 'reference' es un número, no necesita codificación.
    print reference.text
    #Si en los contenidos de la etiqueta de precio tengo más de un elemento, quiere decir que tiene
    #referencias al precio antiguo y al nuevo, por lo que debe lleva un descuento aplicado.
    if len(price_tag.contents) == 1:
        print price_tag.string
    else:
        #De la misma forma busco el precio antiguo y nuevo por la clase CSS. Usamos class_ y no class
        #porque 'class' es palabra reservada de Python.
        old_price = product.find('div', class_='old').text
        new_price = product.find('div', class_='new').text
        #Para calcular los descuentos, quitamos el símbolo de € para poder sacar el float.
        old_float = float(old_price.replace('€',''))
        new_float = float(new_price.replace('€',''))    
        print 'Old price '+old_price
        print 'New Price '+new_price
        print 'Discount '+str(round(100-(new_float*100)/old_float,2))+'%'
    print '\n'
    
    