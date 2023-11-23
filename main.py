from tkinter import *
import sqlite3

conn = sqlite3.connect("bank.db")
c = conn.cursor()

import bank_object

root = Tk()

root.title("SIGN IN")
#new_user = Button()
#old_user = 

root.mainloop()