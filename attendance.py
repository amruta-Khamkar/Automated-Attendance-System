from tkinter import* #for GUI applications
from tkinter import ttk  #it has some styling toolkits
from PIL import Image,ImageTk  #for insert images properly=> pillow
from tkinter import messagebox
import mysql.connector
import cv2 #open source computer vision libraries contains more than 2500 machine learning algorithms
import os 
import csv
from tkinter import filedialog

myData=[]
class Attendance:
   def __init__(self,root):
            self.root=root
            self.root.geometry("1495x700+0+0")
            self.root.title("Face Recogintion System ")

            # ***********Variables*********
            self.varId=StringVar()
            self.varName=StringVar()
            self.varRoll=StringVar()
            self.varCourse=StringVar()
            self.varDep=StringVar()
            self.varTime=StringVar()
            self.varDate=StringVar()
            self.varAttendance=StringVar()

               # first image
            img=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\student1.jpg") 
            img=img.resize((740,200), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg=ImageTk.PhotoImage(img)

            firstLabel=Label(self.root,image=self.photoImg) #to set image on window
            firstLabel.place(x=0,y=0,width=740,height=200)

            # second image
            img1=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\student2.jpg") 
            img1=img1.resize((752,200), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg1=ImageTk.PhotoImage(img1)

            firstLabel=Label(self.root,image=self.photoImg1) #to set image on window
            firstLabel.place(x=740,y=0,width=752,height=200)

            img3=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\moon.jpg") 
            img3=img3.resize((1495,700), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg3=ImageTk.PhotoImage(img3)

            backgroundImage=Label(self.root,image=self.photoImg3) #to set image on window
            backgroundImage.place(x=0,y=200,width=1495,height=700)

            titleLabel=Label(backgroundImage, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 30,"bold"),bg="white", fg="green")
            titleLabel.place(x=0,y=0,width=1500,height=40)

             #main frame
            mainFrame=Frame(backgroundImage,bd=2,bg="white")
            mainFrame.place(x=10,y=48,width=1340, height=440)

            #left label frame
            leftFrame=LabelFrame(mainFrame,bd=3,relief=RIDGE,text="Student Attendance Details",font=("sans-serif",12, "bold"),bg="white")
            leftFrame.place(x=5,y=10,width=660,height=420)

            leftImage=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\student3.jpg") 
            leftImage=leftImage.resize((640,100), Image.ANTIALIAS) #convert high level image to low image
            self.photoleftImage=ImageTk.PhotoImage(leftImage)

            firstLabel=Label(leftFrame,image=self.photoleftImage) #to set image on window
            firstLabel.place(x=3,y=0,width=650,height=100)

            classFrame=LabelFrame(leftFrame,bd=3,relief=RIDGE,bg="white",text="Class Student",font=("sans-serif",12, "bold"))
            classFrame.place(x=5,y=110,width=635,height=300)

            # student id
            studentIdLabel=Label(classFrame,text="AttendanceId",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=0,column=0,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=17,textvariable=self.varId,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=0,column=1,padx=8, pady=3,sticky=W)


            #Roll Number
            studentIdLabel=Label(classFrame,text="Roll Number",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=0,column=2,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=17,textvariable=self.varRoll,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=0,column=3,padx=8, pady=3,sticky=W)

            # student name
            studentIdLabel=Label(classFrame,text="Student Name:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=1,column=0,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=17,textvariable=self.varName,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=1,column=1,padx=8, pady=3,sticky=W)

            # Department
            studentIdLabel=Label(classFrame,text="Department:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=1,column=2,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=17,textvariable=self.varDep,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=1,column=3,padx=8, pady=3,sticky=W)

            #Time
            studentIdLabel=Label(classFrame,text="Time:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=2,column=0,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=17,textvariable=self.varTime,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=2,column=1,padx=8, pady=3,sticky=W)

            #Date
            studentIdLabel=Label(classFrame,text="Date:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=2,column=2,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=17,textvariable=self.varDate,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=2,column=3,padx=8, pady=3,sticky=W)

            # Attendance status
            studentIdLabel=Label(classFrame,text=" Attendance Status:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=3,column=0,padx=5,pady=3,sticky=W)

            divCombo=ttk.Combobox(classFrame,font=("sans-serif",10, "bold" ),textvariable=self.varAttendance,state="readonly",width=20)
            divCombo["values"]=("Status","Present","Absent")
            divCombo.current(0)
            divCombo.grid(row=3,column=1,padx=4,pady=8, sticky=W) 

            #buttons frame
            buttonFrame=Frame(classFrame,bd=2,relief=RIDGE,bg="white")
            buttonFrame.place(x=0,y=226,width=635, height=120)

            saveButton=Button(buttonFrame,text="Import csv",command=self.importCsv, width=15,cursor="hand2", font=("sans-serif",12,"bold"),bg="blue", fg="white")
            saveButton.grid(row=0,column=0)

            updateButton=Button(buttonFrame,text="Export csv",command=self.exportCsv, width=15,cursor="hand2", font=("sans-serif",12,"bold"),bg="blue", fg="white")
            updateButton.grid(row=0,column=1)
            
            updateButton=Button(buttonFrame,text="Update", width=15,cursor="hand2", font=("sans-serif",12,"bold"),bg="blue", fg="white")
            updateButton.grid(row=0,column=2)

            resetButton=Button(buttonFrame,text="Reset", width=15,command=self.resetData,cursor="hand2", font=("sans-serif",12,"bold"),bg="blue", fg="white")
            resetButton.grid(row=0,column=3)


            #right label frame
            rightFrame=LabelFrame(mainFrame,bd=3,bg="white",relief=RIDGE,text="Attendance Details",font=("sans-serif",12, "bold"))
            rightFrame.place(x=675,y=10,width=660,height=420)

            tableFrame=LabelFrame(rightFrame,bd=3,relief=RIDGE,bg="white",font=("sans-serif",12, "bold"))
            tableFrame.place(x=6,y=5,width=635,height=380)

            scrollX=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
            scrollY=ttk.Scrollbar(tableFrame,orient=VERTICAL)

            self.AttendanceReportTable=ttk.Treeview(tableFrame,column=("studentId","Name","RollNumber","Course","Department","Time","Date","Attendance"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

            scrollX.pack(side=BOTTOM,fill=X)
            scrollY.pack(side=RIGHT,fill=Y)
            scrollX.config(command=self.AttendanceReportTable.xview)
            scrollY.config(command=self.AttendanceReportTable.yview)

            self.AttendanceReportTable.heading("studentId", text="studentId")
            self.AttendanceReportTable.heading("Name", text="Name")
            self.AttendanceReportTable.heading("RollNumber", text="Roll Number")
            self.AttendanceReportTable.heading("Course", text="Course")
            self.AttendanceReportTable.heading("Department", text="Department")
            self.AttendanceReportTable.heading("Time", text="Time")
            self.AttendanceReportTable.heading("Date", text="Date")
            self.AttendanceReportTable.heading("Attendance", text="Attendance")
            self.AttendanceReportTable["show"]="headings"

            self.AttendanceReportTable.column("studentId",width=100)
            self.AttendanceReportTable.column("Name",width=100)
            self.AttendanceReportTable.column("RollNumber",width=100)
            self.AttendanceReportTable.column("Course",width=100)
            self.AttendanceReportTable.column("Department",width=100)
            self.AttendanceReportTable.column("Time",width=100)
            self.AttendanceReportTable.column("Date",width=100)
            self.AttendanceReportTable.column("Attendance",width=100)

            self.AttendanceReportTable.bind("<ButtonRelease>",self.getCursor)
            self.AttendanceReportTable.pack(fill=BOTH,expand=1)

            # *************fetch data**********
   def fetchData(self,rows):
           self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
           for i in rows:
              self.AttendanceReportTable.insert("",END, values=i)

            #   **********import csv**************

   def importCsv(self):
           global myData
           myData.clear()
           fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("Al File","*.*")),parent=self.root)
           with open(fln) as myFile:
              csvRead=csv.reader(myFile,delimiter=",")
              for i in csvRead: 
                myData.append(i)
           self.fetchData(myData)


           #  **********import csv**************
   def exportCsv(self):
      try:
         if len(myData)<1:
            messagebox.showerror("No Data","No data found to export", parent=self.root)
            return False

         fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("Al File","*.*")),parent=self.root)
         with open(fln,mode="w",newline="\n") as myFile:
            expWrite=csv.writer(myFile,delimiter=",")
            for i in myData: 
                expWrite.writerow(i)
                messagebox.showinfo("Data Export","Your data exported "+os.path.basename(fln)+" Successfully")
      except Exception as es:
         messagebox.showerror("Error",f"Due To : {str(es)}", parent=self.root)

            # **********get cursor*********
   def getCursor(self,event=" "):
      cursorRow=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursorRow)
      data=content["values"]

      self.varId.set(data[0]),
      self.varName.set(data[1]),
      self.varRoll.set(data[2]),
      self.varCourse.set(data[3]),
      self.varDep.set(data[4]),
      self.varTime.set(data[5]),
      self.varDate.set(data[6]),
      self.varAttendance.set(data[7])

      # *********Reset Button*******
   def resetData(self):
            self.varId.set(" ")
            self.varName.set(" ")
            self.varRoll.set(" ")
            self.varCourse.set(" ")
            self.varDep.set(" ")
            self.varTime.set(" ")
            self.varDate.set(" ")
            self.varAttendance.set("Status")







         
      

if __name__ == "__main__":

  root=Tk()  #call root  with toolkit
  obj=Attendance(root)  #make object of class and give the class name and pass root because we want to connect them
  root.mainloop() #close the main loop