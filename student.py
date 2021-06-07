from tkinter import* #for GUI applications
from tkinter import ttk  #it has some styling toolkits
from PIL import Image,ImageTk  #for insert images properly=> pillow
from tkinter import messagebox
import mysql.connector
import cv2 #open source computer vision libraries contains more than 2500 machine learning algorithms


class Student:
    def __init__(self,root):
            self.root=root
            self.root.geometry("1495x700+0+0")
            self.root.title("Face Recogintion System ")

            # **********************variables************
            self.varDep=StringVar()
            self.varCourse=StringVar()
            self.varYear=StringVar()
            self.varSem=StringVar()
            self.varId=StringVar()
            self.varRoll=StringVar()
            self.varName=StringVar()
            self.varDiv=StringVar()
            self.varGen=StringVar()
            self.varDOB=StringVar()
            self.varEmail=StringVar()
            self.varPhone=StringVar()
            self.varParents=StringVar()
            self.varCity=StringVar()

              # first image
            img=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\student1.jpg") 
            img=img.resize((490,100), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg=ImageTk.PhotoImage(img)

            firstLabel=Label(self.root,image=self.photoImg) #to set image on window
            firstLabel.place(x=0,y=0,width=490,height=100)

            # second image
            img1=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\student2.jpg") 
            img1=img1.resize((490,100), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg1=ImageTk.PhotoImage(img1)

            firstLabel=Label(self.root,image=self.photoImg1) #to set image on window
            firstLabel.place(x=490,y=0,width=490,height=100)

            # third image
            img2=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\student3.jpg") 
            img2=img2.resize((490,100), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg2=ImageTk.PhotoImage(img2)

            firstLabel=Label(self.root,image=self.photoImg2) #to set image on window
            firstLabel.place(x=980,y=0,width=490,height=100)

              # background image
            img3=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\moon.jpg") 
            img3=img3.resize((1495,700), Image.ANTIALIAS) #convert high level image to low image
            self.photoImg3=ImageTk.PhotoImage(img3)

            backgroundImage=Label(self.root,image=self.photoImg3) #to set image on window
            backgroundImage.place(x=0,y=110,width=1495,height=700)

            titleLabel=Label(backgroundImage, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30,"bold"),bg="white", fg="green")
            titleLabel.place(x=0,y=0,width=1500,height=40)

            #main frame
            mainFrame=Frame(backgroundImage,bd=2,bg="white")
            mainFrame.place(x=10,y=48,width=1340, height=530)

            #left label frame
            leftFrame=LabelFrame(mainFrame,bd=3,relief=RIDGE,text="Student Details",font=("sans-serif",12, "bold"),bg="white")
            leftFrame.place(x=5,y=10,width=660,height=510)

            leftImage=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\student3.jpg") 
            leftImage=leftImage.resize((640,100), Image.ANTIALIAS) #convert high level image to low image
            self.photoleftImage=ImageTk.PhotoImage(leftImage)

            firstLabel=Label(leftFrame,image=self.photoleftImage) #to set image on window
            firstLabel.place(x=3,y=0,width=650,height=100)

            #current course
            currentFrame=LabelFrame(leftFrame,bd=3,relief=RIDGE,bg="white",text="Current Course Details",font=("sans-serif",12, "bold"))
            currentFrame.place(x=5,y=110,width=635,height=100)

            #department label
            departLabel=Label(currentFrame,text="Department",font=("sans-serif",10, "bold" ),bg="white")
            departLabel.grid(row=0,column=0,padx=2,pady=8)

            departCombo=ttk.Combobox(currentFrame,textvariable=self.varDep,font=("sans-serif",10, "bold" ),state="readonly",width=17)
            departCombo["values"]=("Select Department","Computer","IT","Mechanical","Civil","Electrical","EXTC")
            departCombo.current(0)
            departCombo.grid(row=0,column=1,padx=2,pady=8)

            #Course
            courseLabel=Label(currentFrame,text="Course",font=("sans-serif",10, "bold" ),bg="white")
            courseLabel.grid(row=0,column=2,padx=2,pady=8,sticky=W)

            courseCombo=ttk.Combobox(currentFrame,textvariable=self.varCourse,font=("sans-serif",10, "bold" ),state="readonly",width=17)
            courseCombo["values"]=("Select Course","FE","SE","TE","BE")
            courseCombo.current(0)
            courseCombo.grid(row=0,column=3,padx=2,pady=8, sticky=W)

            #year
            yearLabel=Label(currentFrame,text="Year",font=("sans-serif",10, "bold" ),bg="white")
            yearLabel.grid(row=1,column=0,padx=2,pady=8)

            yearCombo=ttk.Combobox(currentFrame,textvariable=self.varYear,font=("sans-serif",10, "bold" ),state="readonly",width=17)
            yearCombo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
            yearCombo.current(0)
            yearCombo.grid(row=1,column=1,padx=2,pady=8,sticky=W)

            #semester
            semLabel=Label(currentFrame,text="Semester",font=("sans-serif",10, "bold" ),bg="white")
            semLabel.grid(row=1,column=2,padx=2,pady=8)

            semCombo=ttk.Combobox(currentFrame,textvariable=self.varSem,font=("sans-serif",10, "bold" ),state="readonly",width=17)
            semCombo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
            semCombo.current(0)
            semCombo.grid(row=1,column=3,padx=2,pady=8, sticky=W) 

            #Student information
            classFrame=LabelFrame(leftFrame,bd=3,relief=RIDGE,bg="white",text="Class Student",font=("sans-serif",12, "bold"))
            classFrame.place(x=5,y=205,width=635,height=300)

            #Student id
            studentIdLabel=Label(classFrame,text="studentId",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=0,column=0,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=15,textvariable=self.varId,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=0,column=1,padx=8, pady=3,sticky=W)

            #Roll Number
            studentIdLabel=Label(classFrame,text="Roll Number",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=0,column=2,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=15,textvariable=self.varRoll,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=0,column=3,padx=8, pady=3,sticky=W)

            # student name
            studentIdLabel=Label(classFrame,text="Student Name:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=1,column=0,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=15,textvariable=self.varName,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=1,column=1,padx=8, pady=3,sticky=W)

            #class division
            studentIdLabel=Label(classFrame,text=" Class Division:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=1,column=2,padx=5,pady=3,sticky=W)

            divCombo=ttk.Combobox(classFrame,textvariable=self.varDiv,font=("sans-serif",10, "bold" ),state="readonly",width=17)
            divCombo["values"]=("A","B","C","D")
            divCombo.current(0)
            divCombo.grid(row=1,column=3,padx=4,pady=8, sticky=W) 


            #Gender
            studentIdLabel=Label(classFrame,text="Gender:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=2,column=0,padx=8,pady=3,sticky=W)

            genderCombo=ttk.Combobox(classFrame,textvariable=self.varGen,font=("sans-serif",10, "bold" ),state="readonly",width=17)
            genderCombo["values"]=("Female","Male","Others")
            genderCombo.current(0)
            genderCombo.grid(row=2,column=1,padx=4,pady=8, sticky=W) 

            # DOB
            studentIdLabel=Label(classFrame,text="DOB:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=2,column=2,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=15,textvariable=self.varDOB,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=2,column=3,padx=8, pady=3,sticky=W)

            #email
            studentIdLabel=Label(classFrame,text="Email:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=3,column=0,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=15,textvariable=self.varEmail,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=3,column=1,padx=8, pady=3,sticky=W)

            #Phone Number
            studentIdLabel=Label(classFrame,text="Phone Number:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=3,column=2,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=15,textvariable=self.varPhone,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=3,column=3,padx=8, pady=3,sticky=W)

            #parents number
            studentIdLabel=Label(classFrame,text="Parents Number:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=4,column=0,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=15,textvariable=self.varParents,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=4,column=1,padx=8, pady=3,sticky=W)

            #City
            studentIdLabel=Label(classFrame,text="City:",font=("sans-serif",10, "bold" ),bg="white")
            studentIdLabel.grid(row=4,column=2,padx=8,pady=3,sticky=W)

            studentIdEntry=ttk.Entry(classFrame,width=15,textvariable=self.varCity,font=("sans-serif",12, "bold"))
            studentIdEntry.grid(row=4,column=3,padx=8, pady=3,sticky=W)

            #radio buttons
            self.varRadio1=StringVar()
            radioButton1=ttk.Radiobutton(classFrame,variable=self.varRadio1,text="Take Photo Sample", value="Yes")
            radioButton1.grid(row=5, column=0, padx=4,pady=4)

            radioButton2=ttk.Radiobutton(classFrame,variable=self.varRadio1,text="No Photo Sample", value="No")
            radioButton2.grid(row=5, column=1, padx=4,pady=4)

            #buttons frame
            buttonFrame=Frame(classFrame,bd=2,relief=RIDGE,bg="white")
            buttonFrame.place(x=0,y=195,width=635, height=120)

            saveButton=Button(buttonFrame,text="Save",command=self.addData, width=20,cursor="hand2", font=("sans-serif",12,"bold"),bg="blue", fg="white")
            saveButton.grid(row=0,column=0)

            updateButton=Button(buttonFrame,text="Update",command=self.updateData, width=20,cursor="hand2", font=("sans-serif",12,"bold"),bg="blue", fg="white")
            updateButton.grid(row=0,column=1)
            
            resetButton=Button(buttonFrame,text="Reset",command=self.resetData, width=20,cursor="hand2", font=("sans-serif",12,"bold"),bg="blue", fg="white")
            resetButton.grid(row=0,column=2)

            takePhoto=Button(buttonFrame,text="Take Photo Sample",command=self.generateDataset,cursor="hand2", width=20, font=("sans-serif",12,"bold"),bg="blue", fg="white")
            takePhoto.grid(row=1,column=0)

            updatePhoto=Button(buttonFrame,text="Update Photo Sample",cursor="hand2", width=20, font=("sans-serif",12,"bold"),bg="blue", fg="white")
            updatePhoto.grid(row=1,column=2)





            #right label frame
            rightFrame=LabelFrame(mainFrame,bd=3,bg="white",relief=RIDGE,text="Student Details",font=("sans-serif",12, "bold"))
            rightFrame.place(x=675,y=10,width=660,height=510)

            rightImage=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\student3.jpg") 
            rightImage=rightImage.resize((640,100), Image.ANTIALIAS) #convert high level image to low image
            self.photorightImage=ImageTk.PhotoImage(leftImage)

            firstLabel=Label(rightFrame,image=self.photorightImage) #to set image on window
            firstLabel.place(x=3,y=0,width=650,height=100)

            # **********Search system**********
            searchFrame=LabelFrame(rightFrame,bd=3,relief=RIDGE,bg="white",text="Search system",font=("sans-serif",12, "bold"))
            searchFrame.place(x=5,y=110,width=635,height=70)

            searchLabel=Label(searchFrame,text="Search By :",font=("sans-serif",10, "bold" ),bg="white")
            searchLabel.grid(row=0,column=0,padx=2,pady=8)

            serachCombo=ttk.Combobox(searchFrame,textvariable=self.varSem,font=("sans-serif",10, "bold" ),state="readonly",width=17)
            serachCombo["values"]=("Select","RollNo","PhoneNo")
            serachCombo.current(0)
            serachCombo.grid(row=0,column=1,padx=2,pady=8, sticky=W) 

            serachButton=Button(searchFrame,text="Search",command=self.resetData, width=15,cursor="hand2", font=("sans-serif",12,"bold"),bg="blue", fg="white")
            serachButton.grid(row=0,column=3,padx=4)

            showButton=Button(searchFrame,text="Show All",command=self.resetData, width=15,cursor="hand2", font=("sans-serif",12,"bold"),bg="blue", fg="white")
            showButton.grid(row=0,column=4,padx=4)

            # ****************table frame*********
            tableFrame=LabelFrame(rightFrame,bd=3,relief=RIDGE,bg="white",text="Search system",font=("sans-serif",12, "bold"))
            tableFrame.place(x=5,y=180,width=635,height=300)

            scrollX=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
            scrollY=ttk.Scrollbar(tableFrame,orient=VERTICAL)

            self.studentTable=ttk.Treeview(tableFrame,column=("dep","course","year","sem","studentId","roll","name","div","gender","dob","email","phone","parents","City","photo"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
            scrollX.pack(side=BOTTOM,fill=X)
            scrollY.pack(side=RIGHT,fill=Y)
            scrollX.config(command=self.studentTable.xview)
            scrollY.config(command=self.studentTable.yview)


            self.studentTable.heading("dep", text="Department")
            self.studentTable.heading("course", text="Course")
            self.studentTable.heading("year", text="Year")
            self.studentTable.heading("sem", text="Semester")
            self.studentTable.heading("studentId", text="studentId")
            self.studentTable.heading("roll", text="Roll Number")
            self.studentTable.heading("name", text="Name")
            self.studentTable.heading("div", text="Division")
            self.studentTable.heading("gender", text="Gender")
            self.studentTable.heading("dob", text="DOB")
            self.studentTable.heading("email", text="Email")
            self.studentTable.heading("phone", text="Phone Number")
            self.studentTable.heading("parents", text="Parents Number")
            self.studentTable.heading("City", text="City")
            self.studentTable.heading("photo", text="photoSampleStatus")
            self.studentTable["show"]="headings"

            self.studentTable.column("dep",width=100)
            self.studentTable.column("course",width=100)
            self.studentTable.column("year",width=100)
            self.studentTable.column("sem",width=100)
            self.studentTable.column("studentId",width=100)
            self.studentTable.column("roll",width=100)
            self.studentTable.column("name",width=100)
            self.studentTable.column("div",width=100)
            self.studentTable.column("gender",width=100)
            self.studentTable.column("dob",width=100)
            self.studentTable.column("email",width=100)
            self.studentTable.column("phone",width=100)
            self.studentTable.column("parents",width=100)
            self.studentTable.column("City",width=100)
            self.studentTable.column("photo",width=140)

            self.studentTable.pack(fill=BOTH,expand=1)
            self.studentTable.bind("<ButtonRelease>",self.getCursor)
            self.fetchData()
            
            # qsn1
            # qsn1Label=Label(rightFrame,text="I enjoy meeting new people",font=("sans-serif",10, "bold" ),bg="white")
            # qsn1Label.grid(row=0,column=0,padx=3,pady=3,sticky=W)3
            # self.varqsn1=StringVar()

            # agreeButton2=ttk.Radiobutton(rightFrame,variable=self.varqsn1,text="Agree", value="Agree",width=15)
            # agreeButton2.grid(row=1, column=0,padx=30,pady=3,sticky=W)
           
            # disagreeButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn1,text="Disagree", value="Disagree",width=15)
            # disagreeButton1.grid(row=1, column=1,padx=30,pady=3,sticky=W)

            # unsureButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn1,text="Unsure", value="Unsure",width=15)
            # unsureButton1.grid(row=1, column=2,padx=30,pady=3,sticky=W)

            # # qsn2
            # qsn1Label=Label(rightFrame,text="I enjoy meeting new people",font=("sans-serif",10, "bold" ),bg="white")
            # qsn1Label.grid(row=2,column=0,padx=3,pady=3,sticky=W)
            # self.varqsn2=StringVar()

            # agreeButton2=ttk.Radiobutton(rightFrame,variable=self.varqsn2,text="Agree", value="Agree",width=15)
            # agreeButton2.grid(row=3, column=0,padx=30,pady=3,sticky=W)
           
            # disagreeButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn2,text="Disagree", value="Disagree",width=15)
            # disagreeButton1.grid(row=3, column=1,padx=30,pady=3,sticky=W)

            # unsureButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn2,text="Unsure", value="Unsure",width=15)
            # unsureButton1.grid(row=3, column=2,padx=30,pady=3,sticky=W)

            # # qsn3
            # qsn1Label=Label(rightFrame,text="I enjoy meeting new people",font=("sans-serif",10, "bold" ),bg="white")
            # qsn1Label.grid(row=4,column=0,padx=3,pady=3,sticky=W)
            # self.varqsn3=StringVar()

            # agreeButton2=ttk.Radiobutton(rightFrame,variable=self.varqsn3,text="Agree", value="Agree",width=15)
            # agreeButton2.grid(row=5, column=0,padx=30,pady=3,sticky=W)
           
            # disagreeButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn3,text="Disagree", value="Disagree",width=15)
            # disagreeButton1.grid(row=5, column=1,padx=30,pady=3,sticky=W)

            # unsureButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn3,text="Unsure", value="Unsure",width=15)
            # unsureButton1.grid(row=5, column=2,padx=30,pady=3,sticky=W)

            # # qsn4
            # qsn1Label=Label(rightFrame,text="I enjoy meeting new people",font=("sans-serif",10, "bold" ),bg="white")
            # qsn1Label.grid(row=6,column=0,padx=3,pady=3,sticky=W)
            # self.varqsn4=StringVar()

            # agreeButton2=ttk.Radiobutton(rightFrame,variable=self.varqsn4,text="Agree", value="Agree",width=15)
            # agreeButton2.grid(row=7, column=0,padx=30,pady=3,sticky=W)
           
            # disagreeButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn4,text="Disagree", value="Disagree",width=15)
            # disagreeButton1.grid(row=7, column=1,padx=30,pady=3,sticky=W)

            # unsureButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn4,text="Unsure", value="Unsure",width=15)
            # unsureButton1.grid(row=7, column=2,padx=30,pady=3,sticky=W)

            # # qsn5
            # qsn1Label=Label(rightFrame,text="I enjoy meeting new people",font=("sans-serif",10, "bold" ),bg="white")
            # qsn1Label.grid(row=8,column=0,padx=3,pady=3,sticky=W)
            # self.varqsn5=StringVar()

            # agreeButton2=ttk.Radiobutton(rightFrame,variable=self.varqsn5,text="Agree", value="Agree",width=15)
            # agreeButton2.grid(row=9, column=0,padx=30,pady=3,sticky=W)
           
            # disagreeButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn5,text="Disagree", value="Disagree",width=15)
            # disagreeButton1.grid(row=9, column=1,padx=30,pady=3,sticky=W)

            # unsureButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn5,text="Unsure", value="Unsure",width=15)
            # unsureButton1.grid(row=9, column=2,padx=30,pady=3,sticky=W)

            # # qsn6
            # qsn1Label=Label(rightFrame,text="I enjoy meeting new people",font=("sans-serif",10, "bold" ),bg="white")
            # qsn1Label.grid(row=10,column=0,padx=3,pady=3,sticky=W)
            # self.varqsn6=StringVar()

            # agreeButton2=ttk.Radiobutton(rightFrame,variable=self.varqsn6,text="Agree", value="Agree",width=15)
            # agreeButton2.grid(row=11, column=0,padx=30,pady=3,sticky=W)
           
            # disagreeButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn6,text="Disagree", value="Disagree",width=15)
            # disagreeButton1.grid(row=11, column=1,padx=30,pady=3,sticky=W)

            # unsureButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn6,text="Unsure", value="Unsure",width=15)
            # unsureButton1.grid(row=11, column=2,padx=30,pady=3,sticky=W)

            # # qsn7
            # qsn1Label=Label(rightFrame,text="I enjoy meeting new people",font=("sans-serif",10, "bold" ),bg="white")
            # qsn1Label.grid(row=12,column=0,padx=3,pady=3,sticky=W)
            # self.varqsn7=StringVar()

            # agreeButton2=ttk.Radiobutton(rightFrame,variable=self.varqsn7,text="Agree", value="Agree",width=15)
            # agreeButton2.grid(row=13, column=0,padx=30,pady=3,sticky=W)
           
            # disagreeButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn7,text="Disagree", value="Disagree",width=15)
            # disagreeButton1.grid(row=13, column=1,padx=30,pady=3,sticky=W)

            # unsureButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn7,text="Unsure", value="Unsure",width=15)
            # unsureButton1.grid(row=13, column=2,padx=30,pady=3,sticky=W)

            # # qsn8
            # qsn1Label=Label(rightFrame,text="I enjoy meeting new people",font=("sans-serif",10, "bold" ),bg="white")
            # qsn1Label.grid(row=14,column=0,padx=3,pady=3,sticky=W)
            # self.varqsn8=StringVar()

            # agreeButton2=ttk.Radiobutton(rightFrame,variable=self.varqsn8,text="Agree", value="Agree",width=15)
            # agreeButton2.grid(row=15, column=0,padx=30,pady=3,sticky=W)
           
            # disagreeButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn8,text="Disagree", value="Disagree",width=15)
            # disagreeButton1.grid(row=15, column=1,padx=30,pady=3,sticky=W)

            # unsureButton1=ttk.Radiobutton(rightFrame,variable=self.varqsn8,text="Unsure", value="Unsure",width=15)
            # unsureButton1.grid(row=15, column=2,padx=30,pady=3,sticky=W)
            


    
    
    def addData(self):
        if self.varDep.get()=="Select Department" or self.varName.get()=="" or self.varRoll.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)            
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root",password="",database="face_recoginizer")           
                myCursor=conn.cursor()
                myCursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.varDep.get(),
                                                                                        self.varCourse.get(),
                                                                                        self.varYear.get(),
                                                                                        self.varSem.get(),
                                                                                        self.varId.get(),
                                                                                        self.varRoll.get(),
                                                                                        self.varName.get(),
                                                                                        self.varDiv.get(),
                                                                                        self.varGen.get(),
                                                                                        self.varDOB.get(),
                                                                                        self.varEmail.get(),
                                                                                        self.varPhone.get(),
                                                                                        self.varParents.get(),
                                                                                        self.varCity.get(),
                                                                                        self.varRadio1.get()
                                                                                        # self.varqsn1.get(),
                                                                                        # self.varqsn2.get(),
                                                                                        # self.varqsn3.get(),
                                                                                        # self.varqsn4.get(),
                                                                                        # self.varqsn5.get(),
                                                                                        # self.varqsn6.get(),
                                                                                        # self.varqsn7.get(),
                                                                                        # self.varqsn8.get()
                                                                                      
                                                                                        
                                                                                      ))
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Success", "Student Details Has been Added Successfully",parent=self.root)
            except Exception as es:
                  messagebox.showerror("Error",f"Due To : {str(es)}", parent=self.root)

    def fetchData(self):
      conn=mysql.connector.connect(host="localhost", username="root",password="",database="face_recoginizer")           
      myCursor=conn.cursor()
      myCursor.execute("select * from student")
      data=myCursor.fetchall()

      if len(data)!=0:
        self.studentTable.delete(*self.studentTable.get_children())
        for i in data:
          self.studentTable.insert("",END,values=i)
        conn.commit()
      conn.close()

# **********************get cursor***************
    def getCursor(self,event=""):
      cusrorFocus=self.studentTable.focus()
      content=self.studentTable.item(cusrorFocus)
      data=content["values"]

      self.varDep.set(data[0]),
      self.varCourse.set(data[1]),
      self.varYear.set(data[2]),
      self.varSem.set(data[3]),
      self.varId.set(data[4]),
      self.varRoll.set(data[5]),
      self.varName.set(data[6]),
      self.varDiv.set(data[7]),
      self.varGen.set(data[8]),
      self.varDOB.set(data[9]),
      self.varEmail.set(data[10]),
      self.varPhone.set(data[11]),
      self.varParents.set(data[12])
      self.varCity.set(data[13])
      self.varRadio1.set(data[14])
      
# ***************update button***********
    def updateData(self):
         if self.varDep.get()=="Select Department" or self.varName.get()=="" or self.varRoll.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)            
         else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details", parent=self.root)
                if Update>0:
                  conn=mysql.connector.connect(host="localhost", username="root",password="",database="face_recoginizer")           
                  myCursor=conn.cursor()
                  myCursor.execute("update Student set Department=%s, Course=%s, Year=%s, Semester=%s,RollNumber=%s,Name=%s, Division=%s,Gender=%s,DOB=%s,Email=%s,phoneNumber=%s,parentsNumber=%s,City=%s,photoSampleStatus=%s where studentId=%s",(
                                                                                                                                            self.varDep.get(),
                                                                                                                                            self.varCourse.get(),
                                                                                                                                            self.varYear.get(),
                                                                                                                                            self.varSem.get(),
                                                                                                                                            self.varRoll.get(),
                                                                                                                                            self.varName.get(),
                                                                                                                                            self.varDiv.get(),
                                                                                                                                            self.varGen.get(),
                                                                                                                                            self.varDOB.get(),
                                                                                                                                            self.varEmail.get(),
                                                                                                                                            self.varPhone.get(),
                                                                                                                                            self.varParents.get(),
                                                                                                                                            self.varCity.get(),
                                                                                                                                            self.varRadio1.get(),
                                                                                                                                            self.varId.get(),
                                                                                                                                      ))
                else:
                  if not Update:
                    return
                messagebox.showinfo("succcess","Student details has been updates Successfully", parent=self.root)
                conn.commit()
                self.fetchData()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}", parent=self.root)
      

#  ****************Reset button*************
    def resetData(self):
            self.varDep.set("Select Department")
            self.varCourse.set("Select Course")
            self.varYear.set("Select Year")
            self.varSem.set("Select Semester")
            self.varId.set(" ")
            self.varRoll.set(" ")
            self.varName.set(" ")
            self.varDiv.set(" ")
            self.varGen.set(" ")
            self.varDOB.set(" ")
            self.varEmail.set(" ")
            self.varPhone.set(" ")
            self.varParents.set(" ")
            self.varCity.set(" ")
            self.varRadio1.set(" ")
     
   # ***************Generate data set or take photo samples**********
    def generateDataset(self):
      if self.varDep.get()=="Select Department" or self.varName.get()=="" or self.varRoll.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)            
      else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root",password="",database="face_recoginizer")           
                myCursor=conn.cursor()
                myCursor.execute("select * from student")
                myResult=myCursor.fetchall()
                id=0
                for x in myResult:
                  id+=1
                myCursor.execute("update Student set Department=%s, Course=%s, Year=%s, Semester=%s,RollNumber=%s,Name=%s, Division=%s,Gender=%s,DOB=%s,Email=%s,phoneNumber=%s,parentsNumber=%s,City=%s,photoSampleStatus=%s where studentId=%s",(
                                                                                                                                            self.varDep.get(),
                                                                                                                                            self.varCourse.get(),
                                                                                                                                            self.varYear.get(),
                                                                                                                                            self.varSem.get(),
                                                                                                                                            self.varRoll.get(),
                                                                                                                                            self.varName.get(),
                                                                                                                                            self.varDiv.get(),
                                                                                                                                            self.varGen.get(),
                                                                                                                                            self.varDOB.get(),
                                                                                                                                            self.varEmail.get(),
                                                                                                                                            self.varPhone.get(),
                                                                                                                                            self.varParents.get(),
                                                                                                                                            self.varCity.get(),
                                                                                                                                            self.varRadio1.get(),
                                                                                                                                            self.varId.get()==id+1,
                                                                                                                                      ))
                conn.commit()
                self.fetchData()
                self.resetData()
                conn.close()

    #           ##############load predefined data on face frontals from opencv##############
                faceClassifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def faceCropped(img):
                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces=faceClassifier.detectMultiScale(gray,1.3,5)
                    #  scaling factor=1.3
                    #  minimum neighbor=5

                     for(x,y,w,h) in faces:
                        faceCropped=img[y:y+h,x:x+w]
                        return faceCropped

                capture=cv2.VideoCapture(0)
                imgId=0
                while True:
                    ret,frame=capture.read()
                    if faceCropped(frame) is not None:
                        imgId+=1
                        face=cv2.resize(faceCropped(frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        filePath="data/user."+str(id)+"."+str(imgId)+".jpg"
                        cv2.imwrite(filePath,face)
                        cv2.putText(face,str(imgId),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(imgId)==100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Gnenerating Data sets completed")

            except Exception as es:
                    messagebox.showerror("Error",f"Due To : {str(es)}", parent=self.root)




if __name__ == "__main__":

  root=Tk()  #call root  with toolkit
  obj=Student(root)  #make object of class and give the class name and pass root because we want to connect them
  root.mainloop() #close the main loop