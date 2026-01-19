from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pandas as pd
import qrcode
import os

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Your ID is here!")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="purple")

        self.bg = ImageTk.PhotoImage(file="bg5.jpg")
        bg = Label(self.root, image=self.bg).place(x=450, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="bg5.jpg")
        self.left_label = Label(self.root, image=self.left)
        self.left_label.place(x=80, y=100, width=400, height=500)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="ID CARD", font=("times new roman", 20, "bold"), bg="white", fg="purple").place(x=50, y=30)

        # Load data from CSV file
        df = pd.read_csv('id_card_details.csv')

        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Label(frame1, text=df['First Name'][0], font=("times new roman", 15, "bold"), bg="purple", fg="purple")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Label(frame1, text=df['Last Name'][0], font=("times new roman", 15, "bold"), bg="white", fg="purple")
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Label(frame1, text=df['Contact No.'][0], font=("times new roman", 15, "bold"), bg="white", fg="purple")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Label(frame1, text=df['Email'][0], font=("times new roman", 15, "bold"), bg="white", fg="purple")
        self.txt_email.place(x=370, y=200, width=250)

        clss = Label(frame1, text="Class", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.txt_cls = Label(frame1, text=df['Class'][0], font=("times new roman", 15, "bold"), bg="white", fg="purple")
        self.txt_cls.place(x=50, y=270, width=250)

        dept = Label(frame1, text="Branch", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_dept = Label(frame1, text=df['Branch'][0], font=("times new roman", 15, "bold"), bg="white", fg="purple")
        self.txt_dept.place(x=370, y=270, width=250)

        bgrp = Label(frame1, text="Blood Group", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_bgrp = Label(frame1, text=df['Blood Group'][0], font=("times new roman", 15, "bold"), bg="white", fg="purple")
        self.txt_bgrp.place(x=50, y=340, width=250)

        div = Label(frame1, text="Division", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_div = Label(frame1, text=df['Division'][0], font=("times new roman", 15, "bold"), bg="white", fg="purple")
        self.txt_div.place(x=370, y=340, width=250)

        crn = Label(frame1, text="CRN", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=380)
        self.txt_crn = Label(frame1, text=df['CRN'][0], font=("times new roman", 15, "bold"), bg="white", fg="purple")
        self.txt_crn.place(x=50, y=410, width=250)

        # Print button
        submit_btn = ttk.Button(frame1, text="Print", command=self.submit_form, style="TButton",)
        submit_btn.place(x=50, y=450, width=250)

    def submit_form(self):
        # Placeholder function for the print action
        print("Printing...")

# Create the main Tk() instance outside the class
root = Tk()
obj = Register(root)
root.mainloop()
