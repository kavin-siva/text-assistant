import time
import os
from plyer import notification
from functions import speak


def reminder():
    variable = ''
    try:
        with open('reminder_time.txt', 'r') as f:
            variable = f.readline()
            message = f.readline()
    except:
        speak('What would you like me to remind you about ')
        message = input()
    if variable == '':

        hor = int(input('What is the hour: '))
        minn = int(input('What is the minute: '))
        sec = int(input('What is the seconds: '))

        with open('reminder_time.txt', 'a') as f:
            f.write(f'{hor}{minn}{sec}\n')
            f.write(message)
    else:
        hor = int(variable[0:2])
        minn = int(variable[2:4])
        sec = int(variable[4:])
    print('Reminder is set ')
    while True:
        if time.localtime().tm_hour == hor and time.localtime().tm_min == minn and time.localtime().tm_sec == sec:

            print('Reminder Alert *** Check your Notifications *** ')
            os.remove('reminder_time.txt')
            break

    notification.notify(
        title='Reminder',
        message=message,
        timeout=12

    )

    input()


reminder()
