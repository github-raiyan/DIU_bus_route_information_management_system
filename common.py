#!/usr/bin/python3.6
from tkinter import *
from functools import partial
from threading import Thread
import tkinter.messagebox
import time
import openPhoto
import login
import weather
import db
import map
import about
path=openPhoto.path
class common(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("950x600")
        self.resizable(0, 0)
        self.configure(bg="white")
        self.bg=openPhoto.openPhoto(f"{path}sea.jpg",950,600)
        Label(self,image=self.bg).place(x=0,y=0)
        menubar=Menu(self,activebackground="lightgreen",bg="white")
        about=Menu(menubar,tearoff=0,bg="white",activebackground="lightgreen")

        about.add_command(label="About",command=self.about,)
        about.add_command(label="Exit",command=exit)
        menubar.add_cascade(label="About",menu=about)

        self.config(menu=menubar)

        Label(bg="#00AEEF",width=900,height=3).place(x=0,y=0)
        self.diulogo=openPhoto.openPhoto(f"{path}diulogo.png",110,50)
        Label(self,image=self.diulogo,bg="#00AEEF").place(x=0,y=0)
        self.logoutButton=Button(self,text="Log out",bg="#FF5722",activebackground="#FF5722",command=self.logout)

        self.bar=Label(self,bg="#FF825C",width=97,height=2)
        self.bar.place(x=10,y=108)
        self.infopic=openPhoto.openPhoto(f"{path}info.png",10,10)

        Label(self,text="No",fg="white",bg="#FF825C",font= "Arial 10 bold").place(x=16,y=112)
        Label(self, text="Bus name", fg="white", bg="#FF825C", font="Arial 10 bold").place(x=60, y=112)
        Label(self, text="Time", fg="white", bg="#FF825C", font="Arial 10 bold").place(x=200, y=112)
        Label(self, text="Route", fg="white", bg="#FF825C", font="Arial 10 bold").place(x=350, y=112)
        Label(self, text="Map", fg="white", bg="#FF825C", font="Arial 10 bold").place(x=550, y=112)

        self.scr=scrollbar(self,10,140,670,350)


    def logout(self):
        login.Login.userloggedout=True
        self.destroy()

    def wther(self,x,y):
        time.sleep(1)
        self.wthrpic=openPhoto.openPhoto(f"{path}offline.png",150,150)
        weather_frame=Frame(self,bg="white",width=160,height=160)
        weather_frame.place(x=x,y=y)
        if(weather.get_update()):
            self.wthrpic=openPhoto.openPhoto(f"{path}{weather.icon}.png",80,80)
            Label(weather_frame, image=self.wthrpic, bg="white").place(x=85, y=0)
            Label(weather_frame,text=f"{weather.temp - 273.15}°C\n", bg="white",font="Arial 18 bold").place(x=10, y=25)
            Label(weather_frame,text=f"\nStatus: {weather.main}\nCity: Dhaka\n"
                            f"Humidity: {weather.humidity}%\n",bg="white",font="Arial 10 italic").place(x=30,y=75)
        else:
            Label(weather_frame,image=self.wthrpic,bg="white").place(x=0,y=0)

    def listBuses(self,user):
        self.user=user
        db.cursor.execute("select rowid, bus_name, time, route, info from bus")
        result=db.cursor.fetchall()
        i=0
        for row in result:
            i+=1
            f=Frame(self.scr.frame,bg="white",width=590,height=40)
            f.pack(side=TOP,pady=3,padx=6)
            if(self.user=="admin"):
                f.configure(width=658)

            f.pack_propagate(0)
            Label(f,text=f"{i}",bg="white",font="Arial 10").place(x=8,y=10)
            Label(f, text=f"{row[1]}", bg="white", font="Arial 11").place(x=40,y=10)
            Label(f, text=f"{row[2]}", bg="white", font="Arial 11").place(x=170,y=10)

            lst=row[3].split(',')

            Label(f, text=f"{lst[0]} to {lst[len(lst)-1]}", bg="white", font="Arial 8").place(x=260,y=10)

            thread=Thread(target=self.showInfo,args=(row[4],))
            infoLabel=Button(f,image=self.infopic,bd=0,bg="white",activebackground="white",command=thread.start)
            infoLabel.place(x=495,y=13)


            Button(f,text="See map", bg="#A2D3FB",activebackground="#59B0F8",bd=0,font="Arial 8", command=partial(self.seeMap,lst)).place(x=517,y=8)
            if( self.user=="admin"):

                Button(f, text="Delete", bg="#FCC9C5", activebackground="#F7564B", bd=0, font="Arial 8",command=partial(self.delete,row[1],row[2])).place(x=593,y=8)

        self.scr.put()

    def seeMap(self, lst):
        root=map.map(lst)
        root.mainloop()
        root.mainloop()

    def delete(self,bus_name,time):
        if(tkinter.messagebox.askyesno("Delete Bus","Are you sure?")):
            db.cursor.execute(f"delete from bus where bus_name = '{bus_name}' and time = '{time}'")
            db.db.commit()
            for widget in self.scr.frame.winfo_children():
                widget.destroy()
            self.listBuses("admin")

    def showInfo(self,str):
        infoLabel=Label(self,text=str,bg="#FFEB3B")
        if(self.user=="admin"):
            infoLabel.place(x=700,y=190)
        else:
            infoLabel.place(x=630, y=190)
        infoLabel.update()
        time.sleep(6)
        infoLabel.destroy()


    def about(self):
        root=about.about()
        root.mainloop()

class scrollbar():
    def __init__(self,parent,x,y,width,height):
        self.f=Frame(parent,bg="white")
        self.f.place(x=x,y=y)

        self.canvas=Canvas(self.f,width=width,height=height,bg="#C9EDF0")
        self.scr=Scrollbar(self.f,orient="vertical",command=self.canvas.yview,bg="white",activebackground="#A2D392",troughcolor="white")
        self.frame=Frame(self.canvas,bg="#C9EDF0")

    def put(self):
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'),yscrollcommand=self.scr.set)
        self.canvas.pack(side='left')
        self.scr.pack(side=RIGHT, fill=Y)
