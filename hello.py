import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Mukti@123",database="project")
cursor=con.cursor()
query2="show tables;"
cursor.execute(query2)
data=cursor.fetchall()
con.close()

print("hello")

'''img_top1=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\social_media_.jpg")
        img_top1=img_top1.resize((1530,720),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)'''

img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\social_media_.jpg")
        img2=img2.resize((500,390),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=200,height=390)