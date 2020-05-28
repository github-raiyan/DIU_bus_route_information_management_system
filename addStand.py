#!/usr/bin/python3.6
from tkinter import *
import openPhoto
import db
path=openPhoto.path
class addStand(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("980x800")
        self.resizable(0,0)
        self.configure(bg="white")
        self.title("Add a bus stand")

        # self.mp=openPhoto.openPhoto(f"{path}map.png",800,800)
        self.mp = PhotoImage(master=self, file=f"{path}map.png", width=800, height=800)
        # self.point=openPhoto.openPhoto(f"{path}point.png",20,30)
        self.point = PhotoImage(master=self, file=f"{path}point.png", width=20, height=30)
        self.image= PhotoImage(master=self, file=f"{path}sky.png", width=800, height=800)
        Label(self,image=self.image).place(x=600,y=0)
        self.label=Label(self,image=self.mp,cursor="cross")
        #self.label=Label(self,bg="orange",width=800,height=800)
        self.label.place(x=0,y=0)



        self.var=Entry(self,bg="white")
        self.var.place(x=820,y=50)
        Label(self,text="Bus stand name:",bg="white",font="Arial 10 bold").place(x=820,y=28)
        Button(self,text="Done",font="Arial 12 bold",bg="#56beff",activebackground="#56beff",command=self.done).place(x=860,y=100)

        self.label.bind('<Button-1>',self.click)

        self.labelPoint=Label(self,image=self.point)

    def click(self,event):
        self.labelPoint.destroy()
        self.x=event.x
        self.y=event.y
        #print(f"Bus name {self.var.get()}  {self.x}  {self.y}")
        self.labelPoint = Label(self,image=self.point)
        self.labelPoint.place(x=self.x-10,y=self.y-30)


    def done(self):
        db.insert_into_bus_stand(self.var.get(),self.x,self.y)
        self.destroy()
