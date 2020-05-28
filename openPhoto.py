#!/usr/bin/python3.6
from  tkinter import *
from PIL import Image,ImageTk
import os
path=f"{os.getcwd()}/images/"

def openPhoto(s,w,h):

    img=Image.open(s)
    img = img.resize((w,h), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(img)
    return photo

