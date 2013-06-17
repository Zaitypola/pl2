# -*- coding: iso-8859-15 -*-


from Tkinter import *
import noticias
import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        result = Tk()
        scrollbar = Scrollbar(result)
        scrollbar.pack(side=RIGHT, fill=Y)

        result_text = Text(result, wrap=WORD, yscrollcommand=scrollbar.set)
        result_text.pack()

        scrollbar.config(command=result_text.yview)



        '''Variables que usaremos en el programa. Partimos de dos listas:

            feeds: Almacena la lista de ficheros XML que finalmente usaremos en la búsqueda.
                   Iremos completándola en función de las fuentes que hayamos seleccionado y de
                   las categorías.

            sources: Almacenamos la lista de fuentes seleccionadas en la consola.
                     De cada fuente almacenamos todas categorías accesibles.
                     Según la selección de categoría, almacenaremos en feeds la URL
                     de los XML correspondientes.

        '''

        feeds = []
        sources = []
        #Variables que controlan la selección de fuentes.
        if var_ABC.get() == 1:
            sources.append(abc)
        if var_elMundo.get() == 1:
            sources.append(elMundo)
        if var_elPais.get() == 1:
            sources.append(elPais)
        #Añadimos a feeds las categorías de las fuentes elegidas.
        for source in sources:
            feeds.append(source[var_Category.get()])
        #Llamamos a la función 'search' con los XML, el término de búsqueda y la ventana de salida.
        noticias.search(feeds,var_searchInput.get(),result_text)
        #Configuramos la salida como sólo de escritura.
        result_text.configure(state='disabled')
        result.title(var_searchInput.get())
        result.mainloop()

def search():
    thread=MyThread()
    thread.run()

#Lista de categorías.
categories = [
        ("Latest news", 0),
        ("Sports", 1),
        ("National", 2),
        ("International", 3),
    ]
#Lista de XML, cada uno de una categoría diferente.
abc = ['http://www.abc.es/rss/feeds/abc_ultima.xml',
       'http://www.abc.es/rss/feeds/abc_Deportes.xml',
       'http://www.abc.es/rss/feeds/abcPortada.xml',
       'http://www.abc.es/rss/feeds/abc_Internacional.xml']

elMundo= ['http://elmundo.feedsportal.com/elmundo/rss/portada.xml',
         'http://elmundo.feedsportal.com/elmundodeporte/rss/portada.xml',
         'http://elmundo.feedsportal.com/elmundo/rss/espana.xml',
         'http://elmundo.feedsportal.com/elmundo/rss/internacional.xml']

elPais = ['http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
           'http://ep00.epimg.net/rss/deportes/portada.xml',
           'http://ep00.epimg.net/rss/elpais/portada.xml',
           'http://ep00.epimg.net/rss/internacional/portada.xml']

#Creamos un hilo para ejecutar ambas ventanas en paralelo
#Creamos la raíz de la interfaz, todos los elementos deben ir acopladas a ésta.
root = Tk()
#Modificamos la resolución al crearse.
root.geometry("300x200")
#Título de la ventana
root.title("News feeds searcher")
#Creamos una ventana principal, vacía.
frame=Frame(root)
#Añadimos la ventana al objeto raíz.
frame.pack(fill=BOTH, expand=1)
#Variables que almacenarán los valores de la selección de fuentes.
var_elMundo = IntVar()
var_elPais = IntVar()
var_ABC = IntVar()
#Almacena la categoría seleccionada.
var_Category = IntVar()
#Almacena el input del cuadro de búsqueda.
var_searchInput = StringVar()
#Por defecto elegida la primera categoría.
var_Category.set(0)
#Etiqueta creada para las categorías.
Label(frame, text="Categories").pack(anchor=W)
#Botón de selección de categorías. Iteramos sobre categoría y el valor para crear los botones.
for category,value in categories:
    Radiobutton(frame, text=category,variable=var_Category, value=value).pack(anchor=W)
#Etiqueta para la fuente.
Label(frame, text="Source").place(x=150,y=0)
#Botones para la fuente.
Checkbutton(frame, text="El Mundo",variable=var_elMundo).place(x=150,y=15)
Checkbutton(frame, text="El Pais",variable=var_elPais).place(x=150,y=30)
Checkbutton(frame, text="ABC",variable=var_ABC).place(x=150,y=45)
#Texto de salida de la búsqueda.
#Texto para el input de la búsqueda.
Entry(frame,textvariable=var_searchInput).place(x=0,y=120)
#Botón que llama a la función search.
Button(frame, text="Search",command=search).place(x=130,y=120)
#LLamar a la ventana para correr la aplicación.
#Seguir en el fichero 'noticias.py' donde se hace la búsqueda.
root.mainloop()