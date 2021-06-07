from tkinter import* #for GUI applications
from tkinter import ttk  #it has some styling toolkits
from PIL import Image,ImageTk  #for insert images properly=> pillow
from tkinter import messagebox
import mysql.connector
import cv2 #open source computer vision libraries contains more than 2500 machine learning algorithms
import os
import numpy as np


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1495x700+0+0")
        self.root.title("Face Recogintion System ")

        titleLabel=Label(self.root, text="DEVELOPER", font=("sans-serif", 30,"bold"),bg="white", fg="purple")
        titleLabel.place(x=0,y=0,width=1400,height=30)

        imgTop=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\dev2.jpg") 
        imgTop=imgTop.resize((1405,700), Image.ANTIALIAS) #convert high level image to low image
        self.photoimgTop=ImageTk.PhotoImage(imgTop)

        firstLabel=Label(self.root,image=self.photoimgTop) #to set image on window
        firstLabel.place(x=0,y=35,width=1405,height=700)

         #main frame
        mainFrame=Frame(firstLabel,bd=2,bg="white")
        mainFrame.place(x=800,y=0,width=650, height=650)

        imgBottom=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\dev.jpg") 
        imgBottom=imgBottom.resize((330,200), Image.ANTIALIAS) #convert high level image to low image
        self.photoimgBottom=ImageTk.PhotoImage(imgBottom)

        firstLabel=Label(mainFrame,image=self.photoimgBottom) #to set image on window
        firstLabel.place(x=300,y=0,width=330,height=200)

        # Developer info
        titleLabel=Label (mainFrame,text="Hello, Our Project Topic is \n Automated Attendance System  \n And Personality developement using \n Face Recogintion", font=("sans-serif", 13,"bold"),bg="white", fg="black")
        titleLabel.place(x=0,y=5)

        titleLabel=Label (mainFrame,text="No of members:4", font=("sans-serif", 13,"bold"),bg="white", fg="black")
        titleLabel.place(x=75,y=115)

        imgTop2=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\att.jpg") 
        imgTop2=imgTop2.resize((600,300), Image.ANTIALIAS) #convert high level image to low image
        self.photoimgTop2=ImageTk.PhotoImage(imgTop2)

        firstLabel=Label(mainFrame,image=self.photoimgTop2) #to set image on window
        firstLabel.place(x=0,y=205,width=600,height=300)    

        titleLabel=Label (mainFrame,text="Group Members are:", font=("sans-serif", 13,"bold"),bg="white", fg="black")
        titleLabel.place(x=0,y=510)

        titleLabel=Label (mainFrame,text="1]Amruta Khamkar\n2]Pranav Jangam\n3]Nishant Ghangale\n4]Prashant Khadye", font=("sans-serif", 13,"bold"),bg="white", fg="black")
        titleLabel.place(x=0,y=535)



if __name__ == "__main__":
        root=Tk()  #call root with toolkit
        obj=Developer(root)  #make object of class and give the class name and pass root because we want to connect them
        root.mainloop() #close the main loop