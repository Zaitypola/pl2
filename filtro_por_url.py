from bs4 import BeautifulSoup
import re
import urllib2


#mover de site_graphics a otra localizacion dentro del servidor.
url = urllib2.urlopen('http://www.boston.com/bigpicture/2013/03/daily_life_february_2013.html')
soup = BeautifulSoup(url)

for link in soup.find_all('img'):
    if re.match('^http://inapcache.+/site_graphics/.+',link.get('src')):
        print link['src']
        result = re.split('site_graphics',link.get('src'))
        link['src']=result[0]+'new_site'+result[1]
        print link['src']




"""url_tochange = 'http://inapcache.boston.com/universal/site_graphics/blogs/bigpicture/feb13dailylife/bp35.jpg'
result = re.split('site_graphics', url_tochange)
print url_tochange
print result[0]+'new_site'+result[1]"""