from Tkinter import *
import noticias


def search():
    feeds = []
    sources = []
    t.configure(state='normal')

    t.delete(1.0,END)

    if var_ABC.get() == 1:
        sources.append(abc)
    if var_elMundo.get() == 1:
        sources.append(elMundo)
    if var_elPais.get() == 1:
        sources.append(elPais)
        
    for source in sources:
        feeds.append(source[var_Category.get()])
    
    noticias.search(feeds,var_searchInput.get(),t)
    t.configure(state='disabled')
    

categories = [
        ("Latest news", 0),
        ("Sports", 1),
        ("National", 2),
        ("International", 3),
    ]      

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

root = Tk()
root.geometry("1024x768")

root.title("News feeds searcher")
frame=Frame(root)
frame.pack(fill=BOTH, expand=1)

var_elMundo = IntVar()
var_elPais = IntVar()
var_ABC = IntVar()
var_Category = IntVar()
var_searchInput = StringVar()

var_Category.set(0)

Label(frame, text="Categories").pack(anchor=W)

for category,value in categories:
    Radiobutton(frame, text=category,variable=var_Category, value=value).pack(anchor=W)

Label(frame, text="Source").place(x=150,y=0)
Checkbutton(frame, text="El Mundo",variable=var_elMundo).place(x=150,y=15)
Checkbutton(frame, text="El Pais",variable=var_elPais).place(x=150,y=30)
Checkbutton(frame, text="ABC",variable=var_ABC).place(x=150,y=45)

t=Text(frame, height=26, width=300)
t.place(x=0,y=150)
Entry(frame,textvariable=var_searchInput).place(x=0,y=120)
Button(frame, text="Search",command=search).place(x=130,y=120)




root.mainloop()
