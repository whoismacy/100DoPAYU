import random

import pandas

from tkinter import *

# TODO 1 Clean the Data using csv
# TODO 2 Assign the Data to a list.
# TODO 3 Create a Window
# TODO 4 Create 4 PhotoImages, two for the button (image=)

BACKGROUND_COLOR = "#B1DDC6"
to_learn = dict()

try:
    data = pandas.read_csv("datas.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("estoen.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = dict()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="Espanol", fill="black")
    canvas.itemconfig(center_text, text=current_card['es'], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(center_text, text=current_card['en'], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

def is_known():
    to_learn.remove(current_card)
    datas = pandas.DataFrame(to_learn)
    datas.to_csv("words_to_learn.csv")
    next_card()
# Creating a window
window = Tk()
window.title("Flash Cards Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(ms=3000, func=flip_card)

# Creating the PhotoImages
card_back = PhotoImage(file="card_back.png")
card_front = PhotoImage(file="card_front.png")
right = PhotoImage(file="right.png")
wrong = PhotoImage(file="wrong.png")

# Creating the Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(400, 150, text="", anchor="center", font=("Courier", 30, "italic"))
center_text = canvas.create_text(400, 263, text="", anchor="center", font=("Courier", 35, "bold"))

# Creating the Buttons
r_button = Button(image=right, command=next_card,bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, border=0)
r_button.grid(column=1, row=1)

w_button = Button(image=wrong, command=is_known, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, border=0)
w_button.grid(column=0, row=1)

next_card()

window.mainloop()
