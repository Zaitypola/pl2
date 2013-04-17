from bs4 import BeautifulSoup
import re
import urllib2


#mover de site_graphics a otra localizacion dentro del servidor.
url = urllib2.urlopen('http://www.boston.com/bigpicture/2013/03/daily_life_february_2013.html')
soup = BeautifulSoup(url)
'''
for link in soup.find_all('img'):
    src = link.get('src')
    if re.match('^http://inapcache.+/site_graphics/.+', src):
        result = re.split('site_graphics', src)
        link['src']=result[0]+'new_site'+result[1]
        print link.get('src')
 '''
 
for link in soup.find_all(src=re.compile('^http://inapcache.+/site_graphics/.+')):
    src=link.get('src')
    result = re.split('site_graphics', src)
    link['src']=result[0]+'new_site'+result[1]
    print link.get('src')       
        
