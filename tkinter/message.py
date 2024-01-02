from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Simple Search")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my popup!", "Hello")
    Label(root, text= response)
    if response == 1:
        Label(root, text='You clicked yes!').pack()
    else:
        Label(root, text='You clicked no!').pack()
Button(root, text='Popup', command=popup).pack()

root.mainloop()