# -------------------------------- imports -------------------------------- #
from tkinter import *
import pandas as pd
import random

# ------------------------------- constants ------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = None
data = {}


# ------------------------------- functions ------------------------------ #
def next_card():
    global current_card, flip_timer 
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=front_card) 
    flip_timer = window.after(3000, flip_card)
    
def flip_card():
    canvas.itemconfig(card_image, image=back_card)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    
def is_known():
    data.remove(current_card)
    df = pd.DataFrame(data)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    
# ------------------------------- data ------------------------------ #
try:
    data = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data = original_data.to_dict(orient="records")
else:
    data = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
    

# -------------------------------- UI/UX --------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")

canvas.config(bg=BACKGROUND_COLOR,  highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)  

# Buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      highlightcolor=BACKGROUND_COLOR, command=is_known )
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      highlightcolor=BACKGROUND_COLOR, command=next_card )
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()