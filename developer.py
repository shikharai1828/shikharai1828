from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x720+0+0")
        self.root.title("face recognition system")

        
        title_lbl=Label(self.root,text="DEVELOPER DETAILS ",font=("times new roman",35,"bold"), bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1350,height=48)

        img_top=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2024-01-17 at 04.02.10.jpeg")
        img_top=img_top.resize((800,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=800,height=700)

        title_lbl=Label(f_lbl,text="I am Shikha Rai,a second year engineering student.",font=("times new roman",18,"bold"), bg="black",fg="white")
        title_lbl.place(x=0,y=0)

        title_lbl=Label(f_lbl,text="I belongs to Buxar -Bihar.",font=("times new roman",18,"bold"), bg="black",fg="white")
        title_lbl.place(x=0,y=40)

        title_lbl=Label(f_lbl,text="I have completed my 10th and 12th from Bihar public school (Buxar).",font=("times new roman",18,"bold"), bg="black",fg="white")
        title_lbl.place(x=0,y=80)

        title_lbl=Label(f_lbl,text="And currently pursuing Btech from iimt group of engineering(Greater Noida).",font=("times new roman",18,"bold"), bg="black",fg="white")
        title_lbl.place(x=0,y=120)

        title_lbl=Label(f_lbl,text="I have developed this software as  mini project for my course.",font=("times new roman",18,"bold"), bg="black",fg="white")
        title_lbl.place(x=0,y=160)

        title_lbl=Label(f_lbl,text="I know the basics of c language and currently learning python.",font=("times new roman",18,"bold"), bg="black",fg="white")
        title_lbl.place(x=0,y=200)








        img_bottom=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2024-01-17 at 03.58.26.jpeg")
        img_bottom=img_bottom.resize((550,700),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl1=Label(self.root,image=self.photoimg_bottom)
        f_lbl1.place(x=800,y=50,width=550,height=700)








if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        