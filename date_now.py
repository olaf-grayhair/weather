import datetime
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

import schedule
import time

root = Tk()

main_frame = tk.Frame(root, width=320, height=320)

now = datetime.datetime.now()
print(now.hour)
if now.hour > 5 and now.hour < 12:
    print('Morning')
elif now.hour > 11 and now.hour < 18:
    print('Afternoon')
elif now.hour > 17 and now.hour < 22:
    print('Evening')
else:
    print('Night')

if now.hour > 19:
    image = Image.open("/home/sasha/PycharmProjects/weather/night_new.png")
    print('pm')
elif now.hour > 8:
    image = Image.open("/home/sasha/PycharmProjects/weather/day_new.png")
    print('am')

# resized_image = Image.open("/home/sasha/PycharmProjects/weather/night.jpg").resize((380, 320))
# resized_image.save('night_new.png')
background = ImageTk.PhotoImage(image)
print(image.size)

label1 = tk.Label(root, image=background)
text = tk.Label(root, text=now)

label1.place(x=0, y=0)
text.place(x=50, y=0)
main_frame.pack()
root.mainloop()

schedule.every(1).seconds.do(print(now))

while True:
    schedule.run_pending()
    time.sleep(1)