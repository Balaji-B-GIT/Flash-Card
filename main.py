from operator import indexOf
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_dict = {}
data = pandas.read_csv("data/french_words.csv")
dict_ = data.to_dict(orient="records")

def front_card():
    global random_dict, timer
    window.after_cancel(timer)
    random_dict = random.choice(dict_)
    french_word = random_dict["French"]
    canvas.itemconfig(canvas_image,image = front_img)
    canvas.itemconfig(title, text="French",fill = "black")
    canvas.itemconfig(word, text=french_word,fill = "black")
    timer = window.after(3000, func=back_card)

def back_card():
    eng_word = random_dict["English"]
    canvas.itemconfig(canvas_image,image=back_img)
    canvas.itemconfig(title, text="English",fill = "white")
    canvas.itemconfig(word, text=eng_word,fill = "white")

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
timer = window.after(3000,func = back_card)

canvas = Canvas(width=800,height=526)

front_img = PhotoImage(file = "images/card_front.png")
back_img = PhotoImage(file = "images/card_back.png")
right_img = PhotoImage(file = "images/right.png")
wrong_img = PhotoImage(file = "images/wrong.png")

canvas_image = canvas.create_image(400,263,image = front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))

canvas.grid(row = 0,column = 0,columnspan = 2,sticky=EW)

known_button = Button(image=right_img, highlightthickness=0, command=front_card)
known_button.grid(row=1,column=0)

unknown_button = Button(image=wrong_img, highlightthickness=0, command=front_card)
unknown_button.grid(row=1,column=1)

front_card()

window.mainloop()
