import tkinter

window = tkinter.Tk()
# set the title -
window.title("My first GUI program")
# set the minimum window size -
window.minsize(800,800)

# create a label -
label = tkinter.Label(text="It's ya boy Label!", font=("Arial", 22, "italic"))
# display the label (call the packer) -
label.pack()     # parameters to convey display instructions

label["text"] = "New Text"
label.config(text="New Text")


















"""Kept at the end of ALL code, keeps the mainloop running and the window open"""
window.mainloop()