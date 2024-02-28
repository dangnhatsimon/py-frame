from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Simple Search")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')
root.geometry("400x400")

# var = IntVar()
var = StringVar()

def show():
    myLabel = Label(root, text= var.get()).pack()
    
c = Checkbutton(root, text= "Check this box, I dare you", variable= var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()



myButton = Button(root, text= "Show Selection", command=show).pack()


root.mainloop()