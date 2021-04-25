from tkinter import *
import requests


def get_quote():
    source = requests.get(url="https://api.kanye.rest/")    # access the API
    source.raise_for_status()   # display appropiate errors
    quote = source.json()["quote"]  # retrive the quote from the API
    canvas.itemconfig(quote_text, text=quote)   # pass the quote to the 'quote_text' canvas


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="100Days\day33_APIs/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="100Days\day33_APIs\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()