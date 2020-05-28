#!/usr/bin/python3.6
from tkinter import *
from threading import Thread
import common
import addBus
import addStand
import time
class admin(common.common):
    def __init__(self):
        super().__init__()
        self.title("Admin")

        self.listBuses("admin")
        self.b1=Button(self,text="Post notice",command=self.text_box,bd=0,bg="#8BC34A",activebackground="#8BC34A")
        self.b1.place(x=780,y=340)
        self.logoutButton.place(x=870, y=13)
        Label(self, text="Notice board", bg="#E19494", bd=2, height=2, width=21, font="Arial 10 bold").place(x=745, y=130)
        self.mssg()


        thread=Thread(target=self.wther,args=(740,400,))
        thread.start()
        #self.wther(740,400)
        Button(self,text="Add a bus",command=self.addBus,bd=0,bg="lightgreen",activebackground="lightgreen").place(x=150,y=520)
        Button(self,text="Add a bus stand",command=self.addStand,bd=0,bg="lightgreen",activebackground="lightgreen").place(x=250,y=520)

    def text_box(self):
        self.m.destroy()
        self.b1.destroy()

        self.box=Text(self,width=18,height=10,bg="#F9C48C")
        self.box.place(x=745,y=170)

        self.b1 = Button(self, text="Post", command=self.save_notice,bd=0,bg="#8BC34A",activebackground="#8BC34A")
        self.b1.place(x=800, y=340)


    def save_notice(self):
        self.b1.destroy()
        self.b1 = Button(self, text="Post notice", command=self.text_box,bd=0,bg="#8BC34A",activebackground="#8BC34A")
        self.b1.place(x=780, y=340)

        f = open("notice.txt", "w")
        f.write(self.box.get("1.0",END))
        f.write(f"\nPublished on:\n{time.ctime()}")
        f.close()
        self.mssg()


    def addBus(self):
        self.window=addBus.addBus(self.scr.frame,self.listBuses)
        print("add bus")
        self.window.mainloop()


    def addStand(self):
        window=addStand.addStand()
        window.mainloop()


    def mssg(self):
        self.var=StringVar()
        f=open("notice.txt","r")
        self.var.set(f.read())
        f.close()
        Label(self, bg="#F9C48C", width=21, height=10).place(x=745, y=170)
        self.m=Message(self,text=self.var.get(),width=135,bg="#F9C48C")
        self.m.place(x=745,y=170)
