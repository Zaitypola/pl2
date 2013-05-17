import pygtk
import gtk
import gtk.glade

class MainGui:
    def __init__(self):
        self.widgets = gtk.glade.XML("noticias.glade")
        signals = {"search_input_activate" : self.on_search_input_activate,
                   "search_button_clicked" : self.on_search_input_clicked,
                   "gtk_main_quit" : gtk.main_quit}
        
        self.widgets.signal_autoconnect(signals)
        self.search_input = self.widgets.get_widget("search_input")
        self.elMundo = self.widgets.get_widget("elMundo_button")
        self.elPais = self.widgets.get_widget("elPais_button")
        self.ABC = self.widgets.get_widget("ABC_button")

if __name__== "__main__":
    MainGui()
    gtk.main()