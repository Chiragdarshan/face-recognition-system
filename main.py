from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer

# ---------------------- Main Face Recognition System ---------------------
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")

        # Load and Display Header Images
        self.set_images()
        self.set_buttons()

    def set_images(self):
        img1 = Image.open(r"images\page 1.WEBP").resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"images\photo 2.jpeg").resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=500, y=0, width=500, height=130)

        img3 = Image.open(r"images\photo 3.jpeg").resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=500, height=130)

        img4 = Image.open(r"images\bgimage.jpeg").resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        self.bg_img = Label(self.root, image=self.photoimg4)
        self.bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(self.bg_img, text="SMART ATTENDENCE SYSTEM USING FACIAL RECOGNITION", font=("times new roman",24,"bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=50)

    def set_buttons(self):
        btn_data = [
            ("students.jpeg", "Student Details", self.student_details, 100, 50),
            ("face detector.jpeg", "Face Detector", self.face_data, 400, 50),
            ("attendence.jpeg", "Attendance", self.attendence_data, 700, 50),
            ("help.jpeg", "Help Desk", None, 1000, 50),
            ("train.jpeg", "Train Data", self.train_data, 100, 300),
            ("photos.jpeg", "Photos", self.open_img, 400, 300),
            ("developer.jpeg", "Developer", self.developer_data, 700, 300),
            ("exit.jpeg", "Exit", self.iExit, 1000, 300)
        ]

        for img_name, label, cmd, x, y in btn_data:
            img = Image.open(f"images\\{img_name}").resize((180, 180), Image.LANCZOS)
            photoimg = ImageTk.PhotoImage(img)
            Button(self.bg_img, image=photoimg, command=cmd, cursor="hand2").place(x=x, y=y, width=180, height=180)
            Button(self.bg_img, text=label, command=cmd, font=("times new roman",18,"bold"), bg="darkblue", fg="white", cursor="hand2").place(x=x, y=y+150, width=180, height=40)
            setattr(self, f"photo_{img_name}", photoimg)  # To prevent garbage collection

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        exit_confirm = messagebox.askyesno("Face Recognition System", "Are you sure you want to exit?", parent=self.root)
        if exit_confirm:
            self.root.destroy()

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)


# ---------------------- Start Everything ---------------------
def run_main_app():
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


# ---------------------- Start Application ---------------------
if __name__ == "__main__":
    run_main_app()
