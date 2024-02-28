from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Matplotlib")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')
root.geometry("400x400")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, bins = 50)
    plt.show()

my_button = Button(root, text="Graph", command=graph)
my_button.pack()
root.mainloop()