from bs4 import BeautifulSoup


#Pon la palabra dedos en negrita.

f=open('index.html','rw')
soup = BeautifulSoup(f)



print soup.prettify()
