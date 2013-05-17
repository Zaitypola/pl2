# -*- coding: iso-8859-15 -*-

from Tkinter import *

class newsGUI(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def search(self):
        print self.var_ABC.get()
        
        
    def initUI(self):
        categories = [
                ("Latest news", 0),
                ("Sports", 1),
                ("National", 2),
                ("International", 3),
            ]      
        self.parent.title("News feeds searcher")

        self.pack(fill=BOTH, expand=1)
      
        self.var_elMundo = IntVar()
        self.var_elPais = IntVar()
        self.var_ABC = IntVar()
        self.var_Category = IntVar()

        self.var_Category.set(0)
        
        Label(self, text="Categories").pack(anchor=W)
        for category,value in categories:
            Radiobutton(self, text=category,variable=self.var_Category, value=value).pack(anchor=W)
        
        Label(self, text="Source").place(x=150,y=0)
        Checkbutton(self, text="El Mundo",variable=self.var_elMundo).place(x=150,y=15)
        Checkbutton(self, text="El País",variable=self.var_elPais).place(x=150,y=30)
        Checkbutton(self, text="ABC",variable=self.var_ABC).place(x=150,y=45)
       
        Entry(self).place(x=0,y=120)
        Button(self, text="Search").place(x=130,y=120)
        Text(self, height=26, width=70).place(x=0,y=150)
            
def main():
    root = Tk()
    root.geometry("320x240")
    app = newsGUI(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
 