from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x720+0+0")
        self.root.title("face recognition system")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_rollno=StringVar()
        self.var_address=StringVar()
        self.var_phone=StringVar()
        self.var_class=StringVar()
        self.var_teacher=StringVar()
        self.var_email=StringVar()
        self.var_radiobtn1=StringVar()
        


        img0=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-24 at 22.53.25.jpeg")
        img0=img0.resize((500,130),Image.LANCZOS)
    
        self.photoimg0=ImageTk.PhotoImage(img0)

        f_lbl=Label(self.root,image=self.photoimg0)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-24 at 22.53.24.jpeg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img2=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-24 at 22.53.25 (1).jpeg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        img3=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-23 at 01.16.54.jpeg")
        img3=img3.resize((1530,790),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM ",font=("times new roman",30,"bold"), bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=40,width=1345,height=600)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=15,y=5,width=650,height=520)

        left_img=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-25 at 02.40.07.jpeg")
        left_img=left_img.resize((640,120),Image.LANCZOS)
        self.photoleft_img=ImageTk.PhotoImage(left_img)

        f_lbl=Label(Left_frame,image=self.photoleft_img)
        f_lbl.place(x=5,y=0,width=655,height=120)

        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
        current_course_frame.place(x=25,y=140,width=640,height=120) 

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",11,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","ECE","CSE","IT","Mechanical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        dep_label=Label(current_course_frame,text="Course",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=0,column=2)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",11,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Course","Btech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        dep_label=Label(current_course_frame,text="Year",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=1,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",11,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        dep_label=Label(current_course_frame,text="Semester",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",11,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=230,width=700,height=300)

        studentID_label=Label(class_student_frame,text="Student Id:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Student Name:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Class Division:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_class,font=("times new roman",11,"bold"),width=18,state="readonly")
        div_combo["values"]=("Select Class Division","A","B")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        studentID_label=Label(class_student_frame,text="Roll No:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_rollno,width=20,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Gender:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        studentID_label=Label(class_student_frame,text="DOB:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Email:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Phone No:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Address:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        studentID_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",11,"bold"),bg="white")
        studentID_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radiobtn1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radiobtn1,text="No Photo Sample",value="no")
        radiobtn1.grid(row=6,column=1)
        
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=190,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        save_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1)

        save_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=2)

        save_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=220,width=715,height=70)

        takephoto_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",11,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=1,column=0)

        update_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=1)


        






        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=675,y=5,width=650,height=520)

        right_img=Image.open(r"C:\Users\admin\Downloads\WhatsApp Image 2023-12-25 at 02.40.40.jpeg")
        right_img=right_img.resize((655,120),Image.LANCZOS)
        self.photoright_img=ImageTk.PhotoImage(right_img)

        f_lbl=Label(Right_frame,image=self.photoright_img)
        f_lbl.place(x=5,y=0,width=655,height=120)

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=115,width=700,height=70)

        search_label=Label(search_frame,text="Search by",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),width=17,state="readonly")
        search_combo["values"]=("Select","Phone no","Roll no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(search_frame,text="Search",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)
 
        search_btn=Button(search_frame,text="Show all",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=4)
                        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=190,width=650,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","class","roll no","gender","DOB","email","phone no","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("class",text="Class Division")
        self.student_table.heading("roll no",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone no",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("class",width=100)
        self.student_table.column("roll no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self): 
        if self.var_dep.get()=="Select Department" or self.var_id.get()=="":
            messagebox.showerror("error","All Fields are required ",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shikharai1828",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_id.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_class.get(),
                                                                                                    self.var_rollno.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_DOB.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_teacher.get(),
                                                                                                    self.var_radiobtn1.get()
                                                                                            
                
                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    
              

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shikharai1828",database="facerecognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()   


    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_class.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radiobtn1.set(data[14])
                                                                               

         

    def update_data(self):
         if self.var_dep.get()=="Select Department" or self.var_id.get()=="":
            messagebox.showerror("error","All Fields are required ",parent=self.root)

         else:
             try:
                    update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                    if update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Shikharai1828",database="facerecognition")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                                        self.var_dep.get(),                                                                                        
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_sem.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_class.get(),
                                                                                                        self.var_rollno.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_DOB.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radiobtn1.get(),
                                                                                                        self.var_id.get()
                                                                                                 ))
                    else:
                        if not update:
                            return
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
             except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student page delete","Do you want to delete this page",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Shikharai1828",database="facerecognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                      
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_class.set("Select Class Division"),
        self.var_gender.set("Select Gender"),
        self.var_rollno.set(""),
        self.var_DOB.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radiobtn1.set("")

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_id.get()=="":
            messagebox.showerror("error","All Fields are required ",parent=self.root)

        else:
             try:
                 conn=mysql.connector.connect(host="localhost",username="root",password="Shikharai1828",database="facerecognition")
                 my_cursor=conn.cursor()
                 my_cursor.execute("select * from student")
                 myresult=my_cursor.fetchall()
                 id=0
                 for x in myresult:
                     id+=1
                 my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                                        self.var_dep.get(),                                                                                        
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_sem.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_class.get(),
                                                                                                        self.var_rollno.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_DOB.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radiobtn1.get(),
                                                                                                        self.var_id.get()==id+1
                                                                                                 ))
                 conn.commit()
                 self.fetch_data()
                 self.reset_data()
                 conn.close()

                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                 def face_cropped(img):
                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces=face_classifier.detectMultiScale(gray,1.3,5)
                          #scaling factor=1.3
                          #minimum neighbor=5

                     for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                          
                 cap=cv2.VideoCapture(0)
                 img_id=0
                 while True:
                     ret,my_frame=cap.read()
                     if face_cropped(my_frame) is not None:
                         img_id+=1
                         face=cv2.resize(face_cropped(my_frame),(450,450))
                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("Cropped Face",face)     

                     if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                 cap.release()
                 cv2.destroyAllWindows()
                      
                 messagebox.showinfo("Result","Generating dataset completed successfully",parent=self.root)
             except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                      
                    
                    








    
                        
                        








































































































































































































































































































































































































































































































































































































        
        









if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
     

    
