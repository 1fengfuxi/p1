from tkinter import *

userName = "john"
password = "cleese"
loggedIn = False


def updatelogstat():
    print(loggedIn)
    if loggedIn == False:
        btnLogOut.grid_remove()
        return "Not logged in"
    else:
        btnLogOut.grid()
        return "Logged in as "


root = Tk()

label1 = Label(root, text="Not logged in", fg="white", bg="black")
label1.grid(row=0, sticky=W)
label2 = Label(root, text="Press the button to log in.")
label2.grid(row=1, sticky=W)
un = StringVar()
pw = StringVar()


def login():
    top.deiconify()  # same as VB form.show


def logout():
    global loggedIn
    loggedIn = False
    label1.configure(text=updatelogstat())


def goback():
    global loggedIn
    possName = un.get()
    possPass = pw.get()
    if possName == userName and possPass == password:
        loggedIn = True
        label1.configure(text=updatelogstat() + possName)
    top.destroy()


# login objects:
top = Toplevel(root)
top.title("Log in dialogue...")
lbl1 = Label(top, text="User name:").grid(row=0, sticky=W)
e1 = Entry(top, textvariable=un,  show="*").grid(row=0, column=2, sticky=W)
lbl2 = Label(top, text="Password:").grid(row=1, sticky=W)
e2 = Entry(top, textvariable=pw, show="*").grid(row=1, column=2, sticky=W)
Bexit = Button(top, text="Log in", command=goback).grid(row=3, sticky=W)
un.set("john")
pw.set("cleese")
top.withdraw()  # same as VB form.hide
################################
button1 = Button(root, text="Log in", command=login)

button1.grid(row=2, column=2)
btnLogOut = Button(root, text="Log out", command=logout)

btnLogOut.grid(row=3, column=2)

root.mainloop()
