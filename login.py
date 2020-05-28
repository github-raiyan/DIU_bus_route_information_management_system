#!/usr/bin/python3.6
from tkinter import *
import os
import time
import openPhoto
import db
from threading import Thread
path=openPhoto.path
class Login(Tk):
    userloggedout=False
    user="None"
    def __init__(self):

        super().__init__()

        if ( not os.path.isfile("bus_route")):
            db.create_db()

        self.geometry("900x500")
        self.resizable(0,0)
        self.p=openPhoto.openPhoto(f"{path}background(copy).png",900,500)
        Label(image=self.p).place(x=0,y=0)
        Label(text="DIU bus route information management system",font="Arial 10 italic",anchor="w",width=150,height=1,bg="lightgreen").place(x=0,y=480)
        self.login()

    def frame(self):
        self.pf=openPhoto.openPhoto(f"{path}frame.png",356,392)
        Label(self,image=self.pf).place(x=292,y=51)

    def passCheck(self):
        def print_mssg():
            self.epass.delete(0, END)
            self.wpass = Label(self, text="Wrong userID or password", bg="red", fg="white")
            self.wpass.place(x=590, y=170)
            self.wpass.update()
            time.sleep(4)
            self.wpass.destroy()

        if(self.lAs.get()==0 and self.idtxt.get()=="admin" and self.passtxt.get()=="admin"):
            Login.user="admin"
            self.destroy()
        elif(db.passcheck(self.idtxt.get(),self.passtxt.get())):
            Login.user="student"
            self.destroy()
        else:

            thread=Thread(target=print_mssg)
            thread.start()





    def regisCheck(self):
        def print_mssg():
            self.erpasstxt.delete(0, END)
            self.erconpasstxt.delete(0, END)
            self.wpass = Label(self, text="Passwords are not identical", bg="red", fg="white")
            self.wpass.place(x=590, y=190)
            self.wpass.update()
            time.sleep(4)
            self.wpass.destroy()


        if(self.rpasstxt.get()==self.rconpasstxt.get()):

            if(not db.isIdExists(self.ridtxt.get())):

                gender="Male"
                if(self.gender.get()==1):
                    gender="Female"
                db.insert_into_student(self.ridtxt.get(),self.nametxt.get(),self.emailtxt.get(),self.rpasstxt.get(),gender)
                self.login()

        else:
            thread=Thread(target=print_mssg)
            thread.start()


    def login(self):
        Login.userloggedout=False

        self.title("Log in")
        self.frame()
        Label(self, text="ID:",font="Arial 12 bold",bg="white",fg="orange").place(x=399, y=140)
        Label(self, text="Password:", font="Arial 12 bold", bg="white", fg="orange").place(x=340, y=170)


        self.idtxt = StringVar()
        self.passtxt = StringVar()
        Entry(self,textvariable=self.idtxt,bg="lightblue").place(x=440,y=140)
        self.epass=Entry(self, textvariable=self.passtxt, bg="lightblue",show="*")
        self.epass.place(x=440, y=170)

        self.lAs=IntVar()
        self.lAs.set(1)
        Radiobutton(self,text="As Admin  ",variable=self.lAs,value=0,bg="white",activebackground="lightgreen").place(x=420,y=210)
        Radiobutton(self, text="As Student", variable=self.lAs, value=1, bg="white", activebackground="lightgreen").place(x=420, y=235)



        Button(self, text="Log in", font="Arial 11 ", activebackground="springGreen3", bg="springGreen3", fg="white",
               activeforeground="white", bd=0, command=self.passCheck,padx=16).place(x=350, y=280)
        Button(self, text="Sign up", font="Arial 11 ", activebackground="steelblue3", bg="steelblue3", fg="white",
               activeforeground="white", bd=0, command=self.signUP).place(x=505, y=280)




    def signUP(self):
        self.frame()
        self.title("Sign up")

        Label(self, text="Name:", font="Arial 12 bold", bg="white", fg="orange").place(x=350, y=100)
        Label(self, text="ID:", font="Arial 12 bold", bg="white", fg="orange").place(x=376, y=130)
        Label(self, text="Email:", font="Arial 12 bold", bg="white", fg="orange").place(x=350, y=160)

        self.nametxt=StringVar()
        self.ridtxt=StringVar()
        self.emailtxt=StringVar()
        Entry(self, textvariable=self.nametxt, bg="lightblue").place(x=430, y=100)
        Entry(self, textvariable=self.ridtxt, bg="lightblue").place(x=430, y=130)
        Entry(self, textvariable=self.emailtxt, bg="lightblue").place(x=430, y=160)

        self.rpasstxt=StringVar()
        self.rconpasstxt=StringVar()
        Label(self, text="Password:", font="Arial 10 bold", bg="white", fg="orange").place(x=333, y=190)
        Label(self, text="Confirm Password:", font="Arial 10 bold", bg="white", fg="orange").place(x=295, y=220)
        self.erpasstxt=Entry(self, textvariable=self.rpasstxt, bg="lightblue",show="*")
        self.erpasstxt.place(x=430, y=190)
        self.erconpasstxt=Entry(self, textvariable=self.rconpasstxt, bg="lightblue", show="*")
        self.erconpasstxt.place(x=430, y=220)

        self.gender=IntVar()
        self.gender.set(0)
        Radiobutton(self, text="Male   ", variable=self.gender, value=0, bg="white", activebackground="lightgreen").place(x=370, y=260)
        Radiobutton(self, text="Female  ", variable=self.gender, value=1, bg="white", activebackground="lightgreen").place(x=450, y=260)


        Button(self, text="Sign up",font="Arial 11 ", activebackground="steelblue3", bg="steelblue3",fg="white",activeforeground="white", bd=0, command=self.regisCheck).place(x=345,y=300)
        Button(self,text="Cancle",font="Arial 11 ", activebackground="tomato", bg="tomato",fg="white",activeforeground="white", bd=0, command=self.login).place(x=490, y=300)
