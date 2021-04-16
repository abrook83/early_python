import tkinter
### it's also possible to -
### 'from tkinter import *' to import every single class from tkinter,
### meaning we no longer need to call tkinter when we create an instance. 

def button_click():
    new_text = float(input.get())
    new_text *= 1.6
    conv_label.config(text=new_text)

"""# create a window"""
window = tkinter.Tk()

"""# set the title"""
window.title("Mile to km conversion")
# set the minimum window size -
window.minsize(300,150)
window.config(pady=20, padx=20)     # adds padding to the window's borders

"""# create the 'Miles' label"""
miles_label = tkinter.Label(text="Miles", font=("Arial", 16, "normal"))
miles_label.grid(column=2, row=0)     # parameters to convey display instructions

"""# create the 'is equal...' label"""
equal_label = tkinter.Label(text="is equal to", font=("Arial", 16, "normal"))
equal_label.grid(column=0, row=1)     # parameters to convey display instructions

"""# create the 'km' label"""
km_label = tkinter.Label(text="km", font=("Arial", 16, "normal"))
km_label.grid(column=2, row=1)     # parameters to convey display instructions

"""# create the converted figure's label"""
conv_label = tkinter.Label(text="", font=("Arial", 16, "normal"))
conv_label.grid(column=1, row=1)     # parameters to convey display instructions

"""# create a button"""
button = tkinter.Button(text="Calculate", command=button_click)        # pass in the name of a function, rather than call it, so no '()' required.
button.grid(column=1, row=2)     # enter coordinates for where to place each widget

"""# text entry"""
input = tkinter.Entry(width=10)     # Entry class from tkinter
input.grid(column=1, row=0)


"""Kept at the end of ALL code, keeps the mainloop running and the window open"""
window.mainloop()