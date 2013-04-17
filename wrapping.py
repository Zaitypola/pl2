from bs4 import BeautifulSoup
import urllib2

url = urllib2.urlopen('http://www.google.es')
soup = BeautifulSoup(url)

    
print soup.prettify()
