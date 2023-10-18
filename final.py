# By Ichi_Gin
# A program  to display a basic login screen with added features
# Import all the needed modules
from tkinter import *
from tkinter import messagebox
import time
# Intitiate the main window
main_window= Tk()
# main_window.geometry("350x350+800+150")
main_window.title("Ichi Screens")
# Set the background color
main_window.configure(bg="powderblue")

width = main_window.winfo_screenwidth()
height = main_window.winfo_screenheight()

main_window.geometry("%dx%d" % (width, height))

# Put widgets in a frame for neatness
fr1 = Frame(main_window, bg="powderblue")
title = Label(fr1, text = "GOOD DAY CAPTAIN .", fg="black", bg="powderblue", font=("helvetica", 25, "bold", "italic"))


fr1.pack(pady=350)
title.pack()



# Function to create a new window after set time
def change():
	main_window.destroy()
	new_window = Tk()

	width = new_window.winfo_screenwidth()
	height = new_window.winfo_screenheight()

	new_window.geometry("%dx%d" % (width, height))

	def clicked_on(event):
		for i in lbox.curselection():
			# Log in functon
			if lbox.get(i) == "Continue as Main User" :
				return

			if lbox.get(i) == "Login to Your account" :
				return

			if lbox.get(i) == "Help" :
				return

			if lbox.get(i) == "Credits" :
				new_window.destroy()
				tx  = Tk()
				textbox = Text(tx, height=18, width=45)

				contributors = [
					"Gia",
					"Anthony",
					"Milan",
					"Branton",
					"Me & Myself"
					]

				for member in contributors:
					textbox.insert(END, member + "\n")

				def change_state():
					textbox.configure(state =DISABLED)

				tx.after(2,change_state)

				



					

				textbox.pack()

			# function to create a new user account 
			elif lbox.get(i) == "Create a new account" :
				new_window.destroy()
				# create a new window and assign it a new name
				signup_window = Tk()
				width = signup_window.winfo_screenwidth()
				height = signup_window.winfo_screenheight()

				signup_window.geometry("%dx%d" % (width, height))


				def on_entry_click(event):
					if entry.get() == "Enter a username...":
						entry.delete(0, "end")
						entry.insert(0, "")
						entry.config(fg="black")
					if entry2.get()== "Choose a password...":
						entry2.delete(0, "end")
						entry2.insert(0, "")
						entry2.config(fg="black")
					if entry3.get()== "Retype your password...":
						entry3.delete(0, "end")
						entry3.insert(0, "")
						entry3.config(fg="black")
				def on_focusout(event):
					if entry.get() == "":
						entry.insert(0, "Enter a username...")
						entry.config(fg="grey")
					if entry2.get() == "":
						entry2.insert(0, "Choose a password...")
						entry2.config(fg="grey")
					if entry.get() == "":
						entry3.insert(0, "Retype your password...")
						entry3.config(fg="grey")

				entry = Entry(signup_window, bd=1, font = ("", 16, "italic"))
				entry.insert(0, "Enter a username...")
				entry.bind("<FocusIn>", on_entry_click)
				entry.bind("<FocusOut>", on_focusout)
				entry.config(fg="grey")


				entry2 = Entry(signup_window, bd=1, font = ("", 16, "italic"))
				entry2.insert(0, "Choose a password...")
				entry2.bind("<FocusIn>", on_entry_click)
				entry2.bind("<FocusOut>", on_focusout)
				entry2.config(fg="grey")

				entry3 = Entry(signup_window, bd=1, font = ("", 16, "italic"))
				entry3.insert(0, "Retype your password...")
				entry3.bind("<FocusIn>", on_entry_click)
				entry3.bind("<FocusOut>", on_focusout)
				entry3.config(fg="grey")

				log_in_btn = Button(signup_window, text="Log In", relief=RIDGE, font = ("Comic Sans", 16))

				entry.pack(anchor = E)
				entry2.pack(anchor = E)
				entry3.pack(anchor = E)
				log_in_btn.pack(anchor = SE)

	# new_window.geometry("500x500")
	new_window.title("Menu Chooser")
	new_window.configure(bg="powderblue")
	l_frame = LabelFrame(new_window, text="Boot Menu",fg="black", bg="powderblue",  font=("Helvetica", 18, "bold", "italic", "underline"), labelanchor = N)
	lbox = Listbox(l_frame, height=height, width=width, activestyle="dotbox", font=("Helvetica", 20, "italic"), fg="black", bg="powderblue",  bd=0, highlightthickness=0, selectforeground="blue", justify=CENTER)

	# label = Label(new_window, text="Boot Menu", fg="black", bg="powderblue",  font=("Helvetica", 18, "bold", "italic", "underline"))


	lbox.insert(0, "Continue as Main User")
	lbox.insert(1, "Login to Your account")
	lbox.insert(2, "Create a new account")
	lbox.insert(3, "Help")
	lbox.insert(4, "Credits")

	# bind functions to buttons
	# bind function to any click
	new_window.bind("<Button-1>", clicked_on)
	# bind function to Enter button
	new_window.bind("<Return>", clicked_on)

	l_frame.pack(padx = 200, pady =100)
	lbox.pack(padx = 150, pady =150)




main_window.after(2000, change)

mainloop()