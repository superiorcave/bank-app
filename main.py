from tkinter import *
import sqlite3

conn = sqlite3.connect("bank.db")
c = conn.cursor()

import bank_object

root = Tk()
signin = Frame(root, width=50, height=150)
login = Frame(root, width=50, height=150)
signin.grid(row=0,column=0)

def loadLogin():
    signin.forget()
    login.grid(row=0, column=0)

root.title("SIGN IN")
new_user = Button(signin, text="New User", font=("Arial", 20, "bold"))
old_user = Button(signin, text="Existing User", font=("Arial", 20, "bold"), command=loadLogin)

new_user.grid(row=2, column=2)
old_user.grid(row=4, column=2)



usernameEntry = Entry(login)
passwordEntry = Entry(login)
usernameEntry.insert(0, 'Enter username here')
passwordEntry.insert(0, 'Enter password here')
def enterButtonClicked():
    user = usernameEntry.get()
    pas = passwordEntry.get()
    c.execute(f"SELECT * FROM bank_info WHERE username = {user} AND password = {pas}")
    for row in c:
        print(row[0])

enterButton = Button(login, text='SUBMIT', font=('Arial', 20, 'bold'), command=enterButtonClicked)

usernameEntry.grid(row=0, column=0)
passwordEntry.grid(row=1, column=0)
enterButton.grid(row=2, column=0)


root.mainloop()