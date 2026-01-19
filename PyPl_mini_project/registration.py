from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pandas as pd
import qrcode
import os

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Yourself Here!")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="purple")

        self.bg = ImageTk.PhotoImage(file="bg5.jpg")
        bg = Label(self.root, image=self.bg).place(x=450, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="bg5.jpg")
        self.left_label = Label(self.root, image=self.left)
        self.left_label.place(x=80, y=100, width=400, height=500)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="purple").place(x=50, y=30)

        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        clss = Label(frame1, text="Class", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.txt_cls = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.txt_cls['values'] = ("Select", "F.E. B.Tech", "S.E. B.Tech", "T.E.B.Tech", "Final Year")
        self.txt_cls.place(x=50, y=270, width=250)

        dept = Label(frame1, text="Branch", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_dept = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.txt_dept['values'] = ("Select", "Computer", "Information Technology", "Artificial Intelligence & Data Science", "Mechanical", "Civil", "Electrical", "Electronics and Telecommunication")
        self.txt_dept.place(x=370, y=270, width=250)

        bgrp = Label(frame1, text="Blood Group", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_bgrp = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.txt_bgrp['values'] = ("Select", "A+ve", "A-ve", "B+ve", "B-ve", "AB+ve", "O+ve", "O-ve")
        self.txt_bgrp.place(x=50, y=340, width=250)

        div = Label(frame1, text="Division", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_div = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.txt_div['values'] = ("Select", "A", "B")
        self.txt_div.place(x=370, y=340, width=250)

        crn = Label(frame1, text="CRN", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=380)
        self.txt_crn = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_crn.place(x=50, y=410, width=250)

        # Upload Photo button
        upload_btn = ttk.Button(frame1, text="Upload Photo", command=self.upload_photo, style="TButton",)
        upload_btn.place(x=370, y=410, width=250)

        # Submit button
        submit_btn = ttk.Button(frame1, text="Submit", command=self.submit_form, style="TButton",)
        submit_btn.place(x=50, y=450, width=250)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title="Select Photo", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.update_layout(file_path)

    def update_layout(self, file_path):
        # Destroy the existing left_label
        if hasattr(self, "left_label") and self.left_label:
            self.left_label.destroy()

        # Set the background color to white after selecting the photo
        self.root.config(bg="purple")

        # Open the image using PIL to get its dimensions
        img = Image.open(file_path)

        # Calculate the scaling factors to fit the image within the frame
        frame_width, frame_height = 400, 500
        img_width, img_height = img.size
        scale_factor = min(frame_width / img_width, frame_height / img_height)

        # Resize the image
        img = img.resize((int(img_width * scale_factor), int(img_height * scale_factor)))

        # Convert the resized image to ImageTk format
        self.left = ImageTk.PhotoImage(img)

        # Display the selected photo as the background for self.left
        self.left_label = Label(self.root, image=self.left)
        self.left_label.place(x=80, y=100, width=frame_width, height=frame_height)

    def submit_form(self):
        # Extracting data from the form
        first_name = self.txt_fname.get()
        last_name = self.txt_lname.get()
        contact_no = self.txt_contact.get()
        email = self.txt_email.get()
        selected_class = self.txt_cls.get()
        selected_dept = self.txt_dept.get()
        selected_blood_group = self.txt_bgrp.get()
        selected_division = self.txt_div.get()
        crn = self.txt_crn.get()

        # Generating ID Card details
        id_card_details = f"""
        ID Card Details:
        -------------------------
        Name: {first_name} {last_name}
        Contact No.: {contact_no}
        Email: {email}
        Class: {selected_class}
        Branch: {selected_dept}
        Blood Group: {selected_blood_group}
        Division: {selected_division}
        CRN: {crn}
        """

        # Save the ID card details to a CSV file
        csv_data = {
            'First Name': [first_name],
            'Last Name': [last_name],
            'Contact No.': [contact_no],
            'Email': [email],
            'Class': [selected_class],
            'Branch': [selected_dept],
            'Blood Group': [selected_blood_group],
            'Division': [selected_division],
            'CRN': [crn]
        }

        df = pd.DataFrame(csv_data)
        csv_file_path = 'id_card_details.csv'
        df.to_csv(csv_file_path, index=False)

        # Generate and save QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(id_card_details)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save('qrcode.png')

        # Open a new window with ID card details and QR code
        self.open_id_card_window(id_card_details, 'qrcode.png')

    def open_id_card_window(self, id_card_details, qrcode_image_path):
        id_card_window = Toplevel(self.root)
        id_card_window.title("ID Card Details")
        id_card_window.geometry("600x800")

        # Display ID card details
        id_card_label = Label(id_card_window, text=id_card_details, font=("times new roman", 14), justify=LEFT)
        id_card_label.pack(pady=20)

        # Display QR code
        qr_code_img = ImageTk.PhotoImage(file=qrcode_image_path)
        qr_code_label = Label(id_card_window, image=qr_code_img)
        qr_code_label.image = qr_code_img
        qr_code_label.pack(pady=20)

# Create the main Tk() instance outside the class
root = Tk()
obj = Register(root)
root.mainloop()