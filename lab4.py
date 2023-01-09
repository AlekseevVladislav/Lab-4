from tkinter import *
from PIL import ImageTk, Image
import string
import random

root = Tk()
root.title("Cs:GO")
root.geometry("1280x720")

def clicked():
    a = random.randint(1,23)
    b = random.randint((a+1),25)
    c = random.sample(string.ascii_letters[a:b+1], b+1-a)
    exit = str(a) + " "
    for i in c:
        exit += i
    exit = exit + " " + str(b)
    print(exit)
    print(a,b)
    print(c)
    canvas1.itemconfig(label1_canvas, text=exit.upper())


bg = ImageTk.PhotoImage(Image.open("123.jpg"))
canvas1 = Canvas(root, width=1280, height=720)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

btn = Button(root, text="Генерировать ключ", command=clicked)

button1_canvas = canvas1.create_window(580, 580, anchor="nw", window=btn)
label1_canvas = canvas1.create_text(630, 550, text="Генерация ключа", fill="white",
                                    font=('Arial 25 bold'))

root.mainloop()