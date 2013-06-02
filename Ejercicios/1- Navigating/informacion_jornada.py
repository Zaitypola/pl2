# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup
import urllib2
import re

'''
Retransmision de todos los partido en directo. Goles y minuto.
'''
#Funciones de las que haremos uso: print_matches y print_highlights_live
def print_matches(table):
    #Busco todas las filas de la tabla.
    rows = table.find_all('tr')
    for row in rows:
        #Equipo local y resultado local.
        local_team = row.find('td',class_="equipo local")
        local_result = local_team.next_sibling.next_sibling
        #Equipo visitante y resultado visitante.
        away_team = row.find('td',class_="equipo visitante")
        away_result = away_team.next_sibling.next_sibling
        #Link al resumen del partido.
        live_link = 'http://www.as.com'+row.find('a',class_="directo_new").get('href')
        #Imprimo el resultado global.
        print local_team.text.replace('\n','')+' '+local_result.text+' - '+away_result.text+' '+away_team.text.replace('\n','')
        #Llamo a la función que entra en el link del resumen e imprime los goles.
        print_highlights(live_link)
        print '\n'
        
def print_highlights(live_link):
    #Abro la URL del resumen.
    url_highlight = urllib2.urlopen(live_link)
    soup_highlight = BeautifulSoup(url_highlight)
    #Extraigo todas las filas de la tabla resumen con clase CSS 'gol'.
    goals = soup_highlight.find_all('tr',{'class' : 'gol'})
    #Le doy la vuelta a la lista ya que en la tabla aparecen desde el minuto 90' al 0'.
    goals.reverse()
    #Itero sobre los goles.
    for goal in goals:
        #Busco los datos de cada gol, minuto, descripción y acción.
        minuto = goal.find('td', {'class' : 'minuto'}).text
        accion = goal.find('td', {'class' : 'accion'}).text
        descripcion = goal.find('td', {'class' : 'desc'}).text
        print accion+' - '+minuto+' - '+descripcion
        
#Pedimos al usuario el número de la jornada de la que quiere información. Aquí comienza la ejecución.
fixture = raw_input("Introduce número de la jornada: ")
#Abrimos la URL usando urllib2.
url = urllib2.urlopen('http://www.as.com/resultados/futbol/primera/jornada-'+fixture+'/')
#Creamos el árbol a partir de la URL.
soup = BeautifulSoup(url)
#Recogemos el <div> que contiene la tabla de los resultados.
results_div = soup.find('div', class_="jornadas_tot")
#Busco la tabla dentro del <div>. find() devuelve la primera coincidencia que encuentre.
table=results_div.find('table')
#Imprimo el titulo de la competición, un <h2> con clase del mismo nombre.
print soup.find('h2',class_="tituloCompeticion").text
print '======================'
#imprimo fecha de la jornada.
print results_div.find('p',class_="jor").text+' **HIGHLIGHTS**\n'

#Llamo a la función que imprime los partidos.
print_matches(table)
