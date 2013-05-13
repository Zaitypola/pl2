# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup, SoupStrainer
import re
import random
'''
Formatear datos en una tabla, aquellos >500 en rojo, <500 en azul!!!
'''
soup = BeautifulSoup("<html><head></head><body></body></html>")
number_elements = int(raw_input("Introduce el número de elementos: "))
rows = int(raw_input("Introduce número de filas: "))
columns = int(raw_input("Introduce número de columnas: "))

number_list = [random.randint(0,1000) for r in xrange(number_elements)]
table = soup.new_tag("table")

for i in range(0,rows):
    tr_tag = soup.new_tag("tr")
    for j in range(0,columns):
        td_tag = soup.new_tag("td")
        p_tag = soup.new_tag("p")
        #p_tag['style']='color:black'
        new_string = soup.new_string(str(number_list[(i*columns)+j]))
        p_tag.string=new_string
        td_tag.append(p_tag)
        
        if int(td_tag.string)>500:
            td_tag['style']='color:red;border:solid'
        else:
            td_tag['style']='color:green;border:solid'
        tr_tag.append(td_tag)
    table.append(tr_tag)
    
soup.body.append(table)
file = open('../../web/tabla.html' ,'w')

file.write(soup.prettify())
file.close()
print 'Fichero modificado y almacenado'

