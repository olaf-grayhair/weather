import psutil
import PySimpleGUI as sg
import time
import os

kernel = os.uname()[2]
version = os.uname()[3].split(' ')[0].split('~')[1]
machine = os.uname()[4]

def uptime():
    return os.popen('uptime -p').read()[:-1].split('up')[1].replace(' ', '', 1)
def cpu_mhz():
    # print(psutil.cpu_count())
    # print(current_cpu)
    real = round(psutil.cpu_freq().current, 3)
    current_cpu = str(real).replace('.', '')
    if len(current_cpu) < 4:
        current_cpu = current_cpu + '0'
    current_cpu = int(current_cpu)
    print(current_cpu)
    return current_cpu

def color_use():
    percent = psutil.virtual_memory().percent
    if round(percent) > 70:
        return '#9B2335'
    elif round(percent) > 50:
        return '#955251'
    elif round(percent) > 30:
        return '#FF6F61'
    else:
        return '#88B04B'

def rep(cpu, num):
    return cpu.replace('shwtemp', '').replace(',', '').replace('(', '').replace(')', '').split()[num].replace('current=', '')

def usage():
    cpu = psutil.cpu_percent(interval=0, percpu=True)
    #network data
    mb = 1024 ** 2
    bytes_sent = psutil.net_io_counters(pernic=True)['enp6s0'][0]
    bytes_recv = psutil.net_io_counters(pernic=True)['enp6s0'][1]
    # print(f'bytes_recv {round(bytes_recv / mb, 2)} / bytes_sent {round(bytes_sent / mb, 2)}')
    return cpu


def mem_use():
    mb = 1024 ** 3
    available = psutil.virtual_memory().available / mb
    used = psutil.virtual_memory().used / mb
    total = psutil.virtual_memory().total / mb
    percent = psutil.virtual_memory().percent
    # print(f'available: {round(available, 2)}G use: {round(used, 2)}G percent: {percent}% total: {round(total, 1)}G')
    return total, percent, used, available

# print(psutil.cpu_stats())

def temperatures():
    temp = psutil.sensors_temperatures()
    cpu_temp = rep(str(temp['coretemp'][0]), 3)
    gpu_temp = rep(str(temp['radeon'][0]), 1)
    # print(temp)
    # cpu_temp1 = rep(str(temp['coretemp'][1]), 2)
    # cpu_temp2 = rep(str(temp['coretemp'][2]), 2)
    # cpu_temp3 = rep(str(temp['coretemp'][3]), 2)
    # cpu_temp4 = rep(str(temp['coretemp'][4]), 2)
    return gpu_temp, cpu_temp
#gui
sg.theme('black')

# sg.theme_previewer()
cpu = [
    [sg.Text('CPU usage'), sg.Text('1999MHz', pad=(80, 0), key='mhz', text_color='#00FF00')],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='cpu1'), sg.Text('0%', key='cpu%1', text_color='#00FF00')],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='cpu2'), sg.Text('0%', key='cpu%2', text_color='#00FF00')],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='cpu3'), sg.Text('0%', key='cpu%3', text_color='#00FF00')],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='cpu4'), sg.Text('0%', key='cpu%4', text_color='#00FF00')],
          [sg.Text('CPU temperature'), sg.Text('0', key='cpu_temp', text_color='#00FF00', pad=(50, 0))],
          [sg.Text('GPU temperature'), sg.Text('0', key='gpu_temp', text_color='#00FF00', pad=(50, 0))],
       ]

mem = [
         [sg.Text('Memory', pad=(0, 0)), sg.Text('1999MHz', pad=(80, 0), key='mhz', text_color='#00FF00')],
         [sg.ProgressBar(100, orientation='h', pad=(0, 0), bar_color=(color_use(), '#FFF'), size=(20, 20), key='mem'),
          sg.Text('0G', key='memText', pad=(10, 0), text_color='#00FF00')]
]

date = [
    [sg.Text('Uptime: '), sg.Text(f'{uptime()}', text_color='#00FF00', pad=(74, 0), key='uptime')],
    [sg.Text('Distribution: '), sg.Text(f'{version} {machine}', text_color='#00FF00', pad=(40, 0))],
    [sg.Text('Kernel: '), sg.Text(kernel, text_color='#00FF00', pad=(79, 0))],
]
layout = [
    [sg.Column(date)],
    [sg.HorizontalSeparator(pad=(0, 20))],
    [sg.Column(cpu)],
    [sg.HorizontalSeparator(pad=(0, 20))],
    [sg.Column(mem)],
    [sg.Button('Quit', pad=(0, 10))]
]

# 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative'
window = sg.Window('Custom Progress Meter', layout, no_titlebar=True,
                   location=(700, 30), margins=(10, 20),

                   font=('Ubuntu', 11, 'bold'))
# loop that would normally do something useful
while True:
    # check to see if the cancel button was clicked and exit loop if clicked
    event, values = window.read(timeout=1000)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # cpu1, cpu2, cpu3, cpu4 = usage()
    cpu = usage()
    window['cpu1'].UpdateBar(cpu[0])
    window['cpu2'].UpdateBar(cpu[1])
    window['cpu3'].UpdateBar(cpu[2])
    window['cpu4'].UpdateBar(cpu[3])
    #cpu_temp
    gpu_temp, cpu_temp = temperatures()
    window['cpu_temp'].update(f'{cpu_temp}℃')
    window['gpu_temp'].update(f'{gpu_temp}℃')
    window['cpu%1'].update(f'{round(cpu[0])}%')
    window['cpu%2'].update(f'{round(cpu[1])}%')
    window['cpu%3'].update(f'{round(cpu[2])}%')
    window['cpu%4'].update(f'{round(cpu[3])}%')
    window['mhz'].update(f'{cpu_mhz()}MHz')
    #mem
    total, percent, used, available = mem_use()
    window['mem'].UpdateBar(percent)
    window['memText'].update(f'{round(used, 1)}G/{round(total, 1)}G')
    #update
    window['uptime'].update(f'{uptime()}')

window.close()
