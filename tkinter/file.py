from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Simple Search")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir='D:/Python/Tkinter/', title='Select a file', 
        filetypes=(('png files', '*.png'), ('all files', '*.*')))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_button = Button(root, text='Open File', command=open).pack()

root.mainloop()
