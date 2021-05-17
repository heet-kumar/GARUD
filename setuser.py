from tkinter import *
import subprocess as sub
import sys
import os

root = Tk()
root.geometry("280x200")

def printvalue():
    u=uname.get()
    e=uemail.get()
    p=path.get()
    print("path : "+p)
    print("email: "+e)
    print("name : "+u)
    command=sub.call(["setuser.sh",u,e,p],shell=True)

Label(root,
text="Set New User",
font="arial 15 bold",
anchor="center").grid(row=1,column=2,pady=10)

pathe = Label(root, text="Local Path",font="arial 10 bold").grid(row=2,column=1,padx=10,pady=5)
uname = Label(root, text="Username",font="arial 10 bold").grid(row=3,column=1,padx=10,pady=5)
email = Label(root, text="Email",font="arial 10 bold").grid(row=4,column=1,padx=10,pady=5)

uemail= StringVar()
uname= StringVar()
path= StringVar()

pentry = Entry(root, textvariable = path).grid(row=2,column=2)
uentry = Entry(root, textvariable = uname).grid(row=3,column=2)
eentry = Entry(root, textvariable = uemail).grid(row=4,column=2)

Button(text="Set",
font="arial 10 bold",
bg="#a8dadc",
command=printvalue
).grid(row=5,column=2,pady=20,ipadx=5)

root.mainloop()