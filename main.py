from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from train import Train
from detection import Detection
from attendance import Attendance
from developer import Developer
from help import Help




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
     
        img0=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (9).jpeg")
        img0=img0.resize((500,130),Image.LANCZOS)
    
        self.photoimg0=ImageTk.PhotoImage(img0)

        f_lbl=Label(self.root,image=self.photoimg0)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (4).jpeg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img2=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47.jpeg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        img3=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-23 at 01.16.54.jpeg")
        img3=img3.resize((1530,790),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM ",font=("times new roman",35,"bold"), bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        def time():
            string=strftime("%H:%M:%S")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",18,"bold"), bg="white",fg="black")
        lbl.place(x=0,y=0,width=110,height=45)
        time()
    

        img4=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (1).jpeg")
        img4=img4.resize((200,180),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=180)

        b1=Button(bg_img,text="STUDENTS DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",13,"bold"), bg="dark blue",fg="white")
        b1.place(x=200,y=280,width=200,height=35)

        img5=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (11).jpeg")
        img5=img5.resize((200,180),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.detect_data)
        b1.place(x=500,y=100,width=200,height=180)

        b1=Button(bg_img,text="FACE RECOGNIZER",cursor="hand2",command=self.detect_data,font=("times new roman",13,"bold"), bg="dark blue",fg="white")
        b1.place(x=500,y=280,width=200,height=35)


        img6=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (2).jpeg")
        img6=img6.resize((200,180),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=200,height=180)

        b1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("times new roman",13,"bold"), bg="dark blue",fg="white")
        b1.place(x=800,y=280,width=200,height=35)
         
        img7=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (3).jpeg")
        img7=img7.resize((200,180),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_desk_data)
        b1.place(x=1100,y=100,width=200,height=180)

        b1=Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_desk_data,font=("times new roman",13,"bold"), bg="dark blue",fg="white")
        b1.place(x=1100,y=280,width=200,height=35)


        img8=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (4).jpeg")
        img8=img8.resize((200,180),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=340,width=200,height=180)

        b1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",13,"bold"), bg="dark blue",fg="white")
        b1.place(x=200,y=520,width=200,height=35)

        img9=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (5).jpeg")
        img9=img9.resize((200,180),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=340,width=200,height=180)

        b1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",13,"bold"), bg="dark blue",fg="white")
        b1.place(x=500,y=520,width=200,height=35)

        img10=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (6).jpeg")
        img10=img10.resize((200,180),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=340,width=200,height=180)

        b1=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("times new roman",13,"bold"), bg="dark blue",fg="white")
        b1.place(x=800,y=520,width=200,height=35)

        img11=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-14 at 01.14.47 (7).jpeg")
        img11=img11.resize((200,180),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExist)
        b1.place(x=1100,y=340,width=200,height=180)

        b1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExist,font=("times new roman",13,"bold"), bg="dark blue",fg="white")
        b1.place(x=1100,y=520,width=200,height=35)

    def open_img(self):
        os.startfile("data")

    def iExist(self):
        self.iExist=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exist this system",parent=self.root)
        if self.iExist>0:
           self.root.destroy()
        else:
            return       

    def student_details(self):
        self.new_window=Toplevel(self.root) 
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Train(self.new_window)

    def detect_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Detection(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Developer(self.new_window)



    def help_desk_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Help(self.new_window)






 
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
     
