#!/usr/bin/python3.6
from tkinter import *
import webbrowser
import openPhoto
path= openPhoto.path
class about(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("550x362")
        self.configure(bg="white")
        self.title("About")
        self.resizable(0,0)
        #self.me = openPhoto.openPhoto(f"{path}raiyan.png",70,80)
        self.me=PhotoImage(master=self, file=f"{path}raiyan.png", width=70, height=80)
        #self.sir=openPhoto.openPhoto(f"{path}hasanuzzaman.png",75,90)
        self.sir=PhotoImage(master=self, file=f"{path}hasanuzzaman.png", width=75, height=90)
        Frame(self,bd=0,bg="#55B68B",width=550,height=330).place(x=0,y=0)
        Label(self,image=self.me,bg="#55B68B").place(x=20,y=40)
        Label(self,image=self.sir,bg="#55B68B").place(x=450,y=200)
        Label(self,text="This software is developed by",bg="#55B68B",fg="white",font="Arial 10 bold").place(x=180,y=8)
        Label(self,
              text="Md Raiyan Hossain\nDepartment of Computer Science and Engineering\nDaffodil International University",
              bg="#55B68B", fg="white", font="Arial 10 italic").place(x=120, y=50)
        Label(self, text="Submitted to,", bg="#55B68B", fg="white", font="Purisa 9 bold").place(x=225, y=130)
        Label(self,
              text="Dr. Md. Hasanuzzaman\nProfessor\nDepartment of Computer Science and Engineering\nUniversity of Dhaka, Bangladesh\nMar 2013 - Present",
              bg="#55B68B", fg="white", font="Arial 10 italic").place(x=120, y=200)


        #self.git=openPhoto.openPhoto(f"{path}git.png",30,30)
        self.git=PhotoImage(master=self,file=f"{path}git.png",width=30,height=30)
        #self.link=openPhoto.openPhoto(f"{path}link.png",25,25)
        self.link = PhotoImage(master=self, file=f"{path}link.png", width=25, height=25)
        #self.face=openPhoto.openPhoto(f"{path}facebook.png",25,25)
        self.face = PhotoImage(master=self, file=f"{path}facebook.png", width=25, height=25)

        l1=Label(self,image=self.git,bg="white")
        l1.place(x=20,y=330)
        l2=Label(self,image=self.link,bg="white")
        l2.place(x=60,y=333)
        l3=Label(self,image=self.face,bg="white")
        l3.place(x=100,y=333)

        l1.bind('<Button-1>',self.github)
        l2.bind('<Button-1>',self.linkedin)
        l3.bind('<Button-1>',self.facebook)

    def github(self,event):
        webbrowser.open("https://github.com/github-raiyan/DIU_bus_route_information_management_system",new=2)

    def linkedin(self,event):
        webbrowser.open("https://www.linkedin.com/in/raiyan-hossain-330924174/",new=2)
    def facebook(self,event):
        webbrowser.open("https://www.facebook.com/rayhan724",new=2)

