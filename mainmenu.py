import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recogin import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("face Recognition System")
        
        #bg image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\backg.jpg")
        img=img.resize((1550,800),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1550,height=800)

        title_lb1=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lb1.place(x=0,y=5,width=1550,height=45)

        #student button

        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\details.jpg")
        img1=img1.resize((220,220),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        b1=Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",25,"bold"),bg="blue",fg="white")
        b1_1.place(x=100,y=300,width=220,height=40)

        #detect face button

        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\facee.webp")
        img2=img2.resize((220,220),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        b1=Button(bg_img,image=self.photoimg2,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",25,"bold"),bg="blue",fg="white")
        b1_1.place(x=450,y=300,width=220,height=40)

        #Attendance button

        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\attendance.jpg")
        img3=img3.resize((220,220),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        b1=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.attendance)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",25,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #help desk button

        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\support.webp")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.help_desk)
        b1.place(x=1150,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Support Desk",cursor="hand2",command=self.help_desk,font=("times new roman",25,"bold"),bg="blue",fg="white")
        b1_1.place(x=1150,y=300,width=220,height=40)

        #photos face button
        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\cam.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.open_image)
        b1.place(x=100,y=450,width=220,height=220)

        b1_1=Button(bg_img,text="photos",cursor="hand2",command=self.open_image,font=("times new roman",25,"bold"),bg="blue",fg="white")
        b1_1.place(x=100,y=650,width=220,height=40)
        
        #train face button

        img6=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\trainn.webp")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)


        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.train_data)
        b1.place(x=800,y=450,width=220,height=220)

        b1_1=Button(bg_img,text="train data",cursor="hand2",command=self.train_data,font=("times new roman",25,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=650,width=220,height=40)

        #developer button

        img7=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\dev.png")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.dev_data)
        b1.place(x=450,y=450,width=220,height=220)

        b1_1=Button(bg_img,text="developer",cursor="hand2",command=self.dev_data,font=("times new roman",25,"bold"),bg="blue",fg="white")
        b1_1.place(x=450,y=650,width=220,height=40)
        
        #exit button

        img8=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\exitt.webp")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.exit)
        b1.place(x=1150,y=450,width=220,height=220)

        b1_1=Button(bg_img,text="exit",cursor="hand2",command=self.exit,font=("times new roman",25,"bold"),bg="blue",fg="white")
        b1_1.place(x=1150,y=650,width=220,height=40)

      
    def open_image(self):
        os.startfile("data")

    #===================functions buttons============================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window) 

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)  

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 

    def dev_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    def exit(self):
        self.Exit=messagebox.askyesno("Face Recognition","Are you sure you want to exit?")
        if self.Exit>0:
            self.root.destroy()
        else:
            return 

    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window) 

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()