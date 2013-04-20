from bs4 import BeautifulSoup
import urllib2

url = urllib2.urlopen('http://www.google.es')
soup = BeautifulSoup(url)

    
a_tag = soup.a

print a_tag

a_tag.name = "b"

print a_tag