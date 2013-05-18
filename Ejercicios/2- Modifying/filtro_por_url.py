from bs4 import BeautifulSoup
import re
import urllib2

url = urllib2.urlopen('http://www.boston.com/bigpicture/2013/03/daily_life_february_2013.html')
soup = BeautifulSoup(url)

for link in soup.find_all('img', src=re.compile('^http://inapcache.+/site_graphics/.+')):
    result = re.split('site_graphics', link.get('src'))
    link['src']=result[0]+'new_site'+result[1]
    print link.get('src')
