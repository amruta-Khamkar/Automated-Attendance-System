from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #for insert images properly=> pillow
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1495x700+0+0")
      self.root.title("Face Recogintion System ")

      # varibales
      self.varFname=StringVar()
      self.varLname=StringVar()
      self.varContact=StringVar()
      self.varEmail=StringVar()
      self.varSecurityQ=StringVar()
      self.varSecurityA=StringVar()
      self.varPass=StringVar()
      self.varConfirmPass=StringVar()
  
        # background image
      img=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\nature2.jpg") 
      img=img.resize((1495,710), Image.ANTIALIAS) #convert high level image to low image
      self.photoImg=ImageTk.PhotoImage(img)
      firstLabel=Label(self.root,image=self.photoImg) #to set image on window
      firstLabel.place(x=0,y=0,width=1495,height=710)

        # left image
      img1=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\cup.jpg") 
      img1=img1.resize((470,550), Image.ANTIALIAS) #convert high level image to low image
      self.photoImg1=ImageTk.PhotoImage(img1)

      secondLabel=Label(self.root,image=self.photoImg1) #to set image on window
      secondLabel.place(x=50,y=80,width=470,height=550)

        # frame
      mainFrame=Frame(self.root,bd=2,bg="white")
      mainFrame.place(x=520,y=80,width=800, height=550)

      registerLabel=Label(mainFrame, text="REGISTER HERE", font=("times new roman", 20,"bold"),bg="white" ,fg="green")
      registerLabel.place(x=20,y=20)

        # label and entry 
      fnameLabel=Label(mainFrame, text="First Name", font=("times new roman", 15,"bold"),bg="white" ,fg="black")
      fnameLabel.place(x=50,y=100)

      self.fnameEntry=ttk.Entry(mainFrame,width=15,textvariable=self.varFname,font=("times new roman",15, "bold"))
      self.fnameEntry.place(x=50,y=130,width=250)
        
      lnameLabel=Label(mainFrame, text="Last Name", font=("times new roman", 15,"bold"),bg="white" ,fg="black")
      lnameLabel.place(x=370,y=100)

      self.lnameEntry=ttk.Entry(mainFrame,width=15,textvariable=self.varLname,font=("times new roman",15, "bold"))
      self.lnameEntry.place(x=370,y=130,width=250)

      contactLabel=Label(mainFrame, text="Contact No", font=("times new roman", 15,"bold"),bg="white" ,fg="black")
      contactLabel.place(x=50,y=170)

      self.contactEntry=ttk.Entry(mainFrame,width=15,textvariable=self.varContact,font=("times new roman",15, "bold"))
      self.contactEntry.place(x=50,y=200,width=250)

      emailLabel=Label(mainFrame, text="Email", font=("times new roman", 15,"bold"),bg="white" ,fg="black")
      emailLabel.place(x=370,y=170)

      self.emailEntry=ttk.Entry(mainFrame,width=15,textvariable=self.varEmail,font=("times new roman",15, "bold"))
      self.emailEntry.place(x=370,y=200,width=250)

      securityLabel=Label(mainFrame,text="Select Secuirty Question",font=("times new roman",15, "bold" ),bg="white")
      securityLabel.place(x=25,y=240,width=250)

      self.securityCombo=ttk.Combobox(mainFrame,textvariable=self.varSecurityQ,font=("times new roman",14, "bold" ),state="readonly",width=17)
      self.securityCombo["values"]=("Select","Who is your best friend","Whats your favourite animal","Your birth place")
      self.securityCombo.current(0)
      self.securityCombo.place(x=50,y=270,width=250)

      secAnsLabel=Label(mainFrame, text="Security Answer", font=("times new roman", 15,"bold"),bg="white" ,fg="black")
      secAnsLabel.place(x=370,y=240)

      self.secAnsEntry=ttk.Entry(mainFrame,textvariable=self.varSecurityA,width=15,font=("times new roman",15, "bold"))
      self.secAnsEntry.place(x=370,y=270,width=250 )

      passLabel=Label(mainFrame, text="Password", font=("times new roman", 15,"bold"),bg="white" ,fg="black")
      passLabel.place(x=50,y=310)

      self.passEntry=ttk.Entry(mainFrame,width=15,textvariable=self.varPass,font=("times new roman",15, "bold"))
      self.passEntry.place(x=50,y=340,width=250)

      confirmPassLabel=Label(mainFrame, text="Confirm Password", font=("times new roman", 15,"bold"),bg="white" ,fg="black")
      confirmPassLabel.place(x=370,y=310)

      self.confirmPassEntry=ttk.Entry(mainFrame,width=15,textvariable=self.varConfirmPass,font=("times new roman",15, "bold"))
      self.confirmPassEntry.place(x=370,y=340,width=250)

        # Checkbutton
      self.varCheck=IntVar()
      checkBtn=Checkbutton(mainFrame,text="I Agree with Terms & Conditions",variable=self.varCheck, font=("times new roman", 13,"bold"),bg="white" ,fg="black",onvalue=1,offvalue=0)
      checkBtn.place(x=50,y=380)

        # buttons
      img2=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\register.png") 
      img2=img2.resize((180,50), Image.ANTIALIAS) #convert high level image to low image
      self.photoImg2=ImageTk.PhotoImage(img2)

      button1=Button(mainFrame,image=self.photoImg2,command=self.registerData,borderwidth=0,cursor="hand2")
      button1.place(x=20,y=430,width=180,height=50)

      img3=Image.open(r"C:\Users\HP\Desktop\Major Project By Amruta\Images\loginB.png") 
      img3=img3.resize((180,50), Image.ANTIALIAS) #convert high level image to low image
      self.photoImg3=ImageTk.PhotoImage(img3)

      button1=Button(mainFrame,image=self.photoImg3,borderwidth=0,cursor="hand2")
      button1.place(x=300,y=430,width=180,height=50)

            # functions
    def registerData(self):
      if self.varFname.get()=="" or self.varEmail.get()=="" or self.varSecurityQ.get=="Select":
        messagebox.showerror("Error","All fields are required")

      elif self.varPass.get()!=self.varConfirmPass.get():
        messagebox.showerror("Error","Password and confirm password must be same")

      elif self.varCheck.get()==0:
        messagebox.showerror("Error","Please agree terms and conditions")

      else:
        conn=mysql.connector.connect(host="localhost", username="root",password="",database="face_recoginizer")           
        myCursor=conn.cursor()
        query=("select * from register where email=%s")
        value=(self.varEmail.get(),)
        myCursor.execute(query,value)
        row=myCursor.fetchone()
        if row!=None:
          messagebox.showerror("Error","This email is already registered")
        else:
          myCursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.varFname.get(),
                                                                                self.varLname.get(),
                                                                                self.varContact.get(),
                                                                                self.varEmail.get(),
                                                                                self.varSecurityQ.get(),
                                                                                self.varSecurityA.get(),
                                                                                self.varPass.get(),                                                                                                                                                               
                                                                          ))
          conn.commit()
          conn.close()
          messagebox.showinfo("Success", "Student Details Has been Added Successfully",parent=self.root)
          
if __name__ == "__main__":

  root=Tk()  #call root  with toolkit
  obj=Register(root)  #make object of class and give the class name and pass root because we want to connect them
  root.mainloop() #close the main loop