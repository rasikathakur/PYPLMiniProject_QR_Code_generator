from tkinter import*
from PIL import Image, ImageTk

class Register:
    def __init__(self, root):
        self.root=root
        self.root.title("Register Yourself Here!")
        self.root.geometry("1350x700+0+0")

        self.bg=ImageTk.PhotoImage(file="bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="monitor.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1, text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="purple").place(x=50,y=30)