#!/usr/bin/python3.6
from tkinter import *
import common
from threading import Thread
class student(common.common):
    def __init__(self):
        super().__init__()
        self.title("Student")
        self.geometry("900x600")
        self.bar.configure(width=87)
        self.scr.canvas.configure(width=598)
        self.logoutButton.place(x=820, y=13)
        Label(self, text="Notice board", bg="#E19494", bd=2, height=2, width=21, font="Arial 10 bold").place(x=698,y=130)
        self.listBuses("student")
        self.mssg()
        thread=Thread(target=self.wther,args=(690,400,))
        #self.wther(680,400)
        thread.start()

    def mssg(self):
        pass
        self.var=StringVar()
        f=open("notice.txt","r")
        self.var.set(f.read())
        f.close()
        Label(self, bg="#F9C48C", width=21, height=10).place(x=698, y=170)
        self.m=Message(self,text=self.var.get(),width=135,bg="#F9C48C")
        self.m.place(x=698,y=170)
