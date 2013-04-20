'''
goals = soup.find_all('tr',{'class' : 'gol'})
goals.reverse()
for goal in goals:
    minuto = goal.find('td', {'class' : 'minuto'}).text
    accion = goal.find('td', {'class' : 'accion'}).text
    descripcion = goal.find('td', {'class' : 'desc'}).text
    
    print accion+' - '+minuto+' - '+descripcion
    
'''