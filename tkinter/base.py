from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Simple Search")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')

def open():
    global my_img
    top = Toplevel()
    top.title("Simple Picture")
    top.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')
    my_img = ImageTk.PhotoImage(Image.open('search.png'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='Close Window', command=top.destroy).pack()

btn = Button(root, text='Open Second Window', command=open)
btn.pack()

root.mainloop()