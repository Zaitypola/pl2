# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup
import urllib2
import smtplib
from email.mime.text import MIMEText

#Creamos el árbol a través de la URL.
soup = BeautifulSoup(urllib2.urlopen('https://play.google.com/store/devices/details?id=nexus_4_8gb&feature=microsite&hl=es'))
#Buscamos la etiqueta con clase CSS 'hardware-inventory-status'
tag = soup.find('div',class_='hardware-inventory-status')
#Variable de condición de parada
stock = False
while not stock:
    if 'no' not in tag.text:
        #Si la palabra 'no' está dentro del texto que encierra la etiqueta...
        stock = True
        #Imprimimos que hay stock
        print 'Hay stock'
        #Preparamos un correo para mandar al usuario
        message = MIMEText("Ya hay stock!!!")
        message["From"]="jorgecalmar@gmail.com"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        #Usamos nuestra cuenta de correo para hacer uso del servidor SMTP.
        server.login("<nombre_cuenta_correo>","<password_de_la_cuenta>")
        server.sendmail("jorgecalmar@gmail.com",{"jorgecalmar@gmail.com"},message.as_string())
        server.quit()
    else:
        print 'No hay stock'