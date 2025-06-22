from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import cv2
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")


        title_lb1=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #bg image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\face_ai.jpg")
        img=img.resize((1550,800),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1550,height=800)

        b1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b1.place(x=490,y=620,width=200,height=40)


    #=========================attendance================================

    def mark_attendance(self,i,r,n,d):
        with open("Mukti.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


     #===================face recognition=========================
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                #print(f"[DEBUG] Predicted ID:{id}, Confidence: {confidence}")

                conn=mysql.connector.connect(host="localhost",user="root",password="Mukti@123",database="project")
                my_cursor=conn.cursor()

                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i=my_cursor.fetchone()
                if isinstance(i,(list,tuple)):
                    i=''.join(i)
                else:
                    i=str(i)
                #if i:i=str(i[0])
                
                my_cursor.execute("select Name from student where Student_Id="+str(id))
                n=my_cursor.fetchone()
                if isinstance(n,(list,tuple)):
                    n=''.join(n)
                else:
                    n=str(n)
                #if n:n=str(n[0])

                my_cursor.execute("select Roll_No from student where Student_Id="+str(id))
                r=my_cursor.fetchone()
                if isinstance(r,(list,tuple)):
                    r=''.join(r)
                else:
                    r=str(r)
                #if r:r=str(r[0])
                    
                my_cursor.execute("select Dep from student where Student_Id="+str(id))
                d=my_cursor.fetchone()
                if isinstance(d,(list,tuple)):
                    d=''.join(d)
                else:
                    d=str(d)
                #if d:d=str(d[0])

                if confidence>77:
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        '''if not video_cap.isOpened():
            print("Error: Could not open webcam.")
            messagebox.showerror("Webcam Error", "Failed to access webcam.")
            return'''

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()