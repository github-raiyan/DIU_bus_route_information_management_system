#!/usr/bin/python3.6
from tkinter import *
import time
import db
import openPhoto
path=openPhoto.path
class map(Tk):
    def __init__(self,list):
        super().__init__()
        self.geometry("800x800")
        self.resizable(0,0)
        self.configure(bg="white")

        self.title("show bus route")
        self.list=list
        self.mp = PhotoImage(master=self, file=f"{path}map.png", width=800, height=800)
        self.point = PhotoImage(master=self, file=f"{path}point.png", width=20, height=30)
        Label(self,image=self.mp).place(x=0,y=0)

        #Button(self,text="Close",command=self.quit).place(x=855,y=60)
        self.run()


    def run(self):
        self.update()
        time.sleep(1)
        for i in range (0,len(self.list)):
            point=db.locationPoint(self.list[i])
            #print(point)
            if(point==None):
                continue
            l=Label(self,image=self.point)
            l.place(x=point[0]-10,y=point[1]-30)
            l=Label(self,text=f"Stoppage {i+1}:\n{self.list[i]}",bg="white")
            l.place(x=point[0]-30,y=point[1]-68)
            l.update()
            time.sleep(1)
