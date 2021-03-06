import PySimpleGUI as sg
import requests
import datetime

# Define the window's contents
API = 'bf51f443afaae5d5c8d1cec8ba83608c'

def clocker():
    now = datetime.datetime.now()
    if now.hour > 22 and now.hour < 5:
        print('n')
        return 'Night'
    elif now.hour > 5 and now.hour < 12:
        return 'Morning'
    elif now.hour > 12 and now.hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'

# def cities(name):
#     if geo(name).status_code == 200 and name != '':
#         print('good city')
#     else:
#         print('bad city')
#         return

def geo(city_feeld):
    return requests.get(f'https://api.openweathermap.org/data/2.5/weather?q='
                       f'{city_feeld}&units=metric&appid={API}')

def weather_data(name):
    city_name = 'kharkov'
    if name != '' and geo(name).status_code == 200:
        result = geo(name).json()
        print('TRY', result)
    else:
        result = geo(city_name).json()
        print('EXCEPT', result)
    description = result['weather'][0]['description']
    temp = round(result['main']['temp'])
    city = result['name']
    icon = result['weather'][0]['icon']
    icon_img = f'https://openweathermap.org/img/wn/{icon}@2x.png'
    response = requests.get(icon_img)
    img_data = response.content
    return description, temp, img_data, city, name
    #GUI INTERFACE
description, temp, img_data, city, name = weather_data('kharkov')

sg.theme('DarkBlue1')
layout = [
          [sg.Input(key='-INPUT-', size=30), sg.Button('Ok')],
          [sg.Text(city, font=('Philosopher, 26'), key='-CITY-')],
          [sg.Text(f"{temp} ℃", font=('Philosopher, 26'), key='-TEMP-'), sg.Image(img_data, key='-IMG-')],
          [sg.Text(description, key='-DESCRIPTION-'), sg.Text(f'{clocker()}', pad=(30, 10), key='clock')],
          # [sg.Button('Ok'), sg.Button('Quit')]
]
# Create the window
window = sg.Window('Weather', layout, alpha_channel=0.8)
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read(timeout=30000)
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    name = values['-INPUT-']
    description, temp, img_data, city, name = weather_data(name)
    window['-CITY-'].update(city)
    window['-TEMP-'].update(f"{temp} ℃")
    window['-IMG-'].update(img_data)
    window['-DESCRIPTION-'].update(description)

window.close()


