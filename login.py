from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import sys
import os

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        # Background Image
        self.bg = Image.open(r"images\login.jpg")
        self.bg = self.bg.resize((1530, 790), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg)
        bg_lbl = Label(self.root, image=self.bg_img)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=600, y=200, width=350, height=400)

        title = Label(frame, text="Admin Login", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title.place(x=90, y=30)

        # Username
        lbl_user = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white")
        lbl_user.place(x=30, y=100)
        self.txtuser = Entry(frame, font=("times new roman", 15), bg="lightgray")
        self.txtuser.place(x=30, y=130, width=270)

        # Password
        lbl_pass = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        lbl_pass.place(x=30, y=180)
        self.txtpass = Entry(frame, font=("times new roman", 15), show="*", bg="lightgray")
        self.txtpass.place(x=30, y=210, width=270)

        # Login Button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, bg="green", fg="white", activebackground="darkgreen")
        loginbtn.place(x=110, y=270, width=120, height=40)

    def login(self):
        user = self.txtuser.get()
        password = self.txtpass.get()

        if user == "chirag" and password == "1234":
            messagebox.showinfo("Success", "Login Successful")

            # 🔁 Redirect to main.py
            self.root.destroy()
            subprocess.Popen([sys.executable, "main.py"])
        else:
            messagebox.showerror("Error", "Invalid Username or Password")


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
