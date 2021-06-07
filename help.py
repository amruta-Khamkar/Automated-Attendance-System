from tkinter import* #for GUI applications
from tkinter import ttk  #it has some styling toolkits
from PIL import Image,ImageTk  #for insert images properly=> pillow
from tkinter import messagebox
import mysql.connector
import cv2 #open source computer vision libraries contains more than 2500 machine learning algorithms
import os
import numpy as np


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1495x700+0+0")
        self.root.title("Face Recogintion System ")

        titleLabel=Label(self.root, text="HELP DESK", font=("sans-serif", 30,"bold"),bg="white", fg="purple")
        titleLabel.place(x=0,y=0,width=1400,height=30)

        imgTop=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\portfolio.jpg") 
        imgTop=imgTop.resize((1405,700), Image.ANTIALIAS) #convert high level image to low image
        self.photoimgTop=ImageTk.PhotoImage(imgTop)

        firstLabel=Label(self.root,image=self.photoimgTop) #to set image on window
        firstLabel.place(x=0,y=35,width=1405,height=700)

        helpLabel=Label (firstLabel,text="Email:amrutakhamkar15@gmail.com", font=("times new roman", 20,"bold"),bg="white", fg="black")
        helpLabel.place(x=500,y=300)

if __name__ == "__main__":
        root=Tk()  #call root with toolkit
        obj=Help(root)  #make object of class and give the class name and pass root because we want to connect them
        root.mainloop() #close the main loop