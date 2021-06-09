from tkinter import *
import pandas
import random

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



#-------------------Function-------------------

def next_card():
    global current_row,timer
    window.after_cancel(timer)
    current_row=random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(title, text="French",fill="black")
    canvas.itemconfig(word,text=current_row["French"],fill="black")
    timer=window.after(3000,flip_card)


def flip_card():
    canvas.itemconfig(canvas_image,image=back)
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=current_row["English"],fill="white")


def is_known():
    to_learn.remove(current_row)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#__________UI________________


# ------------window----------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
timer=window.after(3000,flip_card)

# -----Card-Front------

canvas = Canvas(width=800, height=536,bg=BACKGROUND_COLOR,highlightthickness=0)
front = PhotoImage(file=".\images\card_front.png")
back = PhotoImage(file=".\images\card_back.png")
canvas_image=canvas.create_image(400, 268, image=front)
title=canvas.create_text(400,100,text="",font=("Aerial",60,"italic"))
word=canvas.create_text(400,268,text="",font=("Aerial",40,"bold"))
canvas.grid(row=1, column=1,columnspan=2)



# button-wrong

logo_wrong = PhotoImage(file=".\images\wrong.png")
button_wrong= Button(image=logo_wrong,command=next_card)
button_wrong.grid(row=2, column=1)

# button-right
logo_right = PhotoImage(file="tick.png")
button_right = Button(image=logo_right,command=is_known)
button_right.grid(row=2, column=2)

next_card()



window.mainloop()
