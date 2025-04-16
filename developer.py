from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")
        
        
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=35)
        
        img_top = Image.open(r"images\dev.jpg")
        img_top = img_top.resize((1530,720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=55, width=1530, height=720)
        
        #------------frame
        main_frame = Frame(f_lbl3, bd=2,)
        main_frame.place(x=800, y=0, width=450, height=600)
        
        
        img_top1 = Image.open(r"images\dev.jpg")
        img_top1 = img_top1.resize((200,200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl3 = Label(main_frame, image=self.photoimg_top1)
        f_lbl3.place(x=300, y=0, width=200, height=200)
        
        #---------Developer info
        dev_label=Label(main_frame,text="HELLO MY NAME IS CHIRAG DARSHAN BA ",font=("times new roman",10,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        
        




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
        