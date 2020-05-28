#!/usr/bin/python3.6
import login
import admin
import student
from tkinter import *

def loginWindow():
    root=login.Login()
    root.update()
    root.mainloop()
    if(login.Login.user=="admin"):

        window=admin.admin()
        window.update()
        window.mainloop()
    elif(login.Login.user=="student"):
        window=student.student()
        window.update()
        window.mainloop()

    login.Login.user="None"
    
    if(login.Login.userloggedout):
        loginWindow()

if __name__ == '__main__':

   loginWindow()
