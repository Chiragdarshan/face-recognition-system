from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")

        # Load and Display First Image
        img1 = Image.open(r"images\page 1.WEBP")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Load and Display Second Image
        img2 = Image.open(r"images\photo 2.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Load and Display Third Image
        img3 = Image.open(r"images\photo 3.jpeg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=500, height=130)

        # Load and Display Background Image
        img4 = Image.open(r"images\bgimage.jpeg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)  # ✅ Correct image stored

        bg_img = Label(self.root, image=self.photoimg4)  # ✅ Correct image assigned
        bg_img.place(x=0, y=130, width=1530, height=710) 
         # ✅ Correct background size


        title_lbl=Label(bg_img,text="SMART ATTENDENCE SYSTEM USING FACIAL RECOGNITION",font=("times new roman",24,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=50)

        #student button
        img5 = Image.open(r"images\students.jpeg")
        img5 = img5.resize((180, 180), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)  # ✅ Correct image stored

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=200,width=180,height=40)


        #detect face  button
        img6 = Image.open(r"images\face detector.jpeg")
        img6 = img6.resize((180, 180), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)  # ✅ Correct image stored

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Face Dectector",cursor="hand2",command=self.face_data,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=200,width=180,height=40)


        #Attendence button
        img7 = Image.open(r"images\attendence.jpeg")
        img7 = img7.resize((180, 180), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)  # ✅ Correct image stored

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=700,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=200,width=180,height=40)

         #help desk button

        img8 = Image.open(r"images\help.jpeg")
        img8 = img8.resize((180, 180), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)  # ✅ Correct image stored

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1000,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=200,width=180,height=40)


        # train button

        img9 = Image.open(r"images\train.jpeg")
        img9 = img9.resize((180, 180), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)  # ✅ Correct image stored

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=300,width=180,height=180)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=450,width=180,height=40)

         # photos button

        img10 = Image.open(r"images\photos.jpeg")
        img10 = img10.resize((180, 180), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)  # ✅ Correct image stored

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=180,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=450,width=180,height=40)


         # developer button

        img11 = Image.open(r"images\developer.jpeg")
        img11 = img11.resize((180, 180), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)  # ✅ Correct image stored

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=700,y=300,width=180,height=180)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=450,width=180,height=40)


        # exit button

        img12 = Image.open(r"images\exit.jpeg")
        img12 = img12.resize((180, 180), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)  # ✅ Correct image stored

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b1.place(x=1000,y=300,width=180,height=180)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=450,width=180,height=40)
        
    def open_img(self):
        os.startfile("data")
        
       
       
       
        #function buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)









if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
