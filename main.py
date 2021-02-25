from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_pair = ""


def change_word():
    global random_pair, flip
    screen.after_cancel(flip)
    random_pair = random.choice(words)
    random_word = random_pair["English"]
    card.itemconfig(background, image=front)
    card.itemconfig(language, text="Angielski", fill="Black")
    card.itemconfig(word, text=random_word, fill="Black")
    flip = screen.after(3000, flip_card)


def flip_card():
    card.itemconfig(background, image=back)
    card.itemconfig(language, text="Polski", fill="white")
    card.itemconfig(word, text=random_pair["Polish"], fill="white")

def is_known():
    words.remove(random_pair)
    to_learn = pandas.DataFrame(words)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    change_word()


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/words.csv")

words = data.to_dict(orient="records")

screen = Tk()
screen.title("Learn English")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip = screen.after(3000, flip_card)

card = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
background = card.create_image(400, 263, image=front)
language = card.create_text(400, 150, text="Angielski", font=("Arial", 40, "italic"))
word = card.create_text(400, 283, text="word", font=("Arial", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

button_right = Button(highlightthickness=0, command=is_known)
right = PhotoImage(file="images/right.png")
button_right.config(image=right)
button_right.grid(column=1, row=1)

button_wrong = Button(highlightthickness=0, command=change_word)
wrong = PhotoImage(file="images/wrong.png")
button_wrong.config(image=wrong)
button_wrong.grid(column=0, row=1)

change_word()




screen.mainloop()
