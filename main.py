from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from mainmenu import Face_Recognition_System
import os
import mysql.connector

class Face_Recognition_Systemm:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        #bg image

        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\face.jpg")
        img=img.resize((1550,800),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1550,height=800)


        b1=Button(bg_img,text="OPEN MAIN MENU",cursor="hand2",command=self.main_menu,font=("times new roman",35,"bold"),bg="blue",fg="white")
        b1.place(x=200,y=700,width=500,height=50)
 
    def main_menu(self):
        self.root.withdraw()
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)

if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_Systemm(root)
    root.mainloop()