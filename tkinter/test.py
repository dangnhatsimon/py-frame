import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):

  def __init__(self):
      super().__init__()

      self.title("TITLE")

      self.submit = ttk.Button(self, text = 'SUBMIT', command = self.click_submit_button)
      self.submit.grid(row = 0, column = 2, padx = 20, pady = 20)

class submit_button(Window):

  def __init__(self):
      super().__init__()
      self.submit_pop_up = tk.Toplevel(self)
      self.submit_pop_up.withdraw()
      print(self.submit_pop_up)

  def click_submit_button(self):
      self.submit_pop_up.deiconify()
      print('New PopUp')

if __name__ == "__main__":
    app = submit_button()
    app.mainloop()