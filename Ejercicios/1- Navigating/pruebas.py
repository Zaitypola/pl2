from Tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, wrap=WORD, yscrollcommand=scrollbar.set)
text.pack()

scrollbar.config(command=text.yview)


root.mainloop()