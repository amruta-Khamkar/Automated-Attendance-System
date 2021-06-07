from tkinter import* #for GUI applications
from tkinter import ttk  #it has some styling toolkits
from PIL import Image,ImageTk  #for insert images properly=> pillow
import tkinter
from student import Student
import os
from train import Train
from faceRecoginizer import faceRecoginizer
from attendance import Attendance
from Developer import Developer
from help import Help
from time import strftime
from datetime import datetime

class faceRecognitionSystem:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1495x700+0+0")
            self.root.title("Face Recogintion System ")

            # first image
            img=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\face1.jpg") 
            img=img.resize((490,130), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg=ImageTk.PhotoImage(img)

            firstLabel=Label(self.root,image=self.photoImg) #to set image on window
            firstLabel.place(x=0,y=0,width=490,height=130)

            # second image
            img1=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\faceDetection.jpg") 
            img1=img1.resize((490,130), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg1=ImageTk.PhotoImage(img1)

            firstLabel=Label(self.root,image=self.photoImg1) #to set image on window
            firstLabel.place(x=490,y=0,width=490,height=130)

            # third image
            img2=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\face2.jpg") 
            img2=img2.resize((490,130), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg2=ImageTk.PhotoImage(img2)

            firstLabel=Label(self.root,image=self.photoImg2) #to set image on window
            firstLabel.place(x=980,y=0,width=490,height=130)

            exitButton=Button(self.root,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman", 18,"bold"),bg="black", fg="white")
            exitButton.place(x=1280,y=2, width=80, height=30)

            # background image
            img3=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\moon.jpg") 
            img3=img3.resize((1495,700), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg3=ImageTk.PhotoImage(img3)

            backgroundImage=Label(self.root,image=self.photoImg3) #to set image on window
            backgroundImage.place(x=0,y=130,width=1495,height=700)

            titleLabel=Label(backgroundImage, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 30,"bold"),bg="white", fg="red",)
            titleLabel.place(x=0,y=0,width=1500,height=45)

            # *********time*****
            def time():
                string=strftime('%H:%M:%S %p')
                lbl.config(text=string)
                lbl.after(1000,time)

            lbl=Label(titleLabel,font=("times new roman", 15,"bold"),bg="white", fg="black")
            lbl.place(x=0,y=0,width=110,height=40)
            time()


            #student button
            img4=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\studentButton.jpg") 
            img4=img4.resize((220,220), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg4=ImageTk.PhotoImage(img4)

            button1=Button(backgroundImage,command=self.studentDetails,image=self.photoImg4, cursor="hand2")
            button1.place(x=120 ,y=80, width=220, height=220)

            button1_1=Button(backgroundImage,text="students Details",command=self.studentDetails, cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
            button1_1.place(x=120,y=280, width=220, height=40)
            
            #detect face button
            img5=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\faceDetector.jpg") 
            img5=img5.resize((220,220), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg5=ImageTk.PhotoImage(img5)

            button1=Button(backgroundImage,command=self.faceData,image=self.photoImg5, cursor="hand2")
            button1.place(x=420 ,y=80, width=220, height=220)

            button1_1=Button(backgroundImage,command=self.faceData,text="Face Detector", cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
            button1_1.place(x=420,y=280, width=220, height=40)

            #Attendance face button
            img6=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\att.jpg") 
            img6=img6.resize((220,220), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg6=ImageTk.PhotoImage(img6)

            button1=Button(backgroundImage,image=self.photoImg6,command=self.AttendanceData, cursor="hand2")
            button1.place(x=720 ,y=80, width=220, height=220)

            button1_1=Button(backgroundImage,text="Student Attendance",command=self.AttendanceData,cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
            button1_1.place(x=720,y=280, width=220, height=40)

        #     #help button
            img7=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\help.png") 
            img7=img7.resize((220,220), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg7=ImageTk.PhotoImage(img7)

            button1=Button(backgroundImage,command=self.helpDesk,image=self.photoImg7, cursor="hand2")
            button1.place(x=1020 ,y=80, width=220, height=220)

            button1_1=Button(backgroundImage,text="Help Desk",command=self.helpDesk, cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
            button1_1.place(x=1020,y=280, width=220, height=40)

        #     #train button
            img8=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\train.jpg") 
            img8=img8.resize((220,220), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg8=ImageTk.PhotoImage(img8)

            button1=Button(backgroundImage,command=self.Train,image=self.photoImg8, cursor="hand2")
            button1.place(x=120 ,y=340, width=220, height=220)

            button1_1=Button(backgroundImage,text="Train Data",command=self.Train, cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
            button1_1.place(x=120,y=520, width=220, height=40)

        #     #photos button
            img9=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\photos.jpg") 
            img9=img9.resize((220,220), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg9=ImageTk.PhotoImage(img9)

            button1=Button(backgroundImage,command=self.openImage,image=self.photoImg9, cursor="hand2")
            button1.place(x=420 ,y=340, width=220, height=220)

            button1_1=Button(backgroundImage,text="Photos",command=self.openImage, cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
            button1_1.place(x=420,y=520, width=220, height=40)

        #     #Developer button
            img10=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\deve.jpg") 
            img10=img10.resize((220,220), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg10=ImageTk.PhotoImage(img10)

            button1=Button(backgroundImage,command=self.DevData,image=self.photoImg10, cursor="hand2")
            button1.place(x=720 ,y=340, width=220, height=220)

            button1_1=Button(backgroundImage,text="Developer", command=self.DevData,cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
            button1_1.place(x=720,y=520, width=220, height=40)

        #     #Exit button
            img11=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\exit.jpg") 
            img11=img11.resize((220,220), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg11=ImageTk.PhotoImage(img11)

            button1=Button(backgroundImage,image=self.photoImg11, cursor="hand2")
            button1.place(x=1020 ,y=340, width=220, height=220)

            button1_1=Button(backgroundImage,text="Exit", cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
            button1_1.place(x=1020,y=520, width=220, height=40)


        def openImage(self):
            os.startfile("data")

# *******************Function Buttons******************
        def studentDetails(self):
            self.newWindow=Toplevel(self.root)
            self.app=Student(self.newWindow)

        def Train(self):
            self.newWindow=Toplevel(self.root)
            self.app=Train(self.newWindow)
            
        def faceData(self):
            self.newWindow=Toplevel(self.root)
            self.app=faceRecoginizer(self.newWindow)

        def AttendanceData(self):
            self.newWindow=Toplevel(self.root)
            self.app=Attendance(self.newWindow)

        def DevData(self):
            self.newWindow=Toplevel(self.root)
            self.app=Developer(self.newWindow)

        def helpDesk(self):
            self.newWindow=Toplevel(self.root)
            self.app=Help(self.newWindow)

        def iExit(self):
            self.iExit=tkinter.messagebox.askyesno("Face Recogintion","Are you sure you want to exit this project",parent=self.root)
            if self.iExit>0:
                self.root.destroy()
            
            else:
                return


if __name__ == "__main__":
        root=Tk()  #call root with toolkit
        obj=faceRecognitionSystem(root)  #make object of class and give the class name and pass root because we want to connect them
        root.mainloop() #close the main loop