# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup
import urllib2
import re

'''
Retransmision de todos los partido en directo. Goles y minuto.
'''

def print_matches(table):
    rows = table.find_all('tr')
    for row in rows:
        local_team = row.find('td',class_="equipo local")
        local_result = local_team.next_sibling.next_sibling
        away_team = row.find('td',class_="equipo visitante")
        away_result = away_team.next_sibling.next_sibling
        live_link = 'http://www.as.com'+row.find('a',class_="directo_new").get('href')
        print local_team.text.replace('\n','')+' '+local_result.text+' - '+away_result.text+' '+away_team.text.replace('\n','')
        print_highlights(live_link)
        print '\n'
        
def print_highlights(live_link):
    url_highlight = urllib2.urlopen(live_link)
    soup_highlight = BeautifulSoup(url_highlight)
    goals = soup_highlight.find_all('tr',{'class' : 'gol'})
    goals.reverse()
    for goal in goals:
        minuto = goal.find('td', {'class' : 'minuto'}).text
        accion = goal.find('td', {'class' : 'accion'}).text
        descripcion = goal.find('td', {'class' : 'desc'}).text
        print accion+' - '+minuto+' - '+descripcion


url = urllib2.urlopen('http://www.as.com/resultados/futbol/primera/jornada-34/')
soup = BeautifulSoup(url)

results_div = soup.find('div', class_="jornadas_tot")
table=results_div.find('table')

print soup.find('h2',class_="tituloCompeticion").text
print '======================'
print results_div.find('p',class_="jor").text+' **HIGHLIGHTS**\n'


print_matches(table)
