from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\developerr.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=500,y=0,width=500,height=600)

        bg_img=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\bg.png")
        bg_image=bg_img.resize((500,600),Image.LANCZOS)
        self.bg_photo=ImageTk.PhotoImage(bg_img)

        bg_label=Label(main_frame,image=self.bg_photo)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        #Developer iNFO
        dev_label=Label(main_frame,text="Hello\nI am a developer\n Learning about more languages and     \nbuilding projects.",font=("times new roman",20,"bold"))
        dev_label.place(x=13,y=0)


if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()