import requests
import os
import schedule
import time

API = 'bf51f443afaae5d5c8d1cec8ba83608c'
city_name = 'kharkov'

def cities():
    name = input('type city: ')
    try:
        print('good')
        return name
    except:
        print('bad')
        return city_name
    # if res.status_code == '200':
    #     print('good city')
    #     return name
    # else:
    #     print('bad city')

def weather_data(city_name):
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q='
                       f'{city_name}&units=metric&appid={API}')
    result = res.json()
    print(res.status_code)
    description = result['weather'][0]['description']
    icon = result['weather'][0]['icon']
    icon_img = f'https://openweathermap.org/img/wn/{icon}@2x.png'
    wind = result['wind']['speed']
    temp = round(result['main']['temp'])
    temp_max = result['main']['temp_max']
    temp_min = result['main']['temp_min']
    feels_like = result['main']['feels_like']
    pressure = result['main']['pressure']
    humidity = result['main']['humidity']
    city = result['name']
    response = requests.get(icon_img)
    img_data = response.content
    return description, temp, img_data, city

description, temp, img_data, city = weather_data('london')


schedule.every(30).seconds.do(weather_data, 'kharkov')

while True:
    schedule.run_pending()
    time.sleep(1)

# def write_file(file):
#     if os.path.exists(f'{file}.json'):
#         print('This file is already exist!')
#     else:
#         with open(f'{file}.json', 'w') as f:
#             f.write(res.text)
#         print('File writed successfully')

