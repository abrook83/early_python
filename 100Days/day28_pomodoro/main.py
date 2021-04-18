from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_REPETITIONS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_button_click():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    global TIMER_REPETITIONS
    TIMER_REPETITIONS = 0

# # ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_button_click():
    global TIMER_REPETITIONS
    TIMER_REPETITIONS += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if TIMER_REPETITIONS == 8:
        countdown_timer(long_break_seconds)
        timer_label.config(text="Break", fg=RED)
    elif TIMER_REPETITIONS % 2 == 0:
        countdown_timer(short_break_seconds)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown_timer(work_seconds)
        timer_label.config(text="Work!", fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_timer(count):
    """Countdown from the input time, create a mins & secs count."""
    min_left = math.floor(count / 60)       # rounds down to the nearest integer
    sec_left = count % 60
    if sec_left < 10:
        sec_left = f"0{sec_left}"
    canvas.itemconfig(timer_text, text=f"{min_left}:{sec_left}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown_timer, count - 1)
    else:
        start_button_click()
        tick_count = ""
        for _ in range(math.floor(TIMER_REPETITIONS/2)):
            tick_count += "✔"
        check_mark_label.config(text=tick_count)


# ---------------------------- UI SETUP ------------------------------- #
"""Create the app's window"""
window = Tk()
"""# set the title"""
window.title("Aaron's Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)     # adds padding to the window's borders

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="100Days\day28_pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

"""# create the 'Check mark' label"""
check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
check_mark_label.grid(column=1, row=4)     # parameters to convey display instructions

"""# create the 'Timer' label"""
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
timer_label.grid(column=1, row=0)     # parameters to convey display instructions

"""# create the start button"""
start_button = Button(text="start", fg=RED, font=(FONT_NAME, 12, "bold"), command=start_button_click, highlightthickness=0)
start_button.grid(column=0, row=2)     # enter grid coordinates for where to place each widget

"""# create the reset button"""
reset_button = Button(text="reset", fg=RED, font=(FONT_NAME, 12, "bold"), command=reset_button_click, highlightthickness=0)
reset_button.grid(column=2, row=2)     # enter grid coordinates for where to place each widget


window.mainloop()