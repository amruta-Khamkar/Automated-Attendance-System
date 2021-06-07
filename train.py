from tkinter import* #for GUI applications
from tkinter import ttk  #it has some styling toolkits
from PIL import Image,ImageTk  #for insert images properly=> pillow
from tkinter import messagebox
import mysql.connector
import cv2 #open source computer vision libraries contains more than 2500 machine learning algorithms
import os
import numpy as np


class Train:
    def __init__(self,root):
            self.root=root
            self.root.geometry("1495x700+0+0")
            self.root.title("Face Recogintion System ")

            titleLabel=Label(self.root, text="TRAIN DATA SET", font=("times new roman", 30,"bold"),bg="white", fg="purple")
            titleLabel.place(x=0,y=0,width=1400,height=30)

            imgTop=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\trainData.png") 
            imgTop=imgTop.resize((1405,382), Image.ANTIALIAS) #convert high level image to low image
            self.photoimgTop=ImageTk.PhotoImage(imgTop)

            firstLabel=Label(self.root,image=self.photoimgTop) #to set image on window
            firstLabel.place(x=0,y=35,width=1405,height=382)

            button1_1=Button(self.root,text="TRAIN DATA",command=self.trainClassifier, cursor="hand2",font=("times new roman", 18,"bold"),bg="red", fg="white")
            button1_1.place(x=0,y=260, width=1400, height=60)


            imgBottom=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\trainPpl.jpg") 
            imgBottom=imgBottom.resize((1400,385), Image.ANTIALIAS) #convert high level image to low image
            self.photoimgBottom=ImageTk.PhotoImage(imgBottom)

            firstLabel=Label(self.root,image=self.photoimgBottom) #to set image on window
            firstLabel.place(x=0,y=320,width=1400,height=385)


    def trainClassifier(self):
        dataDir=("data")
        path=[os.path.join (dataDir,file) for file in os.listdir(dataDir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #converts gray scale image
            imageNp=np.array(img,'uint8') #it is data type #we use numpy for converting into array efficiently and it increases performance of 88%
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
        
        # *************Train the classifier and save***********

        classifier=cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces,ids)
        classifier.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")




if __name__ == "__main__":
  root=Tk()  #call root  with toolkit
  obj=Train(root)  #make object of class and give the class name and pass root because we want to connect them
  root.mainloop() #close the main loop