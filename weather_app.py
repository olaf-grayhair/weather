import tkinter as tk
from tkinter import ttk
from req import description, temp, img_data, city
from PIL import ImageTk, Image
from io import BytesIO

window = tk.Tk()
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

window.title('Weather app')

main_frame = tk.Frame(window, width=250, height=200, bg='#88B04B')
rain = tk.Label(window, text=description, bg='black', fg='#FFF', font=('Times', 18))
city_name = tk.Label(window, text=city, bg='#88B04B', fg='#FFF', font=('Times', 20))
temperature = tk.Label(window, text=f"{temp} ℃", bg='#88B04B', fg='#FFF', font=('Times', 24))
images = tk.Label(window, image=img, bg='#88B04B', fg='#FFF', font=('Times', 28))

image = Image.open("/home/sasha/PycharmProjects/weather/night_new.png")
background = ImageTk.PhotoImage(image)
bg_img = tk.Label(main_frame, image=background)
bg_img.place(x=0, y=0)

password = tk.StringVar(window)
password_entry = ttk.Entry(window, textvariable=password)

city = []
def login_clicked():
    city.append(password_entry.get())
    print(city)
    city.pop()

button = tk.Button(
    window,
    text="Submit!",
    bg="blue",
    fg="yellow",
    command=login_clicked
)

main_frame.grid(row=0, column=0, sticky='w')
password_entry.grid(row=0, column=0, sticky='nw', padx=10, pady=10)
button.grid(row=0, column=0, sticky='ne', padx=10, pady=10)
rain.place(x=10, y=160)
temperature.place(x=10, y=90)
city_name.place(x=10, y=50)
images.place(x=100, y=50)


window.mainloop()
