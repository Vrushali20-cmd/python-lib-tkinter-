from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1200x700+0+0")

        # Variables
        self.NamesoFtables = StringVar()
        self.Reference_No = StringVar()
        self.Dose = StringVar()
        self.Numberoftablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.Expdate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()  # Used as Blood Pressure
        self.HowtouseMedication = StringVar()   # Used as Medication
        self.PatientId = StringVar()
        self.nhsnumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()

        # Title
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 30, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Frames
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=100, width=1200, height=350)

        DataframeLeft = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=900, height=310)

        DataframeRight = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"), text="Prescription")
        DataframeRight.place(x=910, y=5, width=260, height=310)

        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=450, width=1200, height=70)

        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=520, width=1200, height=160)

        # Labels and Entries (Your Format)
        lblNameTablet = Label(DataframeLeft, text="Name of Tablet:", font=("arial", 12, "bold"))
        lblNameTablet.grid(row=0, column=0, sticky=W)
        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.NamesoFtables, font=("arial", 12, "bold"), width=27)
        comNametablet["values"] = ("", "Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, text="Reference No:", font=("arial", 12, "bold"))
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, textvariable=self.Reference_No, font=("arial", 12, "bold"), width=29)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, text="Dose:", font=("arial", 12, "bold"))
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, textvariable=self.Dose, font=("arial", 12, "bold"), width=29)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft, text="No of Tablets:", font=("arial", 12, "bold"))
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataframeLeft, textvariable=self.Numberoftablets, font=("arial", 12, "bold"), width=29)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, text="Lot:", font=("arial", 12, "bold"))
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, textvariable=self.Lot, font=("arial", 12, "bold"), width=29)
        txtLot.grid(row=4, column=1)

        lblissuedate = Label(DataframeLeft, text="Issue Date:", font=("arial", 12, "bold"))
        lblissuedate.grid(row=5, column=0, sticky=W)
        txtissuedate = Entry(DataframeLeft, textvariable=self.Issuedate, font=("arial", 12, "bold"), width=29)
        txtissuedate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, text="Exp Date:", font=("arial", 12, "bold"))
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, textvariable=self.Expdate, font=("arial", 12, "bold"), width=29)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, text="Daily Dose:", font=("arial", 12, "bold"))
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, textvariable=self.DailyDose, font=("arial", 12, "bold"), width=29)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, text="Side Effect:", font=("arial", 12, "bold"))
        lblSideEffect.grid(row=0, column=2, sticky=W)
        txtSideEffect = Entry(DataframeLeft, textvariable=self.sideEffect, font=("arial", 12, "bold"), width=29)
        txtSideEffect.grid(row=0, column=3)

        lblFurtherInfo = Label(DataframeLeft, text="Further Info:", font=("arial", 12, "bold"))
        lblFurtherInfo.grid(row=1, column=2, sticky=W)
        txtFurtherInfo = Entry(DataframeLeft, textvariable=self.FurtherInformation, font=("arial", 12, "bold"), width=29)
        txtFurtherInfo.grid(row=1, column=3)

        lblBloodPressure = Label(DataframeLeft, text="Blood Pressure:", font=("arial", 12, "bold"))
        lblBloodPressure.grid(row=2, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, textvariable=self.DrivingUsingMachine, font=("arial", 12, "bold"), width=29)
        txtBloodPressure.grid(row=2, column=3)

        lblStorageAdvice = Label(DataframeLeft, text="Storage Advice:", font=("arial", 12, "bold"))
        lblStorageAdvice.grid(row=3, column=2, sticky=W)
        txtStorageAdvice = Entry(DataframeLeft, textvariable=self.StorageAdvice, font=("arial", 12, "bold"), width=29)
        txtStorageAdvice.grid(row=3, column=3)

        lblMedication = Label(DataframeLeft, text="Medication:", font=("arial", 12, "bold"))
        lblMedication.grid(row=4, column=2, sticky=W)
        txtMedication = Entry(DataframeLeft, textvariable=self.HowtouseMedication, font=("arial", 12, "bold"), width=29)
        txtMedication.grid(row=4, column=3)

        lblPatientId = Label(DataframeLeft, text="Patient ID:", font=("arial", 12, "bold"))
        lblPatientId.grid(row=5, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, textvariable=self.PatientId, font=("arial", 12, "bold"), width=29)
        txtPatientId.grid(row=5, column=3)

        lblNHS = Label(DataframeLeft, text="NHS Number:", font=("arial", 12, "bold"))
        lblNHS.grid(row=6, column=2, sticky=W)
        txtNHS = Entry(DataframeLeft, textvariable=self.nhsnumber, font=("arial", 12, "bold"), width=29)
        txtNHS.grid(row=6, column=3)

        lblPatientName = Label(DataframeLeft, text="Patient Name:", font=("arial", 12, "bold"))
        lblPatientName.grid(row=7, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, textvariable=self.PatientName, font=("arial", 12, "bold"), width=29)
        txtPatientName.grid(row=7, column=3)

        lblDOB = Label(DataframeLeft, text="Date of Birth:", font=("arial", 12, "bold"))
        lblDOB.grid(row=8, column=2, sticky=W)
        txtDOB = Entry(DataframeLeft, textvariable=self.DateofBirth, font=("arial", 12, "bold"), width=29)
        txtDOB.grid(row=8, column=3)

        lblAddress = Label(DataframeLeft, text="Patient Address:", font=("arial", 12, "bold"))
        lblAddress.grid(row=8, column=0, sticky=W)
        txtAddress = Entry(DataframeLeft, textvariable=self.PatientAddress, font=("arial", 12, "bold"), width=29)
        txtAddress.grid(row=8, column=1)

        # Text area
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=30, height=16)
        self.txtPrescription.grid(row=0, column=0)

        # Buttons
        btnPrescription = Button(ButtonFrame, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=15, command=self.iPrescriptionData)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(ButtonFrame, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=15)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(ButtonFrame, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=15)
        btnUpdate.grid(row=0, column=2)

        btnClear = Button(ButtonFrame, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=15)
        btnClear.grid(row=0, column=3)

        btnDelete = Button(ButtonFrame, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=15)
        btnDelete.grid(row=0, column=4)

        btnExit = Button(ButtonFrame, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=15)
        btnExit.grid(row=0, column=5)

    def iPrescriptionData(self):
        if self.NamesoFtables.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="mysql@123",
                    database="MyDatas"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO hospital (nameoftablets, Reference_No, dose, nooftablets, lot, issuedate, expdate, dailydose, sideeffect, furtherinfo, bloodpressure, storageadvice, medication, patientid, nhsnumber, patientname, dob, address) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.NamesoFtables.get(),
                        self.Reference_No.get(),
                        self.Dose.get(),
                        self.Numberoftablets.get(),
                        self.Lot.get(),
                        self.Issuedate.get(),
                        self.Expdate.get(),
                        self.DailyDose.get(),
                        self.sideEffect.get(),
                        self.FurtherInformation.get(),
                        self.DrivingUsingMachine.get(),
                        self.StorageAdvice.get(),
                        self.HowtouseMedication.get(),
                        self.PatientId.get(),
                        self.nhsnumber.get(),
                        self.PatientName.get(),
                        self.DateofBirth.get(),
                        self.PatientAddress.get()
                    )
                )
                conn.commit()
                messagebox.showinfo("Success", "Record inserted successfully")
            except Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                if conn.is_connected():
                    my_cursor.close()
                    conn.close()


# Run program
if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()
