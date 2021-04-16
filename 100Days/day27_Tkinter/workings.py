import tkinter
### it's also possible to -
### 'from tkinter import *' to import every single class from tkinter,
### meaning we no longer need to call tkinter when we create an instance. 

def button_click():
    # print("Which one a y'all clikced me??")
    # label.config(text="Button clicked!")
    new_text = input.get()
    label.config(text=new_text)

"""# create a window"""
window = tkinter.Tk()

"""# set the title"""
window.title("My first GUI program")
# set the minimum window size -
window.minsize(800,800)

"""# create a label"""
label = tkinter.Label(text="It's ya boy Label!", font=("Arial", 22, "italic"))
# change the text in a label by calling it like a dictionary -
label["text"] = "New Text"
# OR, pass in the text as a key=word argument -
label.config(text="New Text")
# display the label (call the packer) -
label.pack(side="top")     # parameters to convey display instructions
# Use placement methods (pack, place...) at the end of each widget's code

"""# create a button"""
button = tkinter.Button(text="Click here", command=button_click)        # pass in the name of a function, rather than call it, so no '()' required.
button.place(x=100, y=200)      # enter coordinates for where to place each widget

"""# text entry"""
input = tkinter.Entry(width=10)     # Entry class from tkinter
input.pack()


"""Kept at the end of ALL code, keeps the mainloop running and the window open"""
window.mainloop()