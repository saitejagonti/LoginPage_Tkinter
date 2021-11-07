import tkinter
from tkinter import *
from tkinter import messagebox

def ok():
    username = e1.get()
    password = e2.get()

    if(username == "" and password == ""):
        messagebox.showinfo("","blank not allowed")

    elif(username == "admin" and password == "1234"):
        messagebox.showinfo("","Login successfully")
        root.destroy()

    else:
        messagebox.showinfo("","Invalid username and password")

def newregi():
    name= e3.get()
    password = e4.get()
    reenterpassword= e5.get()

    if (name != "" and password==reenterpassword):
        messagebox.showinfo("","Register successfully")
        root.destroy()

    elif (name == "" and password == "" and reenterpassword == ""):
        messagebox.showinfo("", "blank not allowed")

    elif (name != "" and password!=reenterpassword):
        messagebox.showinfo("","Password not matched")

    else:
        messagebox.showinfo("","Invalid Information")

root = Tk()
root.title("Login")
root.geometry("300x400")
global e1
global e2
global e3
global e4
global e5


Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
Label(root, text="Name").place(x=10, y=197)
Label(root, text="Password").place(x=10, y=220)
Label(root, text="Re-Enter Password").place(x=10, y=243)
Label(root, text="sign in").place(x=10, y=165)


e1 = Entry(root)
e1.place(x=100, y=10)

e2 = Entry(root)
e2.place(x=100, y=40)
e2.config(show = '*')

e3 = Entry(root)
e3.place(x=115, y=200)

e4 = Entry(root)
e4.place(x=115, y=220)
e4.config(show = '*')

e5 = Entry(root)
e5.place(x=115, y=240)
e5.config(show = '*')

Button(root, text="Login", command=ok, height = 1, width = 8, bg="blue", fg="white").place(x=10, y=80)
Button(root, text="Register", command=newregi, bg="red", fg="white").place(x=100,y=280)

root.mainloop()
