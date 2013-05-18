'''
Cambios en el codigo, cambiar la envoltura de un texto por otra.
Funciones wrap y unwrap, envolver en etiquetas un elemento o desenvolverlo.

Ejercicios: 
1-Aquellos textos que contengan cierta palabra se pongan en negrita (Wrap con <b> </bold>)
'''

from bs4 import BeautifulSoup
import re

#Envolvemos el p en un nuevo div con id="id2"

soup = BeautifulSoup('<html><head><title>Title</title></head><body><div id="id1"><p>foobar</p></div><body></html>')

matches = soup.find_all(text=re.compile("foo"))

for match in matches:
    match.wrap(soup.new_tag("b"))
    
print soup.prettify()

