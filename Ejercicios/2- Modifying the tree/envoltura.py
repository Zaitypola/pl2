'''
Cambios en el codigo, cambiar la envoltura de un texto por otra.
Funciones wrap y unwrap, envolver en etiquetas un elemento o desenvolverlo.

Ejercicios: 
1-Aquellos textos que contengan cierta palabra se pongan en negrita (Wrap con <b> </bold>)
'''

from bs4 import BeautifulSoup


#Envolvemos el p en un nuevo div con id="id2"
'''
soup = BeautifulSoup('<html><head><title>Title</title></head><body><div id="id1"><p>Hola</p></div><body></html>')

print soup.find(id="id1")

tag=soup.find('p').wrap(soup.new_tag("div"))
tag['id'] = "id2"
print soup.find(id="id1")


'''

soup = BeautifulSoup("<b></b><p>Hello there</p>")
tag = soup.b
tag.append("Hello")
new_string = soup.new_string(" there")
tag.append(new_string)
#print tag
# <b>Hello there.</b>
#print tag.contents
# [u'Hello', u' there']
print tag.text
print soup.p.contents
newstr=soup.new_string(" bitch")
soup.p.append(newstr)
print soup.p.contents