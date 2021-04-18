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

def reset_button_click():
    pass

# # ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_button_click():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 



# ---------------------------- UI SETUP ------------------------------- #
"""Create the app's window"""
window = Tk()
"""# set the title"""
window.title("Aaron's Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)     # adds padding to the window's borders

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="100Days\day28_pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

"""# create the 'Check mark' label"""
check_mark_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
check_mark_label.grid(column=1, row=4)     # parameters to convey display instructions
# check_mark_label.config(pady=5)

"""# create the 'Timer' label"""
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
timer_label.grid(column=1, row=0)     # parameters to convey display instructions
# timer_label.config(pady=5)

"""# create the start button"""
start_button = Button(text="start", fg=RED, font=(FONT_NAME, 12, "bold"), command=start_button_click, highlightthickness=0)
start_button.grid(column=0, row=2)     # enter grid coordinates for where to place each widget
# start_button.config(pady=5, padx=5)

"""# create the reset button"""
reset_button = Button(text="reset", fg=RED, font=(FONT_NAME, 12, "bold"), command=reset_button_click, highlightthickness=0)
reset_button.grid(column=2, row=2)     # enter grid coordinates for where to place each widget
# reset_button.config(pady=5, padx=5)

window.mainloop()