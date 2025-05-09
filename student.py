from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import tkinter as tk
from flask import Flask, render_template, request, redirect, url_for, flash
import webbrowser
import subprocess
import sys
import os
from multiprocessing import Process
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Automatically open browser
def open_browser():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'chirag' and password == '1234':
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/launch', methods=['POST'])
def launch_app():
    try:
        # Launch main.py as a separate process (Tkinter GUI)
        subprocess.Popen([sys.executable, os.path.join(os.getcwd(), "main.py")])
        flash("Attendance system launched!", "success")
    except Exception as e:
        flash(f"Error launching: {e}", "danger")
    return redirect(url_for('home'))

if __name__ == '__main__':
    Process(target=open_browser).start()
    app.run(debug=True, use_reloader=False)



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")

        #=========variables==============
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_photo=StringVar()




# Load and Display First Image
        img1 = Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM\images\page 1.WEBP")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Load and Display Second Image
        img2 = Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM\images\photo 2.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Load and Display Third Image
        img3 = Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM\images\photo 3.jpeg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=500, height=130)



        # Load and Display Background Image
        img4 = Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM\images\bgimage.jpeg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)  # ✅ Correct image stored

        bg_img = Label(self.root, image=self.photoimg4)  # ✅ Correct image assigned
        bg_img.place(x=0, y=130, width=1530, height=800) 
         # ✅ Correct background size


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=30)

        main_frame = Frame(bg_img, bd=2,)
        main_frame.place(x=0, y=30, width=1400, height=600)

        #left label frame 
        left_frame =  LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=580)

        img_left = Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM\images\students.jpeg")
        img_left = img_left.resize((800, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl3 = Label(left_frame, image=self.photoimg_left)
        f_lbl3.place(x=5, y=0, width=580, height=110)

        #current course
        current_course_frame =  LabelFrame(left_frame, bd=2,bg="white", relief=RIDGE, text="CURRENT COURSE INFORMATION", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=115,width=580,height=120)


        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_department,font=("times new roman",12,"bold"),state = "readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science","Physical Science","Commerece","Management","LAW")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state = "readonly",width=20)
        course_combo["values"]=("Select Course","BCA","BSC","B.COM","BBA","LLB")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #YEAR
        year_label=Label(current_course_frame,text="YEAR",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state = "readonly",width=20)
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester

        semester_label=Label(current_course_frame,text="SEMESTER",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state = "readonly",width=20)
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class student information
        class_student_frame =  LabelFrame(left_frame, bd=2,bg="white", relief=RIDGE, text="CLASS STUDENT INFORMATION", font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=220,width=580,height=350)

        # student id
        studentId_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=15,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name

        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=15,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division

        #class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        #class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no

        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #gender

        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state = "readonly",width=10)
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=6,pady=10,sticky=W)

        #dob

        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Email

        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #phone no

        phone_label=Label(class_student_frame,text="Phone NO:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #address

        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",12,"bold"))
        address_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Radiobutton

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6,column=0,padx=10,pady=5,sticky=W)

        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No Photo Sample", value="N0")
        radiobtn2.grid(row=6,column=1,padx=10,pady=5,sticky=W)
        
        # button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=600,height=30)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=210,width=600,height=30)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=32,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


         #right label frame 
        Right_frame =  LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=0,width=610,height=580)

        img_right = Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM\images\students2.jpeg")
        img_right = img_right.resize((800, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl3 = Label(Right_frame, image=self.photoimg_right)
        f_lbl3.place(x=5, y=0, width=580, height=110)


        # ======= Search System ============
        Search_frame =  LabelFrame(Right_frame, bd=2,bg="white", relief=RIDGE, text="Search system", font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=120,width=600,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state = "readonly",width=12)
        search_combo["values"]=("Select ","roll_no","Phone_no",)
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)


        ShowAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)


        # table frame
        table_frame = Frame(Right_frame, bd=2,bg="white", relief=RIDGE) # text="Search system", font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=180,width=600,height=300)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("department","course","year","sem","id","name","roll","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone Number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()







#============function====================
    def add_data(self):
        if self.var_department.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="Localhost",
                    port=3306,
                    user="root",              
                    password="Chirag@2004",   
                    database="chirudb"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student (department, course, year, semester, student_id, name, roll_no, gender, dob, email, phone, address, photo_sample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

    #################fetch###############

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Chirag@2004",database="chirudb")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from Student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

#======== get cursor

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_department.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])
        self.var_radio1.set(data[12])

#========update function ===========

    def update_data(self):
        if self.var_department.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)  
                if update > 0:
                    conn = mysql.connector.connect(
                        host="Localhost",
                        port=3306,
                        username="root",
                        password="Chirag@2004",
                        database="chirudb"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("""UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, photo_sample=%s WHERE Student_id=%s
""", (
    self.var_department.get(),
    self.var_course.get(),
    self.var_year.get(),
    self.var_sem.get(),
    self.var_name.get(),
    self.var_roll.get(),
    self.var_gender.get(),
    self.var_dob.get(),
    self.var_email.get(),
    self.var_phone.get(),
    self.var_address.get(),
    self.var_radio1.get(),
    self.var_id.get()
))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details update completed", parent=self.root)
                else:
                    if not update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                
# delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("error","Student id must br required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root) 
                if delete>0: 
                    conn = mysql.connector.connect(
                        host="Localhost",
                        port=3306,
                        username="root",
                        password="Chirag@2004",
                        database="chirudb"
                    )                  
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)   
                
# Reset Function
    def reset_data(self):
        self.var_department.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("") 
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("") 
        

#================== Generate Data set and take a sample

    def generate_dataset(self):
     if self.var_department.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
     else:
        try:
            student_id = self.var_id.get()  # ✅ Define student_id properly

            conn = mysql.connector.connect(
                host="Localhost",
                port=3306,
                username="root",
                password="Chirag@2004",
                database="chirudb"
            )
            my_cursor = conn.cursor()

            my_cursor.execute("""UPDATE student SET 
                Department=%s, Course=%s, Year=%s, Semester=%s, 
                Name=%s, Roll_No=%s, Gender=%s, DOB=%s, 
                Email=%s, Phone=%s, Address=%s, photo_sample=%s 
                WHERE Student_id=%s""", (
                self.var_department.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_name.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_radio1.get(),
                student_id  # ✅ Corrected usage
            ))

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # Load pre-defined data on face frontals from OpenCV
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face_cropped = img[y:y + h, x:x + w]
                    return face_cropped

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if ret and face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "DATA/user." + str(student_id) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating data sets completed!!!!")

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    
    
    def is_running_in_docker():
        path='/proc/self/cgroup'
        if os.path.exists('/.dockerenv'):
            return True
        if os.path.isfile(path):
            with open(path) as f:
                return 'docker' in f.read()
            return False
        
     
                            

import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()






      