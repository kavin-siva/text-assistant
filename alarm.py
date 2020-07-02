from pygame import mixer
import time
import playsound
import os
mixer.init()
mixer.music.load('audio files/alarm_music.mp3')


def alarm():
    variable = ''
    try:
        with open('alarm_time.txt', 'r') as f:
            variable = f.read()
    except:
        pass
    if variable == '':
        hor = int(input('What is the hour: '))
        minn = int(input('What is the minute: '))
        sec = int(input('What is the seconds: '))

        with open('alarm_time.txt', 'w') as f:
            f.write(f'{hor}{minn}{sec}')
    else:
        hor = int(variable[0:2])
        minn = int(variable[2:4])
        sec = int(variable[4:])
    print(f'Alarm set for {str(hor)}:{str(minn)}:{str(sec)}. ')
    while True:
        if time.localtime().tm_hour == hor and time.localtime().tm_min == minn and time.localtime().tm_sec == sec:

            print('The Alarm has ended. ')
            os.remove('alarm_time.txt')
            break

    mixer.music.play()
    input()


alarm()
