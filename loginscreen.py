#create a login screen
from tkinter import *
import time
mn= Tk()
mn.geometry("350x350")
mn.title("Ichi Screens")
mn.configure(bg="powderblue")

fr1 = Frame(mn, bg="powderblue")
title = Label(fr1, text = "WELCOME BACK CAPTAIN", fg="black", bg="powderblue", font=("helvetica", 16, "bold", "italic", "underline"))
fr1.pack(pady=140)
title.pack()

def change():
	fr1.destroy()
	mn.geometry("500x500")

mn.after(3000, change)

fr2 = Frame(mn, bg="powderblue")
title2 = Label(fr2, text="ICHI SCREENS", bg="powderblue", fg="maroon", font=("Comic Sans", 16, "bold",  "italic" ))
loginbtn = Button(fr2, text="LOGIN", bg="powderblue", fg="maroon", font=("Comic Sans", 16, "bold",  "italic", "underline"), relief=FLAT)
signupbtn = Button(fr2, text="SIGN UP", bg="powderblue", fg="maroon", font=("Comic Sans", 16, "bold",  "italic", "underline"), relief=FLAT)

fr2.pack(pady=140)
title2.grid(row=0, column=1, columnspan=2)
loginbtn.grid(row=1, column=1, padx=70, pady=70)
signupbtn.grid(row=1, column=2, padx=70, pady=70)


mainloop()
