# ------------------------- PASSWORD MANAGER APP V2 ---------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pword_chars = []
    # add a number of characters from each list into the characters list -
    [pword_chars.append(random.choice(letters)) for letter in range(6)]
    [pword_chars.append(random.choice(symbols)) for symb in range(2)]
    [pword_chars.append(random.choice(numbers)) for num in range(2)]
    # shuffle the list -    
    random.shuffle(pword_chars)
    # 'join' method adds the shuffled letters into a new string -
    pword = "".join(pword_chars)
    # insert the generated password into the password textbox -
    password_entry.insert(0, pword)
    # pyperclip copy's the text onto the clipboard, hit ctrl+v to paste straightaway -
    pyperclip.copy(pword)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    site = website_entry.get()  # get the entered text as the name of the site
    uname = uname_entry.get()   # ...as above
    password = password_entry.get()   # ...as above
    new_entry = {
        site: {
        "Username": uname,
        "Password" : password,
        }
    }

    if len(site) < 1 or len(uname) < 1 or len(password) < 1:
        messagebox.showwarning(title="Fields empty", message="Some of your fields are empty...")
    else:
        try:
            """Open the existing file -"""
            with open(f"100Days\day30_errors_exceptions_json/password_data.json", 'r') as password_data:
                # read the existing data -
                data = json.load(password_data)

        except FileNotFoundError:
            """If the file doesn't exist -"""
            with open(f"100Days\day30_errors_exceptions_json/password_data.json", 'w') as password_data:
                json.dump(new_entry, password_data, indent=4)   # indent adds formatting to the json data

        else:
            """Then update the file -"""
            data.update(new_entry)

            with open(f"100Days\day30_errors_exceptions_json/password_data.json", 'w') as password_data:
                # save the updated data -
                json.dump(data, password_data, indent=4)   # indent adds formatting to the json data
        
        finally:    
            """Delete the field entries -"""
            website_entry.delete(0,END)
            # uname_entry.delete(0,END)
            password_entry.delete(0,END)


def search_entry():
    pass

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
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, padx=2, pady=2)
website_entry.focus()

"""create the username entry box"""
uname_entry = Entry(width=54)
uname_entry.grid(column=1, row=2, columnspan=2, padx=2, pady=2)
uname_entry.insert(0, "aaronbrook83@gmail.com")

"""create the password entry box"""
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, padx=2, pady=2)

"""create the search button"""
password_gen_button = Button(text="Search", fg="black", font=("arial", 10, "normal"), command=search_entry, highlightthickness=0, width=15)
password_gen_button.grid(column=2, row=1, pady=2)     # enter grid coordinates for where to place each widget

"""create the password generator button"""
password_gen_button = Button(text="Generate Password", fg="black", font=("arial", 10, "normal"), command=generate_password, highlightthickness=0, width=15)
password_gen_button.grid(column=2, row=3, pady=2)     # enter grid coordinates for where to place each widget

"""create the add button"""
add_button = Button(text="Add", fg="black", font=("arial", 12, "normal"), command=add_entry, highlightthickness=0, width=36)
add_button.grid(column=1, row=4, columnspan=2, padx=2, pady=2)     # enter grid coordinates for where to place each widget

window.mainloop()