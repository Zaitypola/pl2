from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><p class='clase'>data</html>")



print soup.find('p')['class']