# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup, SoupStrainer
import re
import random
'''
Formatear datos en una tabla, aquellos >500 en rojo, <500 en azul
'''

#Creamos un �rbol con un c�digo HTML vac�o, s�lo contiene las etiquetas b�sicas
soup = BeautifulSoup("<html><head></head><body></body></html>")
#Pedimos al usuario el n�mero de elementos, filas y columnas en las que quiere formatearlos.
number_elements = int(raw_input("Introduce el n�mero de elementos: "))
rows = int(raw_input("Introduce n�mero de filas: "))
columns = int(raw_input("Introduce n�mero de columnas: "))
#Generamos lista de n�meros aleatorios (de 0 a 1000).
number_list = [random.randint(0,2000) for r in xrange(number_elements)]
#Creamos una etiqueta <table> donde iremos almacenando los datos.
table = soup.new_tag("table")
#Iteramos por filas y columnas.
for i in range(0,rows):
    #Creamos una etiqueta <tr> (fila).
    tr_tag = soup.new_tag("tr")
    #Iteramos columnas.
    for j in range(0,columns):
        #Creamos una etiqueta <td> (columna).
        td_tag = soup.new_tag("td")
        #El n�mero lo almacenaremos en un <p> dentro del <td>.
        p_tag = soup.new_tag("p")
        #Generamos el NavigableString que representar� al n�mero.
        new_string = soup.new_string(str(number_list[(i*columns)+j]))
        #Asignamos el NavigableString a la etiqueta p.
        p_tag.string=new_string
        #A�adimos la etiqueta <p> a la columna <td> usando append (a�ade al final del contenido).
        td_tag.append(p_tag)
        #Modificamos el atributo de la colimna para una mejor presentaci�n.
        td_tag['align']="center"
        #Revisamos si el valor de la columna es mayor que 500 para aplicar el estilo correspondiente.
        if int(td_tag.string)>=750 and int(td_tag.string)<=1200 :
            td_tag['style']='color:green;border:solid'
        elif int(td_tag.string)>1200:
            td_tag['style']='color:red;border:solid'
        else:
            td_tag['style']='color:blue;border:solid'
        td_tag.string=td_tag.string+'�C'
        #A�adimos la columna a la fila.    
        tr_tag.append(td_tag)
    #Una vez que hemos finalizado todas las columnas de la fila, a�adimos a la tabla    
    table.append(tr_tag)
#Con la tabla al completo, la a�adimos al body del c�digo HTML.    
soup.body.append(table)
#Abrimos el archivo donde queremos almacenarlo.
file = open('../../web/tabla.html' ,'w')
#Escribimos en el archivo el texto formateado.
file.write(soup.prettify())
#Cerramos el descriptor.
file.close()
#Mensaje de salida.
print 'Fichero modificado y almacenado'

