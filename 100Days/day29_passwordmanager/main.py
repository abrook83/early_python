from tkinter import *
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pword_chars = []
    for letter in range(6):
        pword_chars.append(random.choice(letters))

    for symb in range(2):
        pword_chars.append(random.choice(symbols))

    for num in range(2):
        pword_chars.append(random.choice(numbers))

    random.shuffle(pword_chars)
    pword = ""
    for char in pword_chars:
        pword += char
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    site = website_entry.get()  # get the entered text as the name of the site
    uname = uname_entry.get()   # ...as above
    password = password_entry.get()   # ...as above
    data_entry = f"{site} | {uname} | {password}\n"
    with open(f"100Days\day29_passwordmanager/password_data.txt", mode='a') as password_data:
        password_data.write(data_entry)
    website_entry.delete(0,END)
    uname_entry.delete(0,END)
    password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

"""Create the app's window..."""
window = Tk()
# set the title...
window.title("Password Manager")
# add padding to the window's borders...
window.config(padx=20, pady=20, bg="white")

"""Create the canvas..."""
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
# Identify the image, assign it to a variable...
logo_image = PhotoImage(file="100Days\day29_passwordmanager\logo.png")
# Create an image on the canvas with the 'logo_image' as its image, with the centre at coordinates 100, 100...
canvas.create_image(100, 100, image=logo_image)
# Position the canvas in the window...
canvas.grid(column=1, row=0)

"""create the 'Website' label"""
website_label = Label(text="Website:", fg="black", bg="white", font=("Arial", 14, "normal"))
website_label.grid(column=0, row=1, padx=2, pady=2)     # parameters to convey display instructions

"""create the 'Email/Username' Email/Username:"""
uname_label = Label(text="Email/Username:", fg="black", bg="white", font=("Arial", 14, "normal"))
uname_label.grid(column=0, row=2, padx=2, pady=2)     # parameters to convey display instructions

"""create the 'Password' label"""
password_label = Label(text="Password:", fg="black", bg="white", font=("Arial", 14, "normal"))
password_label.grid(column=0, row=3, padx=2, pady=2)     # parameters to convey display instructions

"""create the website entry box"""
website_entry = Entry(width=54)
website_entry.grid(column=1, row=1, columnspan=2, padx=2, pady=2)
website_entry.focus()

"""create the username entry box"""
uname_entry = Entry(width=54)
uname_entry.grid(column=1, row=2, columnspan=2, padx=2, pady=2)
uname_entry.insert(0, "aaronbrook83@gmail.com")

"""create the password entry box"""
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, padx=2, pady=2)

"""create the password generator button"""
password_gen_button = Button(text="Generate Password", fg="black", font=("arial", 10, "normal"), command=generate_password, highlightthickness=0, width=15)
password_gen_button.grid(column=2, row=3, pady=2)     # enter grid coordinates for where to place each widget

"""create the add button"""
add_button = Button(text="Add", fg="black", font=("arial", 12, "normal"), command=add_entry, highlightthickness=0, width=36)
add_button.grid(column=1, row=4, columnspan=2, padx=2, pady=2)     # enter grid coordinates for where to place each widget

window.mainloop()