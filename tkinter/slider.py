from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Simple Search")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')

vertical = Scale(root, from_=0, to=200)
vertical.pack()


root.mainloop()