import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import qrcode
from PIL import Image, ImageTk

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration Form")

        # Load background image
        background_image = Image.open("bg.jpg")
        background_image = ImageTk.PhotoImage(background_image)

        # Create Canvas to display the background image
        canvas = tk.Canvas(root, width=background_image.width(), height=background_image.height())
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, anchor="nw", image=background_image)

        # Create a white panel with equal margins from all sides
        panel = tk.Frame(canvas, bg="white", width=background_image.width() - 40, height=background_image.height() - 40)
        panel.place(relx=0.5, rely=0.5, anchor="center")

        # Create a container frame for form elements
        form_frame = tk.Frame(panel, bg="white")
        form_frame.pack(padx=20, pady=20)

        # Variables for form data
        self.photo_path_var = tk.StringVar()
        self.prn_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.class_var = tk.StringVar()
        self.division_var = tk.StringVar()
        self.blood_group_var = tk.StringVar()
        self.branch_var = tk.StringVar()

        # Font configuration
        font_style = ("Rockwell", 21)

        # Creating labels and entry widgets
        labels = ["Photo:", "PRN Number:", "Name:", "Class:", "Division:", "Blood Group:", "Branch:"]
        self.entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(form_frame, text=label_text, bg="white", padx=10, pady=10, font=font_style)
            label.grid(row=i, column=0, sticky="e")

            if label_text == "Photo:":
                entry = tk.Button(form_frame, text="Upload Photo", command=self.upload_photo, font=font_style)
            elif label_text == "Branch:":
                branch_options = ["Computer", "Information Technology", "Artificial Intelligence & Data Science",
                                  "Mechanical", "Civil", "Electrical", "Electronics and Telecommunication"]
                entry = ttk.Combobox(form_frame, textvariable=self.branch_var, values=branch_options, font=font_style)
            elif label_text == "Class:":
                class_options = ["FE B.Tech", "SE B.Tech", "TE B.Tech", "Final Year"]
                entry = ttk.Combobox(form_frame, textvariable=self.class_var, values=class_options, font=font_style)
            elif label_text == "Division:":
                division_options = ["A", "B"]
                entry = ttk.Combobox(form_frame, textvariable=self.division_var, values=division_options, font=font_style)
            else:
                entry = tk.Entry(form_frame, textvariable=self.get_variable(label_text), font=font_style, bd=1, highlightbackground="purple", highlightcolor="purple")

            entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")
            self.entries.append(entry)

        # Generate ID Button
        generate_id_button = tk.Button(form_frame, text="Generate ID", command=self.generate_id_card, font=font_style)
        generate_id_button.grid(row=len(labels), column=1, pady=20, sticky="w")

    def get_variable(self, label_text):
        if label_text == "PRN Number:":
            return self.prn_var
        elif label_text == "Name:":
            return self.name_var
        elif label_text == "Blood Group:":
            return self.blood_group_var

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title="Select Photo", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.photo_path_var.set(file_path)

    def generate_id_card(self):
        # Get form data
        data = {
            "Photo": self.photo_path_var.get(),
            "PRN Number": self.prn_var.get(),
            "Name": self.name_var.get(),
            "Class": self.class_var.get(),
            "Division": self.division_var.get(),
            "Blood Group": self.blood_group_var.get(),
            "Branch": self.branch_var.get()
        }

        # Save data to CSV
        self.save_to_csv(data)

        # Generate QR Code
        qr_data = f"PRN: {data['PRN Number']}\nName: {data['Name']}\nClass: {data['Class']}\nDivision: {data['Division']}\nBranch: {data['Branch']}"
        self.generate_qr_code(data['PRN Number'], qr_data)

        # Display ID Card
        self.display_id_card(data)

    def save_to_csv(self, data):
        try:
            df = pd.read_csv("student_data.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Photo", "PRN Number", "Name", "Class", "Division", "Blood Group", "Branch"])

        new_df = pd.DataFrame([data])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv("student_data.csv", index=False)
        print("Data saved to CSV.")

    def generate_qr_code(self, prn, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"qr_codes/{prn}_qr.png")
        print("QR Code generated.")

    def display_id_card(self, data):
        id_card_window = tk.Toplevel(self.root)
        id_card_window.title("Student ID Card")

        # Load Photo
        photo_image = Image.open(data['Photo'])
        photo_image.thumbnail((100, 100))
        photo_image = ImageTk.PhotoImage(photo_image)

        # Load QR Code
        qr_image = Image.open(f"qr_codes/{data['PRN Number']}_qr.png")
        qr_image.thumbnail((100, 100))
        qr_image = ImageTk.PhotoImage(qr_image)

        # Display data on ID Card
        tk.Label(id_card_window, text=f"PRN: {data['PRN Number']}", font=font_style, pady=5).pack()
        tk.Label(id_card_window, text=f"Name: {data['Name']}", font=font_style, pady=5).pack()
        tk.Label(id_card_window, text=f"Class: {data['Class']}", font=font_style, pady=5).pack()
        tk.Label(id_card_window, text=f"Division: {data['Division']}", font=font_style, pady=5).pack()
        tk.Label(id_card_window, text=f"Branch: {data['Branch']}", font=font_style, pady=5).pack()

        # Display Photo
        tk.Label(id_card_window, image=photo_image).pack()

        # Display QR Code
        tk.Label(id_card_window, image=qr_image).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
