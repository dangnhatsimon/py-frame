from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Simple Search")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')

frame = LabelFrame(root, text='This is my frame...', padx=50, pady=50)
frame.pack(padx=10, pady=10)

b1 = Button(frame, text='Search')
b2 = Button(frame, text='Find')
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()