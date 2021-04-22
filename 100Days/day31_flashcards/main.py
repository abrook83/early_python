from tkinter import *
import random
import pandas

BACKGROUND_COLOUR = "#B1DDC6"
FIRST_WORD = 1
LAST_WORD = 100

# -------------------------- SELECT WORDS------------------------------ #

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("100Days\day31_flashcards\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("100Days\day31_flashcards\data\german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")       # add code to select from a range of words in the list....


def next_card():
    """Goes to the next card when prompted."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="German", fill="black")
    canvas.itemconfig(word_text, text=current_card["German"], fill="black")
    canvas.itemconfig(card_bg, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flip a card (change the look to white on green) after the 3sec timer."""
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_image)


def word_known():
    """If a word is known (ticked), then remove it from the dataframe."""
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("100Days\day31_flashcards\data/words_to_learn.csv", index=False)    # 'index=False' removes the indexing of entries when adding to .csv
    next_card()     # after removing the known word, then move to next card.

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOUR)     # adds padding to the window's borders

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOUR, highlightthickness=0)
front_image = PhotoImage(file="100Days\day31_flashcards\images\card_front.png")
back_image = PhotoImage(file="100Days\day31_flashcards\images\card_back.png")
card_bg = canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 150, fill="black", font=("Arial", 36, "italic"))
word_text = canvas.create_text(400, 250, fill="black", font=("Arial", 54, "bold"))
canvas.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

"""# create the 'right' mark label"""
right_image = PhotoImage(file="100Days\day31_flashcards\images/right.png")
right_button = Button(image=right_image, width=100, height=100, bg=BACKGROUND_COLOUR, command=word_known, highlightthickness=0)
right_button.grid(column=0, row=1)

"""# create the 'wrong' mark label"""
wrong_image = PhotoImage(file="100Days\day31_flashcards\images\wrong.png")
wrong_button = Button(image=wrong_image, width=100, height=100, bg=BACKGROUND_COLOUR, command=next_card, highlightthickness=0)
wrong_button.grid(column=1, row=1)

next_card()

window.mainloop()