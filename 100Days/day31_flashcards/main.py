from tkinter import *

BACKGROUND_COLOUR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOUR)     # adds padding to the window's borders

front_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOUR, highlightthickness=0)
front_image = PhotoImage(file="100Days\day31_flashcards\images\card_front.png")
front_canvas.create_image(400, 263, image=front_image)
title_text = front_canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 36, "italic"))
word_text = front_canvas.create_text(400, 250, text="Word", fill="black", font=("Arial", 54, "bold"))
front_canvas.grid(column=1, row=0)

"""# create the 'Check mark' label"""
right_canvas = Canvas(width=100, height=100, bg=BACKGROUND_COLOUR, highlightthickness=0)
right_image = PhotoImage(file="100Days\day31_flashcards\images/right.png")
right_canvas.create_image(100, 112, image=right_image)
right_canvas.grid(column=1, row=1)

# """# create the 'Timer' label"""
# timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
# timer_label.grid(column=1, row=0)     # parameters to convey display instructions

# """# create the start button"""
# start_button = Button(text="start", fg=RED, font=(FONT_NAME, 12, "bold"), command=start_button_click, highlightthickness=0)
# start_button.grid(column=0, row=2)     # enter grid coordinates for where to place each widget



window.mainloop()