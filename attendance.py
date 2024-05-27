from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x720+0+0")
        self.root.title("face recognition system")

        #===========Variables==============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        

        img0=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2024-01-16 at 02.47.48 (1).jpeg")
        img0=img0.resize((680,180),Image.LANCZOS)
    
        self.photoimg0=ImageTk.PhotoImage(img0)

        f_lbl=Label(self.root,image=self.photoimg0)
        f_lbl.place(x=0,y=0,width=680,height=180)

        img1=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2024-01-16 at 02.47.48.jpeg")
        img1=img1.resize((680,180),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=680,y=0,width=680,height=180)

        img3=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-23 at 01.16.54.jpeg")
        img3=img3.resize((1530,790),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=180,width=1530,height=790)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman",30,"bold"), bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1355,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=40,width=1345,height=600)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Left_frame.place(x=15,y=5,width=650,height=520)

        left_img=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2024-01-16 at 02.47.47.jpeg")
        left_img=left_img.resize((640,150),Image.LANCZOS)
        self.photoleft_img=ImageTk.PhotoImage(left_img)

        f_lbl=Label(Left_frame,image=self.photoleft_img)
        f_lbl.place(x=5,y=0,width=655,height=150)

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
        class_student_frame.place(x=5,y=155,width=700,height=295)

        studentID_label=Label(class_student_frame,text="Student Id:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Student name:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Attendance:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,font=("times new roman",12,"bold"),width=18,textvariable=self.var_atten_attendance,state="readonly")
        div_combo["values"]=("Attendance status","Present","Absent")
        div_combo.current(0)
        div_combo.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=715,height=70)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        save_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1)

        save_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=2)

        save_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=3)


        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=675,y=5,width=650,height=520)

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=0,width=650,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("department",text="Department")
        self.student_table.heading("time",text="Time")
        self.student_table.heading("date",text="Date")
        self.student_table.heading("attendance",text="Attendance")
        self.student_table["show"]="headings"

        self.student_table.column("id",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("department",width=100)
        self.student_table.column("time",width=100)
        self.student_table.column("date",width=100)
        self.student_table.column("attendance",width=100)

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
           self.student_table.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
              mydata.append(i)
            self.fetchData(mydata) 

    def exportCSV(self):
        try:
           if len(mydata)<1:
               messagebox.showerror("No Data","No Data found to export",parent=self.root)
               return False
           fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
           with open(fln,mode="w",newline="") as myfile:
             exp_write=csv.writer(myfile,delimiter=",")
             for i in mydata:
               exp_write.writerow(i)
             messagebox.showinfo("Data Export","Your Data is exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)            
        
    def get_cursor(self,event=""):
      cursor_row=self.student_table.focus()
      content=self.student_table.item(cursor_row)
      rows=content['values']
      self.var_atten_id.set(rows[0])
      self.var_atten_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendance.set(rows[6])  
  
  
    def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")  
  
  
  
  
  




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()        