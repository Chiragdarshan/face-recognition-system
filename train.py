from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=35)
        
        img_top = Image.open(r"images\train 1.jpg")
        img_top = img_top.resize((1530,280), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=55, width=1530, height=280)
        
        # BUTTON
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifer,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=335,width=1530,height=40)

        
        
        img_bottom = Image.open(r"images\people 2.jpg")
        img_bottom = img_bottom.resize((1530,300), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl3 = Label(self.root, image=self.photoimg_bottom)
        f_lbl3.place(x=0, y=380, width=1530, height=300)
        
    def train_classifer(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        for image in path:
            img=Image.open(image).convert('L')  # GREYSCALE IMAGE  
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        # TRAIN THE CLASSIFIER and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed successfully")
            
            
          
        
        
        









if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()        
