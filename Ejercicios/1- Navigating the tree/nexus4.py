from bs4 import BeautifulSoup
import urllib2
import smtplib
from email.mime.text import MIMEText


soup = BeautifulSoup(urllib2.urlopen('https://play.google.com/store/devices/details?id=nexus_4_8gb&feature=microsite&hl=es'))

tag = soup.find('div',class_='hardware-inventory-status')
stock = False
while not stock:
    if 'no' not in tag.text:
        stock = True
        print 'Hay stock'
        message = MIMEText("Ya hay stock!!!")
        message["From"]="jorgecalmar@gmail.com"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login("jorgecalmar","pastaylomo23")
        server.sendmail("jorgecalmar@gmail.com",{"jesus.talamante87@gmail.com"},message.as_string())
        server.quit()
    else:
        print 'No hay stock'