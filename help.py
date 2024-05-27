from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x720+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="HELP DESK ",font=("times new roman",45,"bold"), bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1355,height=48)

        img_top=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2024-01-17 at 02.59.59.jpeg")
        img_top=img_top.resize((1355,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=48,width=1355,height=700)

        title_lbl=Label(f_lbl,text="Email:shikha9110913902@gmail.com ",font=("times new roman",18,"bold"), bg="white",fg="black")
        title_lbl.place(x=500,y=280)










if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()        