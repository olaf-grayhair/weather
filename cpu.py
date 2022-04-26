import psutil
import PySimpleGUI as sg
import time

current_cpu = psutil.cpu_freq().current
# print(psutil.cpu_count())


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


def usage():
    cpu = psutil.cpu_percent(interval=0, percpu=True)
    mb = 1024 ** 2
    bytes_sent = psutil.net_io_counters(pernic=True)['enp6s0'][0]
    bytes_recv = psutil.net_io_counters(pernic=True)['enp6s0'][1]
    print(f'bytes_recv {round(bytes_recv / mb, 2)} / bytes_sent {round(bytes_sent / mb, 2)}')
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
# print(psutil.sensors_temperatures())

cpu = [[sg.Text('CPU usage')],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='cpu1'), sg.Text('0%', key='cpu%1')],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='cpu2'), sg.Text('0%', key='cpu%2')],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='cpu3'), sg.Text('0%', key='cpu%3')],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='cpu4'), sg.Text('0%', key='cpu%4')],
          [sg.Button('Quit', pad=(0, 60))]]
layout = [[sg.Text('0G', key='memText')],
         [sg.ProgressBar(100, orientation='м', pad=(30, 30),
                          bar_color=(color_use(), '#FFF'), size=(20, 40), key='mem'),sg.Column(cpu)]]
# 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative'
window = sg.Window('Custom Progress Meter', layout)
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

    window['cpu%1'].update(f'{round(cpu[0])}%')
    window['cpu%2'].update(f'{round(cpu[1])}%')
    window['cpu%3'].update(f'{round(cpu[2])}%')
    window['cpu%4'].update(f'{round(cpu[3])}%')
    #mem
    total, percent, used, available = mem_use()
    window['mem'].UpdateBar(percent)
    window['memText'].update(f'{round(used, 2)}G/{round(total, 2)}G')

window.close()