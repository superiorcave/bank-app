from tkinter import *
import sqlite3

conn = sqlite3.connect("bank.db")
c = conn.cursor()

import bank_object
UserBankObject = bank_object.bank(0,0,0,0,0)

root = Tk()
signin = Frame(root, width=50, height=150)
login = Frame(root, width=50, height=150)
homepage = Frame(root, width=50, height=150)
signin.grid(row=0,column=0)

def loadLogin():
    signin.grid_forget()
    login.grid(row=0, column=0)
def LoginSucessful():
    login.grid_forget()
    homepage.grid(row=0,column=0)
def withdraw():
    money = int(amountEntry.get())
    UserBankObject.balance = UserBankObject.balance - money
    c.execute(f"UPDATE bank_info SET balance = {UserBankObject.balance} WHERE username = '{UserBankObject.username}'")
    conn.commit()

def deposit():
    money = int(amountEntry.get())
    UserBankObject.balance = UserBankObject.balance + money
    balanceDisplay.config(text=f"balance: {UserBankObject.balance}")

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
    c.execute(f"SELECT * FROM bank_info WHERE username = '{user}' AND password = '{pas}'")
    row = c.fetchone()
    print(row)
    global UserBankObject 
    UserBankObject.accountnum = row[0]
    UserBankObject.username = row[1]
    UserBankObject.name = row[2]
    UserBankObject.password = row[3]
    UserBankObject.balance = row[4]
    nameDisplay.config(text=f"Hello {UserBankObject.name}                    ")
    balanceDisplay.config(text=f"balance: {UserBankObject.balance}")
    LoginSucessful()

enterButton = Button(login, text='SUBMIT', font=('Arial', 20, 'bold'), command=enterButtonClicked)

usernameEntry.grid(row=0, column=0)
passwordEntry.grid(row=1, column=0)
enterButton.grid(row=2, column=0)



nameDisplay = Label(homepage, text=f"Hello {UserBankObject.name}", font=('Arial', 18, 'bold'))
balanceDisplay = Label(homepage, text=f"Balance: {UserBankObject.balance}", font=('Arial', 18, 'bold'))
depositButton = Button(homepage, text="Deposit", command= deposit)
withdrawButton = Button(homepage, text="Withdraw", command= withdraw)
amountEntry = Entry(homepage)
amountEntry.insert(0, "Enter amount here")

nameDisplay.grid(row=0, column=0)
balanceDisplay.grid(row=0, column=1)
amountEntry.grid(row=1, column=0)
withdrawButton.grid(row=2, column=0)
depositButton.grid(row=2, column=1)


root.mainloop()