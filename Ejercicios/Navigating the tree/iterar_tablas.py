'''
Retransmision de todos los partido en directo. Goles y minuto
'''

from bs4 import BeautifulSoup
import urllib2


def tag_a_match(tag):
    return tag.name == 'a' and tag.parent.has_key('class') and "tv" in tag.parent.get('class')

base_url = urllib2.urlopen('http://www.as.com/resultados/futbol/primera/jornada-31/')
base_soup = BeautifulSoup(base_url)

list_url = base_soup.find_all(tag_a_match)


'''
goals = soup.find_all('tr',{'class' : 'gol'})
goals.reverse()
for goal in goals:
    minuto = goal.find('td', {'class' : 'minuto'}).text
    accion = goal.find('td', {'class' : 'accion'}).text
    descripcion = goal.find('td', {'class' : 'desc'}).text
    
    print accion+' - '+minuto+' - '+descripcion
    
'''