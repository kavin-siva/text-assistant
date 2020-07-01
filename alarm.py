from pygame import mixer
import time
import playsound


def alarm():
    hor=int(input('What is the hour: '))
    minn=int(input('What is the minute: '))
    sec=int(input('What is the seconds: '))

    n=0

    print(f'Alarm set for {str(hor)}:{str(minn)}:{str(sec)}. ')
    while True:
        if time.localtime().tm_hour==hor and time.localtime().tm_min==minn and time.localtime().tm_sec==sec:
            print('The Alarm has ended. ')
            break

    while n<=15:
        playsound.playsound('alarm_music.mp3')
        time.sleep(2)
alarm()