from bs4 import BeautifulSoup

soup = BeautifulSoup(open('web/index.html'))


print soup.a
print soup.p
print soup.img