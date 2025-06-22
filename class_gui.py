#canvas-only used to draw shapes
#create_line need to pass 4 arguments which are the points of two line
#in circle need to pass 3 arguments which are 2- the position of center in 2D and its radius
#in ellipse need to pass 4 arguments which are 2- the position of center in 2D and 2 for its minor and major axis
from tkinter import *
root=Tk()
w=Canvas(root,width=40,height=60)
w.pack()
x=20
y=30
w.create_line(0,x,20,y)
root.mainloop()


'''
#multi text box
from tkinter import *
root=Tk()
T=Text(root,height=2,width=30)
T.pack()
T.insert(END,"Hello Everyone\nMy name is I don't know\n")
root.mainloop()

#progress bar
import tkinter as tk
from tkinter import ttk
import time 
root=tk.Tk()
root.title("Progressbar example")
def start_progress():
    progress.start()
    for i in range(101):
        time.sleep(0.05)
        progress['value']=i
        root.update_idletasks()
    progress.stop()

progress=ttk.Progressbar(root,orient="horizontal",length=300,mode="determinate")
progress.pack(pady=20)
start_button=tk.Button(root,text="Start Progress",command=start_progress)
start_button.pack(pady=10)



root.mainloop()'''