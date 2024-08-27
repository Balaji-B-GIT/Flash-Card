from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

data = pandas.read_csv("data/french_words.csv")


canvas = Canvas(width=800,height=526)

front_img = PhotoImage(file = "images/card_front.png")
back_img = PhotoImage(file = "images/card_back.png")
right_img = PhotoImage(file = "images/right.png")
wrong_img = PhotoImage(file = "images/wrong.png")

canvas.create_image(400,263,image = front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

canvas.create_text(400,150,text="title",font=("Ariel",40,"italic"))
canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))

canvas.grid(row = 0,column = 0,columnspan = 2,sticky=EW)

known_button = Button(image=right_img,highlightthickness=0)
known_button.grid(row=1,column=0)

unknown_button = Button(image=wrong_img,highlightthickness=0)
unknown_button.grid(row=1,column=1)














window.mainloop()
