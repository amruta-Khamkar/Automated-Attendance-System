from tkinter import* #for GUI applications
from tkinter import ttk  #it has some styling toolkits
from PIL import Image,ImageTk  #for insert images properly=> pillow
from tkinter import messagebox
import mysql.connector
import cv2 #open source computer vision libraries contains more than 2500 machine learning algorithms
import os
import numpy as np
from time import strftime
from datetime import datetime




class faceRecoginizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1495x700+0+0")
        self.root.title("Face Recogintion System ")

        titleLabel=Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30,"bold"),bg="white", fg="GREEN")
        titleLabel.place(x=0,y=0,width=1400,height=30)

        imgTop=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\facee.jpg") 
        imgTop=imgTop.resize((600,700), Image.ANTIALIAS) #convert high level image to low image
        self.photoimgTop=ImageTk.PhotoImage(imgTop)

        firstLabel=Label(self.root,image=self.photoimgTop) #to set image on window
        firstLabel.place(x=0,y=35,width=600,height=700)

        imgBottom=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\must.jpg") 
        imgBottom=imgBottom.resize((790,700), Image.ANTIALIAS) #convert high level image to low image
        self.photoimgBottom=ImageTk.PhotoImage(imgBottom)

        firstLabel=Label(self.root,image=self.photoimgBottom) #to set image on window
        firstLabel.place(x=600,y=35,width=790,height=700)

        button1_1=Button(firstLabel,text="FACE RECOGNITION",command=self.faceRecog, cursor="hand2",font=("times new roman", 18,"bold"),bg="black", fg="white")
        button1_1.place(x=235,y=610, width=300, height=50)

# ***********Attendance***************
    def markAttendance(self,i,p,q,r,s):
        with open("Address.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry=line.split((",")) #split data by comma
                nameList.append(entry[0])
            if((i not in nameList) and (p not in nameList) and (q not in nameList) and (r not in nameList) and (s not in nameList)):
                now=datetime.now()
                d1=now.strftime("%d-%m-%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{p},{q},{r},{s},{dtString},{d1},Present")




# *************face recogintion******
    def faceRecog(self):
        def drawBoundary(img,classifier,scaleFactor,minimumNeighbors,color,text,clf):
            greyImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(greyImage,scaleFactor,minimumNeighbors)

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(greyImage[y:y+h,x:x+w])
                
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root",password="",database="face_recoginizer")           
                myCursor=conn.cursor()

                myCursor = conn.cursor(buffered=True)
                myCursor.execute("select studentId from student where studentId="+str(id))
                i=myCursor.fetchone()
                i=' '.join(i)

                myCursor.execute("select Name from student where studentId="+str(id))
                p=myCursor.fetchone()
                p=' '.join(p)

                myCursor.execute("select RollNumber from student where studentId="+str(id))
                q=myCursor.fetchone()
                q=' '.join(q)

                myCursor.execute("select Course from student where studentId="+str(id))
                r=myCursor.fetchone()
                r=' '.join(r)

                myCursor.execute("select Department from student where studentId="+str(id))
                s=myCursor.fetchone()
                s=' '.join(s)


                if confidence>70:
                    cv2.putText(img,f"studentId:{i}",(x,y-120),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Name:{p}",(x,y-90),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"RollNumber:{q}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Course:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Department:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    self.markAttendance(i,p,q,r,s)
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
            
            return coord
 
        def recognize(img,clf,faceCascade):
            coord=drawBoundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        camera_port=0
        videoCap=cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
        
        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recogintion !", img)

            if cv2.waitKey(1)==13:
                break
        videoCap.release()
        cv2.destroyAllWindows()








if __name__ == "__main__":
  root=Tk()  #call root  with toolkit
  obj=faceRecoginizer(root)  #make object of class and give the class name and pass root because we want to connect them
  root.mainloop() #close the main loop
