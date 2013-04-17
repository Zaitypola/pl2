from bs4 import BeautifulSoup
import urllib2




url = urllib2.urlopen('http://www.bloomberg.com/energy/')
soup = BeautifulSoup(url)


brent = soup.find_all('td')
i = 1
for b in brent:
    print i
    print b
    i=i+1