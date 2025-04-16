from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import mysql.connector
from datetime import datetime
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=35)

        # 1st image
        img_top = Image.open(r"images/face recog.jpg")
        img_top = img_top.resize((650, 710), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl1 = Label(self.root, image=self.photoimg_top)
        f_lbl1.place(x=0, y=45, width=650, height=710)

        # 2nd image
        img_bottom = Image.open(r"images/face recog 3.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=650, y=45, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl2, text="FACE RECOGNITION", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=150, y=300, width=200, height=30)

    def mark_attendance(self, i, n, r, d):
        file_path = "chirag_attendance.csv"
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("ID,Name,Roll,Department,Date,Time,Status\n")

        with open(file_path, "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]
            if str(i) not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{i},{n},{r},{d},{d1},{dtString},Present\n")
                return True
        return False

    def face_recog(self):
        attendance_marked = False
        recognized_ids = set()  # ✅ Track attendance per session

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            nonlocal attendance_marked
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            for (x, y, w, h) in features:
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                if confidence > 77:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Chirag@2004",
                        database="chirudb"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT Student_id, Name, Roll_No, Department FROM student WHERE Student_id=" + str(id))
                    result = my_cursor.fetchone()
                    conn.close()

                    if result:
                        i, n, r, d = result
                        i, n, r, d = str(i), str(n), str(r), str(d)

                        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                        cv2.putText(img, f"ID: {i}", (x, y - 90), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2)
                        cv2.putText(img, f"Roll: {r}", (x, y - 65), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2)
                        cv2.putText(img, f"Name: {n}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2)
                        cv2.putText(img, f"Dept: {d}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2)

                        if i not in recognized_ids:
                            recognized_ids.add(i)
                            if not attendance_marked:
                                attendance_marked = self.mark_attendance(i, n, r, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13 or cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break

        video_cap.release()
        cv2.destroyAllWindows()

        if attendance_marked:
            messagebox.showinfo("Attendance", "Attendance Marked Successfully!")
        else:
            messagebox.showinfo("Info", "No known face detected or attendance already marked.")

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
