from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
import tkinter
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1200x700+0+0")

        #*******************variable******************************
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postocde_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

        # Title Label
        lbtitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 30, "bold"))
        lbtitle.pack(side=TOP, fill=X)

        # Main Frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # Left Data Frame (Library Membership Information)
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=12, relief=RIDGE, font=("times new roman", 12, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0, y=5, width=860, height=350)

        # Labels and Entry for Member Information
        lblMembr = Label(DataFrameLeft, bg="powder blue",text="Member Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMembr.grid(row=0, column=0, sticky=W)
        
        comMember = ttk.Combobox(DataFrameLeft,textvariable=self.member_var, font=("times new roman", 15, "bold"), width=27)
        comMember["values"] = ("Admin staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblPRN_No=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No:",padx=2,bg="powder blue")
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstname=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName:",padx=2,pady=6,bg="powder blue")
        lblFirstname.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lastname:",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtlastname=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtlastname.grid(row=4,column=1)

        lblAdress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1",padx=2,pady=4,bg="powder blue")
        lblAdress1.grid(row=5,column=0,sticky=W)
        txtaddresss1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtaddresss1.grid(row=5,column=1)

        lblAdress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2:",padx=2,pady=6,bg="powder blue")
        lblAdress2.grid(row=6,column=0,sticky=W)
        txtaddresss2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtaddresss2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post Code:",padx=2,pady=4,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostcode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postocde_var,width=29)
        txtPostcode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text=" Book Id:",padx=2,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtbookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtbookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBooktitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBooktitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name:",padx=2,pady=6,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateborrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateborrowed.grid(row=3,column=3)
 
        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtdatedue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtdatedue.grid(row=4,column=3)

        lblDaysonBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days on Book:",padx=2,pady=6,bg="powder blue")
        lblDaysonBook.grid(row=5,column=2,sticky=W)
        txtdaysonbook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtdaysonbook.grid(row=5,column=3)

        lblLateReturn=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="powder blue")
        lblLateReturn.grid(row=6,column=2,sticky=W)
        txtLatereturn=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLatereturn.grid(row=6,column=3)

        lblDateOverdate = Label(DataFrameLeft, font=("arial", 12, "bold"),text="Date Over Due", padx=2, pady=6, bg="powder blue")
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtdateoverdate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateoverdue_var, width=29)
        txtdateoverdate.grid(row=7, column=3)

        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualprice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualprice.grid(row=8,column=3)

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=12, relief=RIDGE, font=("arial", 12, "bold"), padx=20)
        DataFrameRight.place(x=870, y=5, width=580, height=350)
        
        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)  
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=2)

        Listbooks = [
    'Head Firt Book','Learn python The Hard Way','Python programming','Secrete Rahshy',
    'python cookbook','Intro to machine Learning','Machine tecno','My python',
    'Josss Ellif guru','Elite Jungle python','Jungli python',
    'Machine python','Advance python','Inton python','Redchilli python','Ishq python']
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Head Firt Book"):
                self.bookid_var.set("BKID4545")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry ")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1.strftime("%d/%m/%Y"))
                self.datedue_var.set(d3.strftime("%d/%m/%Y"))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif(x=="Learn python The Hard Way"):
                self.bookid_var.set("BKID6758")
                self.booktitle_var.set("Basics of python")
                self.author_var.set("St Mareen ")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1.strftime("%d/%m/%Y"))
                self.datedue_var.set(d3.strftime("%d/%m/%Y"))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.560")    

            elif(x=="Intro to machine learning"):
                self.bookid_var.set("BKID2343")
                self.booktitle_var.set("Introduction to ML")
                self.author_var.set("James Bron ")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1.strftime("%d/%m/%Y"))
                self.datedue_var.set(d3.strftime("%d/%m/%Y"))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 45")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.345")

            elif(x=="Python programming"):
                self.bookid_var.set("BKID9875")
                self.booktitle_var.set("Mastery in Python")
                self.author_var.set("Bones Jammy")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1.strftime("%d/%m/%Y"))
                self.datedue_var.set(d3.strftime("%d/%m/%Y"))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.588")    

            if(x=="python cookbook"):
                self.bookid_var.set("BKID2132")
                self.booktitle_var.set("Projects on python")
                self.author_var.set("Cersie Harvard")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1.strftime("%d/%m/%Y"))
                self.datedue_var.set(d3.strftime("%d/%m/%Y"))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.288")      


        
        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)
        
        for item in Listbooks:
            listBox.insert(END,item)
        
        # Button Frame
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)
        
        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data", font=("arial",12,"bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0 )

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data", font=("arial",12,"bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1 )

        btnAddData=Button(Framebutton,command=self.update,text="Update", font=("arial",12,"bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2 )

        btnAddData=Button(Framebutton,command=self.delete,text="Delete", font=("arial",12,"bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3 )

        btnAddData=Button(Framebutton,command=self.reset,text="Reset", font=("arial",12,"bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4 )

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit", font=("arial",12,"bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5 )
        

        Framedetail=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framedetail.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(Framedetail,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
         
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.libray_table=ttk.Treeview(Table_frame, column=("membertype","prnno","title","firstname","lastname","address1",
                                                            "address2","postid","mobile","bookid","booktitle","author","dateborrowed",
                                                            "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set) 
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
 
        xscroll.config(command=self.libray_table.xview)
        yscroll.config(command=self.libray_table.yview)

        self.libray_table.heading("membertype",text="Member Type")
        self.libray_table.heading("prnno",text="Reference no")
        self.libray_table.heading("title",text="Title")
        self.libray_table.heading("firstname",text="First Name")
        self.libray_table.heading("lastname",text="Last Name")
        self.libray_table.heading("address1",text="Address1")
        self.libray_table.heading("address2",text="Address2")
        self.libray_table.heading("postid",text="Post ID")
        self.libray_table.heading("mobile",text="Mobile Number")
        self.libray_table.heading("bookid",text="Book ID")
        self.libray_table.heading("booktitle",text="Book Title")
        self.libray_table.heading("author",text="Author")
        self.libray_table.heading("dateborrowed",text="Date of borrowed")
        self.libray_table.heading("datedue",text="Date Due")
        self.libray_table.heading("days",text="DaysOnBook")
        self.libray_table.heading("latereturnfine", text="LateReturnFine")
        self.libray_table.heading("dateoverdue",text="DateOverDue")
        self.libray_table.heading("finalprice",text="Final Price")

        self.libray_table["show"]="headings"
        self.libray_table.pack(fill=BOTH,expand=1)

        self.libray_table.column("membertype", width=100)
        self.libray_table.column("prnno", width=100)
        self.libray_table.column("title", width=100)
        self.libray_table.column("firstname", width=100)
        self.libray_table.column("lastname", width=100)
        self.libray_table.column("address1", width=100)
        self.libray_table.column("address2", width=100)
        self.libray_table.column("postid", width=100)
        self.libray_table.column("mobile", width=100)
        self.libray_table.column("bookid", width=100)
        self.libray_table.column("booktitle", width=100)
        self.libray_table.column("author", width=100)
        self.libray_table.column("dateborrowed", width=100)
        self.libray_table.column("datedue", width=100)
        self.libray_table.column("days", width=100)
        self.libray_table.column("latereturnfine", width=100)
        self.libray_table.column("dateoverdue", width=100)
        self.libray_table.column("finalprice", width=100)
        
        self.fetch_data()
        self.libray_table.bind("<<ButtonRelease-1>>",self.get_cursor)

    def adda_data(self):
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql@123",
            database="MyData"
        )
        my_cursor=conn.cursor()
        my_cursor.execute("Insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                              self.member_var.get(),
                                                                                                              self.prn_var.get(),
                                                                                                              self.id_var.get(),
                                                                                                              self.firstname_var.get(),
                                                                                                              self.lastname_var.get(),
                                                                                                              self.address1_var.get(),
                                                                                                              self.address2_var.get(),
                                                                                                              self.postocde_var.get(),
                                                                                                              self.mobile_var.get(),
                                                                                                              self.bookid_var.get(),
                                                                                                              self.booktitle_var.get(),
                                                                                                              self.author_var.get(),
                                                                                                              self.dateborrowed_var.get(),
                                                                                                              self.datedue_var.get(),
                                                                                                              self.daysonbook_var.get(),
                                                                                                              self.latereturnfine_var.get(),
                                                                                                              self.dateoverdue_var.get(),        
                                                                                                              self.finalprice_var.get()
                                                                                                            ))
        conn.commit()
        self.fetch_data
        conn.close()

        messagebox.showinfo("Success","Member Has been inserted successfully")
    
    def update(self):
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql@123",
            database="MyData"
        )
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, Post ID=%s, Mobile=%s, Bookid=%s, Booktitle=%s, Author=%, dateborrowed=%s, datedue=%s, daysonbook=%s,latereturnfine=%s, dateoverdue=%s, finalprice=%s where PRN_NO=%s",(
                                                                                                              self.member_var.get(),
                                                                                                              self.prn_var.get(),
                                                                                                              self.id_var.get(),
                                                                                                              self.firstname_var.get(),
                                                                                                              self.lastname_var.get(),
                                                                                                              self.address1_var.get(),
                                                                                                              self.address2_var.get(),
                                                                                                              self.postocde_var.get(),
                                                                                                              self.mobile_var.get(),
                                                                                                              self.bookid_var.get(),
                                                                                                              self.booktitle_var.get(),
                                                                                                              self.author_var.get(),
                                                                                                              self.dateborrowed_var.get(),
                                                                                                              self.datedue_var.get(),
                                                                                                              self.daysonbook_var.get(),
                                                                                                              self.latereturnfine_var.get(),
                                                                                                              self.dateoverdue_var.get(),        
                                                                                                              self.finalprice_var.get()
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Member has been updated")
    
    def fetch_data(self):
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql@123",
            database="MyData"
        )
        my_cursor=conn.cursor()  
        my_cursor.execute("Select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.libray_table.delete(*self.libray_table.get_children())
            for i in rows:
                self.libray_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    def get_cursor(self,event=""):
        cursor_row=self.libray_table.focus()
        content=self.libray_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postocde_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
 
    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+ self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID NO:\t\t"+ self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+ self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+ self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postocde_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"DaysonBook:\t\t"+ self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"LatereturnFine:\t\t"+ self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice_var.get()+"\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var(""),
        self.firstname_var(""),
        self.lastname_var(""),
        self.address1_var(""),
        self.address2_var(""),
        self.postocde_var(""),
        self.mobile_var(""),
        self.bookid_var(""),
        self.booktitle_var(""),
        self.author_var(""),
        self.dateborrowed_var(""),
        self.datedue_var(""),
        self.daysonbook_var(""),
        self.latereturnfine_var(""),
        self.dateoverdue_var(""),
        self.finalprice_var("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management System","Do you want to Exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member ")
        else:
            conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql@123",
            database="MyData"
        )
        my_cursor=conn.cursor()
        query="delete from library where PRN_No=%s"
        value=(self.prn_var.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Sucess","Member has been Deleted") 


if __name__ == "__main__":
     root = Tk()
     obj = LibraryManagementSystem(root)
     root.mainloop()