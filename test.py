from bs4 import BeautifulSoup

soup = BeautifulSoup('<div>hola<p>pepe</p></div>')

print soup.string
print soup.text