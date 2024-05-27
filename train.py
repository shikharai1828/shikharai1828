from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x720+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="TRAIN DATA SET ",font=("times new roman",35,"bold"), bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1350,height=48)
        
        img_top=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2024-01-13 at 02.18.43 (1).jpeg")
        img_top=img_top.resize((1350,325),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1350,height=315)

        b1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"), bg="dark blue",fg="white")
        b1.place(x=0,y=360,width=1350,height=40)

        img_bottom=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2024-01-13 at 02.55.08.jpeg")
        img_bottom=img_bottom.resize((1350,325),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=400,width=1350,height=315)
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed successfully",parent=self.root)

        

        


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
            