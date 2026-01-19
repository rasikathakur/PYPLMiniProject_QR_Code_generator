from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pandas as pd
import os

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("ID Card Viewer")
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

        # PRN Label and Entry
        prn_label = Label(frame1, text="Enter PRN:", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=70)
        self.txt_prn = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_prn.place(x=180, y=70, width=120)

        # Initialize empty data frame
        self.df = pd.DataFrame()

        # Print button
        print_btn = ttk.Button(frame1, text="Print", command=self.print_id_card, style="TButton",)
        print_btn.place(x=50, y=100, width=250)

    def print_id_card(self):
        prn = self.txt_prn.get().strip()

        if not prn:
            messagebox.showerror("Error", "Please enter PRN number")
            return

        # Load data from CSV file
        self.df = pd.read_csv('id_card_details.csv')

        # Filter data based on the entered PRN number
        filtered_data = self.df[self.df['CRN'].astype(str) == prn]

        if not filtered_data.empty:
            # Display the details if PRN number is found
            self.create_id_card(filtered_data)
        else:
            messagebox.showerror("Error", "PRN not found")

    def create_id_card(self, data):
        # Create a new image with "bg6.jpg" as the base
        img_bg = Image.open("bg6.jpg")
        img = Image.new("RGBA", (700, 500), color=(255, 255, 255, 0))
        img.paste(img_bg, (0, 0))

        # Draw text on the image with the ID card details
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()  # You can customize the font as needed

        draw.text((50, 130), f"Name: {data['First Name'].iloc[0]} {data['Last Name'].iloc[0]}", font=font, fill=(128, 0, 128))
        draw.text((50, 200), f"Contact No.: {data['Contact No.'].iloc[0]}", font=font, fill=(128, 0, 128))
        draw.text((50, 270), f"Email: {data['Email'].iloc[0]}", font=font, fill=(128, 0, 128))
        draw.text((50, 340), f"Class: {data['Class'].iloc[0]}", font=font, fill=(128, 0, 128))

        # Check if 'CRN' is present in the DataFrame
        if 'CRN' in data.columns:
            draw.text((50, 410), f"CRN: {data['CRN'].iloc[0]}", font=font, fill=(128, 0, 128))
        elif 'CRN_x' in data.columns:
            draw.text((50, 410), f"CRN: {data['CRN_x'].iloc[0]}", font=font, fill=(128, 0, 128))
        else:
            messagebox.showerror("Error", "CRN column not found in DataFrame")

        # Save the image to a specified location
        img.save("id_card_image.png")
        print("ID card image saved successfully.")

# Create the main Tk() instance outside the class
root = Tk()
obj = Register(root)
root.mainloop()
