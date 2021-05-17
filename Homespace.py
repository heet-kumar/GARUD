from tkinter import *
import sys
import os

root = Tk()
root.geometry("440x150")

Label(root,
text="Welcome To HomeSpace",
font="arial 15 bold",
anchor="center").grid(row=1,column=2,pady=10)

Button(text="Setup Folder",bg="#83c5be",command=lambda: os.system('python newrepo.py')).grid(row=2,column=1,pady=20,padx=10,sticky=E)
Button(text="Start Backup",bg="#83c5be",command=lambda: os.system('python filepath.py')).grid(row=2,column=2,pady=20)
Button(text="Set New User",bg="#83c5be",command=lambda: os.system('python setuser.py')).grid(row=2,column=3,pady=20,padx=10)

root.mainloop()