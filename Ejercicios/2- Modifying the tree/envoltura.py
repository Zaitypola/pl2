'''
Cambios en el codigo, cambiar la envoltura de un texto por otra.
Funciones wrap y unwrap, envolver en etiquetas un elemento o desenvolverlo.

Ejercicios: 
1-Aquellos textos que contengan cierta palabra se pongan en negrita (Wrap con <b> </bold>)
'''

from bs4 import BeautifulSoup
import re
import urllib2

#Envolvemos el p en un nuevo div con id="id2"

soup = BeautifulSoup('<html><head><title>Title</title></head><body><div id="id1"><p>Hola</p></div><body></html>')

print soup.find(id="id1")

tag=soup.find('p').wrap(soup.new_tag("div"))
tag['id'] = "id2"
print soup.find(id="id1")
print tag.name



