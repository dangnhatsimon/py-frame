# Import libraries
import os
import pandas as pd
from tkinter import *
import re
import openpyxl


def searching(folder_excel: str, keywords: str):
    for file in os.listdir(folder_excel):
        file_name = os.path.splitext(file)[0]
        file_ext = os.path.splitext(file)[1]
        if file_ext in ['.xlsx', '.xlsm', '.xlsb', '.xltx', '.xltm', 'xls', '.xml', '.xlam', '.xla', '.xlw', '.xlr']:
            
    
def word_search(excel_file: str, keywords: str):
    df = pd.read_excel(excel_file, header=True)
    count_word = 0
    for cell in df.iterrows():
        if re.search(keywords,cell):
            count_word += 1


def searching_label(root):
    myLabel = Label(root)
    myLabel.pack()


def main():
    # Create instance
    root = Tk()
    root.title('Simple Searching Tool')

    e = Entry(root, width=50, bg='white', fg='black', borderwidth=5, relief=SUNKEN)
    e.grid(row=0, column=0, padx=10, pady=10)
    e.insert(0, 'Enter your folder path: ')

    folder_but = Button(root, text='Browse', state=DISABLED,
                        padx=10, pady=10, fg='blue', bg='#ffffff')
    folder_but.grid(row=0, column=1, padx=10, pady=10)
    exit_button = Button(root, text='Browse', command=root.quit)
    keyword_but = Button(root, text='Search')
    keyword_but.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
