from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Simple Search")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=1080)
vertical.pack()

horizontal = Scale(root, from_=0, to=1080, orient=HORIZONTAL)
horizontal.pack()


def slide():
    my_label = Label(root, text=str(horizontal.get()) +
                     "x" + str(vertical.get()))
    my_label.pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()
