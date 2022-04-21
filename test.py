from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from req import description, temp, img_data, city, weather_data
import time
import schedule

def can():
    root = Tk()
    # root.geometry('320x320')
    canvas = Canvas(root, width=250, height=220,)
    canvas.pack()
    pilImage = Image.open("/home/sasha/PycharmProjects/weather/day_new.png")
    image = ImageTk.PhotoImage(pilImage)

    canvas.create_image(0, 0, anchor="nw", image=image)

    canvas.create_text(100, 160, text=description, fill="black", font="Verdana 18")
    canvas.create_text(100, 90, text=city, fill="black", font="Verdana 18")
    canvas.create_text(100, 50, text=f"{temp} ℃", fill="black", font="Verdana 24")
    root.mainloop()
    schedule.every(30).seconds.do(weather_data)

    while True:
        schedule.run_pending()
        time.sleep(1)
    can()
# schedule.every(30).seconds.do(can)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

