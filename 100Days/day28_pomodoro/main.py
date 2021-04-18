from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
"""Create the app's window"""
window = Tk()
"""# set the title"""
window.title("Aaron's Pomodoro")
window.minsize(400,500)
window.config(bg=YELLOW)     # adds padding to the window's borders
canvas = Canvas(width=400, height=500, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="100Days\day28_pomodoro/tomato.png")
canvas.create_image(200, 225, image=tomato_image)
canvas.create_text(200, 250, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()

window.mainloop()