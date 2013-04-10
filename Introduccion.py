from bs4 import BeautifulSoup


f=open('web/index.html','r+')


soup = BeautifulSoup(f)


for link in soup.find_all('a'):
    link['class']='red'

f.close()

f=open('web/index.html','w')

f.write(soup.prettify())

f.close()


