from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Simple Search")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')
root.geometry("400x400")


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = [
    "Mon",
    "Tue",
    "Wed",
    "Thurs",
    "Fri",
    "Sat",
    "Sun"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show)

root.mainloop()
