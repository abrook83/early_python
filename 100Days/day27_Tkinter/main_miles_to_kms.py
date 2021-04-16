from tkinter import *
### 'from tkinter import *' imports every single class from tkinter,
### meaning we no longer need to call tkinter when we create an instance.

def button_click():
    new_text = float(input.get())
    new_text *= 1.61
    conv_label.config(text=new_text)

"""# create a window"""
window = Tk()

"""# set the title"""
window.title("Mile to km conversion")
# set the minimum window size -
window.minsize(300,150)
window.config(pady=20)     # adds padding to the window's borders

"""# create the 'Miles' label"""
miles_label = Label(text="Miles", font=("Arial", 16, "normal"))
miles_label.grid(column=2, row=0)     # parameters to convey display instructions
miles_label.config(pady=5, padx=5)

"""# create the 'is equal...' label"""
equal_label = Label(text="is equal to", font=("Arial", 16, "normal"))
equal_label.grid(column=0, row=1)     # parameters to convey display instructions
equal_label.config(pady=5)

"""# create the 'km' label"""
km_label = Label(text="km", font=("Arial", 16, "normal"))
km_label.grid(column=2, row=1)     # parameters to convey display instructions
km_label.config(pady=5)

"""# create the converted figure's label"""
conv_label = Label(text="", font=("Arial", 16, "normal"))
conv_label.grid(column=1, row=1)     # parameters to convey display instructions
conv_label.config(pady=5, padx=5)

"""# create a button"""
button = Button(text="Calculate", command=button_click)        # pass in the name of a function, rather than call it, so no '()' required.
button.grid(column=1, row=2)     # enter coordinates for where to place each widget
button.config(pady=5, padx=5)

"""# text entry"""
input = Entry(width=10)     # Entry class from tkinter
input.grid(column=1, row=0)
# input.config(pady=5, padx=5)

"""Kept at the end of ALL code, keeps the mainloop running and the window open"""
window.mainloop()