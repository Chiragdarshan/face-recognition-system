from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
from tkinter import filedialog
import csv

mydata=[]
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")
        
        #---------------variables----------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()
        
#Load and Display First Image
        img1 = Image.open(r"images\page 1.WEBP")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=750, height=200)

        # Load and Display Second Image
        img2 = Image.open(r"images\photo 2.jpeg")
        img2 = img2.resize((800, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=800, y=0, width=750, height=200)
        
#-------------bg imaGE       
        img4 = Image.open(r"images\bgimage.jpeg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)  # ✅ Correct image stored

        bg_img = Label(self.root, image=self.photoimg4)  # ✅ Correct image assigned
        bg_img.place(x=0, y=130, width=1530, height=800) 
         # ✅ Correct background size
         
         
        title_lbl=Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=30)
        
        main_frame = Frame(bg_img, bd=2,)
        main_frame.place(x=0, y=30, width=1400, height=600)
        
         #left label frame 
        left_frame =  LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="STUDENT ATTENDENCE DETAILS", font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=580)
        
        img_left = Image.open(r"images\students.jpeg")
        img_left = img_left.resize((800, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl3 = Label(left_frame, image=self.photoimg_left)
        f_lbl3.place(x=5, y=0, width=580, height=110)
        
        left_inside_frame = Frame(left_frame, bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=1, y=115, width=585, height=350)
        
        #---------labels and entry
        # Attendence id
        attendenceId_label=Label(left_inside_frame,text="Attendence ID:",font=("times new roman",12,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=10,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
         # Name
        name_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=4,sticky=W)

        atten_name_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name_entry.grid(row=0,column=3,pady=8,sticky=W)
        
         # roll no
        roll_label=Label(left_inside_frame,text="NAME:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=4,sticky=W)

        atten_roll_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll_entry.grid(row=1,column=1,pady=8,sticky=W)
        
         # department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=4,sticky=W)

        atten_dep_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep_entry.grid(row=1,column=3,pady=8,sticky=W)
        
         #  time
        time_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=4,sticky=W)

        atten_time_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time_entry.grid(row=2,column=1,pady=8,sticky=W)
        
         # DATE
        date_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=4,sticky=W)

        atten_date_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date_entry.grid(row=2,column=3,pady=8,sticky=W)
        
         # Name
        attendence_label=Label(left_inside_frame,text="ATTENDENCE STATUS:",font=("times new roman",12,"bold"),bg="white")
        attendence_label.grid(row=3,column=0,padx=4,sticky=W)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=15,textvariable=self.var_atten_attendence,font=("times new roman" ,12, "bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8,sticky=W)
        self.atten_status.current(0)
        
        # button frame
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=315,width=600,height=30)

        save_btn=Button(btn_frame,text="IMPORT CSV",command=self.importCsv,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="EXPORT CSV",command=self.exportCsv,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="UPDATE",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        
        #---------right label frame
        
        Right_frame =  LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Attendence Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=0,width=610,height=580)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=600,height=500)
        
        
        #-----------------scroll bar table-------------------#
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendenceReportTable=ttk.Treeview(table_frame,columns=("id","name","roll","department","time","date","status","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        
        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll NO")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")
    
        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column('id', width=100)
        self.AttendenceReportTable.column('roll', width=100)
        self.AttendenceReportTable.column('name', width=100)
        self.AttendenceReportTable.column('department', width=100)
        self.AttendenceReportTable.column('time', width=100)
        self.AttendenceReportTable.column('date', width=100)
        self.AttendenceReportTable.column('attendence', width=100)
    
      
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        #------------------fetch data-------------------#
        
    def fetch_data(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)  
            
     # import csv       
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread= csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)    
            
    # EXPORT CSV
    
    def exportCsv(self):
      try:
        if len(mydata)<1:
            messagebox.showerror("No Data", "No data found to export", parent=self.root)
            return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),parent=self.root)
        with open(fln, mode="w", newline="")as myfile:
            exp_write=csv.writer(myfile, delimiter=",")
            for i in mydata:
                exp_write.writerow(i)
            messagebox.showinfo("Data Export", "Your data exported to "+os.path.basename(fln)+" Successfully")
      except Exception as es:
          messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)
          
          
    def get_cursor(self,event=""):
        cursor_rows=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_rows)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])    
                 
                 
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")    
        
        






























if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()    