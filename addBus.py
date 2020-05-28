#!/usr/bin/python3.6
from tkinter import *
import db
import openPhoto
path=openPhoto.path
class addBus(Tk):
    def __init__(self,frame,listbuses):
        super().__init__()
        self.f=frame
        self.listbuses=listbuses
        self.geometry("700x400")
        self.configure(bg="white")
        self.title("Add a bus")

        self.image= PhotoImage(master=self, file=f"{path}blue.png", width=1000, height=800)
        Label(self,image=self.image).place(x=0,y=0)


        Label(self,text="Bus name:",bg="white").place(x=18,y=20)
        Label(self,text="Time:",bg="white").place(x=45,y=50)
        Label(self,text="Info:",bg="white").place(x=53,y=80)


        self.name=Entry(self)
        self.name.place(x=100,y=20)
        self.time=Entry(self)
        self.time.place(x=100, y=50)
        self.infoBox=Text(self,width=18,height=10)
        self.infoBox.place(x=100,y=80)
        self.listStands()
        self.listRoute()

    def listStands(self):
        f=Frame(self,width=150,height=250,bg="#29AFEC")
        f.place(x=500,y=30)
        Label(f,text="List of bus stands",bg="lightgreen",padx=10,pady=10,font="Arial 11 bold").pack(side=TOP)

        self.lst=Listbox(f,selectmode=SINGLE,selectbackground="orange")
        self.lst.pack()

        Button(f,text="Add",bg="#FF9900",activebackground="#FF9900",command=self.add).pack(side=LEFT,padx=8,pady=10)
        Button(f,text="Done",bg="lightgreen",activebackground="lightgreen",command=self.done).pack(side=RIGHT,padx=8,pady=10)
        self.route=[]

        db.cursor.execute("SELECT bus_stand_name FROM bus_stand ORDER BY bus_stand_name")
        result=db.cursor.fetchall()
        for row in result:
            self.lst.insert(END,f"{row[0]}")

    def listRoute(self):
        f=Frame(self,width=150,height=250,bg="lightgreen")
        f.place(x=310,y=30)
        Label(f, text="Route:", font="Arial 12 bold", bg="lightgreen",padx=20,pady=5).pack()
        self.lstRoute=Listbox(f,selectbackground="skyblue")
        self.lstRoute.pack()

    def add(self):
        try:
            stand=self.lst.get(self.lst.curselection()[0])
        except:
            return

        self.route.append(stand)
        self.lstRoute.insert(END,stand)
        self.lstRoute.activate(END)

    def done(self):
        s=f"{self.route[0]}"
        for i in range(1,len(self.route)):
            s+=f",{self.route[i]}"
        db.insert_into_bus(self.name.get(),s,self.time.get(),self.infoBox.get("1.0",END))

        for widget in self.f.winfo_children():
            widget.destroy()
        self.listbuses("admin")
        self.destroy()
