from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

"""Create the app's window..."""
window = Tk()
"""set the title..."""
window.title("Password Manager")
"""add padding to the window's borders..."""
window.config(padx=20, pady=20, bg="white")

"""Create the canvas..."""
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
"""Identify the image, assign it to a variable..."""
logo_image = PhotoImage(file="100Days\day29_passwordmanager\logo.png")
"""Create an image on the canvas with the 'logo_image' as its image, at coordinates 100, 100..."""
canvas.create_image(100, 100, image=logo_image)
"""Position the canvas in the window..."""
canvas.grid(column=1, row=1)


window.mainloop()