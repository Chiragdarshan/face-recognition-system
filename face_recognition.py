from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=35)

        # 1st image
        img_top = Image.open(r"images\face recog.jpg")
        img_top = img_top.resize((650, 710), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl1 = Label(self.root, image=self.photoimg_top)
        f_lbl1.place(x=0, y=45, width=650, height=710)

        # 2nd image
        img_bottom = Image.open(r"images\face recog 2.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=650, y=45, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl2, text="FACE RECOGNITION", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=370, y=600, width=200, height=40)

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Chirag@2004", database="chirudb")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("SELECT Roll_No FROM student WHERE Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT Department FROM student WHERE Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                if confidence > 77:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                    cv2.putText(img, f"Roll No: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Dept: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break
            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
