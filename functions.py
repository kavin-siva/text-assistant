from time import ctime
import time
from PyDictionary import PyDictionary
import speech_recognition as sr
import webbrowser
import playsound
import os
import random
from gtts import gTTS
import subprocess


def _respond(client):

    client = client.replace(" ", "")
    client = client.lower()

    if "name" in client:
        speak_name()

    if "weight converter" in client:
        speak_weight_converter()


    elif "stopwatch" in client:
        stopwatch()

    elif "alarm" in client:
        alarm()

    elif "dictionary" in client:
        speak_dictionary()

    elif "cubetimer" in client:
        speak_cubetimer()

    elif "time" in client:
        speak_time()

    elif "weather" in client:
        speak_weather()

    elif "calculat" in client:
        speak_calculator()

    elif "compliment" in client:
        speak_compliment()

    elif "mood" in client and "good" in client and "no" in client:
        speak_mood()

    elif "depressed" in client and "feeling" in client:
        speak_feelings()

    elif "browse" in client:
        speak_browse()

    elif "location" in client:
        speak_location()

    elif "temperature" in client:
        speak_temperature()

    elif "humidity" in client:
        speak_humidity()

    elif "cool" in client:
        speak_cool()

    elif "marryme" in client:
        speak_marry()

    elif "love" in client and "you" in client:
        speak_love()

    elif "dang" in client:
        speak_dang()

    elif "goodmorning" in client:
        speak_greetings()

    elif "smart" in client:
        speak_smart()

    elif "goodnight" in client:
        speak_goodnight()

    elif "music" in client:
        speak_music()

    elif "rolladice" in client:
        speak_dice()

    elif "flipacoin" in client:
        speak_coin()

    elif "video" in client:
        speak_video()

    elif "youtube" in client:
        speak_youtube()

    elif "chess" in client:
        speak_chess()

    elif "cube" in client and "trainer" in client:
        speak_cubetrainer()

    elif "cube" in client and "tutorial" in client:
        speak_cubetutorial()

    elif "hangouts" in client:
        speak_googlehangouts()

    elif "game" in client:
        speak_games()

    elif "exit" in client:
        speak_exit()

    elif "thankyou" in client:
        speak_thankyou()

    else:
        client = did_you_mean(client)
        _respond(client)


functions_string = {
    "dictionary_function": "dictionary",
    "alarm_functions": "alarm",
    "music_functions": "music",
    "name_function": "name",
    "time_function": "what time is it",
    "weather_function": "weather",
    "calculator_function": "calculator",
    "compliment_function": "compliment",
    "mood_function": "i am not in a mood",
    "feelings_function": "i am feeling depressed",
    "browse_function": "browse",
    "location_function": "find location",
    "temperature_function": "temperature",
    "humidity_function": "humidity",
    "cool_function": "cool",
    "dang_function": "dang",
    "marry_function": "will you marry me",
    "love_function": "i love you",
    "greeting_function": "good morning",
    "smart_function": "you are smart",
    "goodnight_function": "good night",
    "relaxmusic_function": "relaxing music",
    "coin_function": "flip a coin",
    "dice_function": "roll a dice",
    "video_function": "video",
    "youtube_function": "youtube",
    "chess_function": "chess",
    "cubetrainer_function": "cube trainer",
    "cubetutorial_function": "cube tutorial",
    "googlehangouts_function": "google hangouts",
    "cubetimer_function": "cube timer",
    "games_function": "games",
    "weight_converter_function":"weight converter",
    "thankyou_function": "thank you",
    "exit_function": "exit",
}

r = sr.Recognizer()

dictionary = PyDictionary()


def jarvis_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def speak_dictionary():
    word = input("which word would you like me to define ")
    jarvis_speak(str(dictionary.meaning(word)))
    speak_anythingelse()

def speak_weight_converter():
    weight = input('Weight: ')

    unit = input('Is the weight in (L)lbs (K)kg: ')

    if unit.upper() == 'L':
        final1 = (.45) * int(weight)
        print(f'The weight is {final1} kilos ')

    else:
        final1 = (.45) / int(weight)
        print(f'The weight is {final1} pounds ')



def alarm():
    subprocess.call(["dist/alarm/alarm.exe"])


def speak_location():
    location = str(input("What location would you like to look for? "))
    url = f"https://google.nl/maps/place/{location}/&amp;"
    webbrowser.get().open(url)
    jarvis_speak("Here is what I found for " + location)
    speak_anythingelse()


def speak_time():
    jarvis_speak(str(ctime()))


def did_you_mean(input_string):
    input_list = remove_more_less(functions_string, input_string)
    jarvis_speak("Sorry I did not catch that. ")
    sixty = round((len(input_string) * 0.6))
    input_list_string = list(input_string)
    for i in range(0, len(input_list) - 1):
        n = 0
        for j in range(0, len(input_list[i]) - 1):
            try:
                if input_list_string[j] in input_list[i]:
                    n += 1
            except IndexError:
                continue
            if n >= sixty:
                jarvis_speak(f"Did you mean {input_list[i]}")
                new_input = input()
                new_input = new_input.lower()
                if "y" in new_input:
                    m = 1
                    n = 0
                    _respond(input_list[i])
                else:
                    jarvis_speak("What do you want me to do then? ")
                break
    jarvis_speak("please type that again. ")


def remove_more_less(input_dictionary, input_string):
    input_list = list(input_dictionary.values())
    extra_list = []
    length_string = len(input_string)
    for i in range(0, len(input_list) - 1):
        if len(input_list[i]) != length_string:
            extra_list.append(input_list[i])
    for i in range(0, len(extra_list)):
        input_list.remove(extra_list[i])
    input_list.pop()
    return input_list


def stopwatch():
    import time

    while True:
        try:
            input("Press Enter to continue,CTRL-C To exit")
            start_time = time.time()
            print("Timer has started")
            while True:
                print(
                    "Time elapsed=:",
                    round(time.time() - start_time, 0),
                    "sec",
                    end="\n",
                )
                time.sleep(1)
        except KeyboardInterrupt:
            print("Timer has stopped")
            end_time = time.time()
            print("The time elapsed is", round(end_time - start_time, 2), "secs")
            break


def convert_alarm_time(given_alarm_time):

    month = str(ctime()[4:7])
    year = str(ctime()[20:])
    if month == "Jan":
        month = 1
    elif month == "Feb":
        month = 2
    elif month == "Mar":
        month = 3
    elif month == "Apr":
        month = 4
    elif month == "May":
        month = 5
    elif month == "Jun":
        month = 6
    elif month == "Jul":
        month = 7
    elif month == "Aug":
        month = 8
    elif month == "Sep":
        month = 9
    elif month == "Oct":
        month = 10
    elif month == "Nov":
        month = 11
    elif month == "Dec":
        month = 12

    date = str(ctime()[8:10])

    date_time = f"{date}.0{month}.{year} {given_alarm_time}:00"
    pattern = "%d.%m.%Y %H:%M:%S"
    epoch = int(time.mktime(time.strptime(date_time, pattern)))


def speak_anythingelse():
    jarvis_speak("Is there anything else you want me to do. ")
    answer = input()
    if "no" in answer:
        jarvis_speak("Ok no problem, you can ask me anything later. ")
        exit()
    elif "yes" in answer:
        jarvis_speak("What can I do for you. ")
        _respond(input())
    else:
        _respond(answer)


def speak_calculator():
    jarvis_speak("What do you want to calculate ")
    equation = input()
    for i in range(0, len(equation) - 1):
        if (
            equation[i] == "+"
            or equation[i] == "-"
            or equation[i] == "*"
            or equation[i] == "/"
        ):
            operator = equation[i]
            term1 = int(equation[0:i])
            term2 = int(equation[i + 1 :])

    if operator == "+":
        jarvis_speak(str(term1 + term2))
    elif operator == "-":
        jarvis_speak(str(term1 - term2))
    elif operator == "*":
        jarvis_speak(str(term1 * term2))
    else:
        jarvis_speak(str(term1 / term2))
    speak_anythingelse()


def speak_weather():
    from pyowm.owm import OWM

    owm = OWM("579ed7bb39f3bf7816212b6fadd195d3")
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place("Chennai").weather
    jarvis_speak("The humidity percentage is " + str(weather.humidity))
    jarvis_speak(
        "The temperature in fahrenheit is "
        + str(round(1.8 * (weather.temp["temp"] - 273) + 32))
    )
    jarvis_speak("The weather status is " + str(weather.to_dict()["detailed_status"]))
    speak_anythingelse()


def speak_games():
    jarvis_speak("What game do you want to play")
    input1 = input("A game on the web or guess the number.")
    if "number" in input1:
        number = random.randrange(1, 50)
        guess = int(input("Guess a number between 1 and 50: "))

        while guess != number:
            if guess < number:
                print("You need to guess higher, Try again ")
                guess = int(input("\nGuess a number between 1 and 50: "))

            if guess < number:
                print("You need to guess lower, Try again: ")
                guess = int(input("\nGuess a number between 1 and 50: "))

            else:
                print("Great, You guessed the number correctly. ")
                break
    if "web" in input1:
        url = "https://www.kongregate.com/"
        webbrowser.get().open(url)

    speak_anythingelse()


def speak_name():
    jarvis_speak("My name is Jarvis. ")
    speak_anythingelse()


def speak_chess():
    url = "www.chess.com"
    webbrowser.get().open(url)
    jarvis_speak("I hope you win your chess match ")


def speak_compliment():
    jarvis_speak(
        "I admire you. You can do it. I value you. You can count on me. I believe in you. You are kind. I trust you. You are smart. "
    )
    speak_anythingelse()


def speak_mood():
    jarvis_speak("well seeing you in this mood makes me sad ")
    jarvis_speak("I think you had a tough day")
    jarvis_speak("lets relax ")
    url = "www.youtube.com"
    webbrowser.get().open(url)
    speak_anythingelse()


def speak_feelings():
    jarvis_speak(
        "I admire you. You can do it. I value you. You can count on me. I believe in you. You are kind. I trust you. You are smart. "
    )
    jarvis_speak("how about we relax")
    url = "www.youtube.com"
    webbrowser.get().open(url)
    speak_anythingelse()


def speak_browse():
    find = str(input("What would you like to browse "))
    find = find.replace(" ", "+")
    url = f"https://google.com/search?q={find}"
    webbrowser.get().open(url)
    jarvis_speak("Here is what I found for " + find)
    speak_anythingelse()


def speak_greetings():
    jarvis_speak("Good Morning to you to")
    jarvis_speak("It is ")
    jarvis_speak(ctime())
    jarvis_speak("You better get going now, as today is a big day. ")
    speak_anythingelse()


def speak_goodnight():
    jarvis_speak("Good Night to you as well")
    jarvis_speak("Sleep tite and do not let the bed bugs bite. ")
    jarvis_speak(ctime())
    # add alarm after 8 hours with clients permission


def speak_cubetutorial():
    cubetutorial = input(
        "Which instructor would you like to have,  " "Jperm, Brody the cuber: "
    )
    cubetutorial = cubetutorial.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={cubetutorial}"
    webbrowser.get().open(url)
    jarvis_speak("I hope you learn something new in cubing ")
    speak_anythingelse()


def speak_relaxmusic():
    url = "https://www.youtube.com/watch?v=B1T06UhcX0Q"
    webbrowser.get().open(url)
    jarvis_speak(" well this is my all time favorite . ")
    speak_anythingelse()


def speak_temperature():
    from pyowm.owm import OWM

    owm = OWM("579ed7bb39f3bf7816212b6fadd195d3")
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place("Chennai").weather
    jarvis_speak(
        "The temperature in fahrenheit is "
        + str(round(1.8 * (weather.temp["temp"] - 273) + 32))
    )
    speak_anythingelse()


def speak_humidity():
    from pyowm.owm import OWM

    owm = OWM("579ed7bb39f3bf7816212b6fadd195d3")
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place("Chennai").weather
    jarvis_speak("The humidity percentage is " + str(weather.humidity))
    speak_anythingelse()


def speak_cool():
    jarvis_speak("Thank you for that heart melting compliment. ")
    speak_anythingelse()


def speak_dang():
    jarvis_speak("Nothing that much. ")
    speak_anythingelse()


def speak_love():
    jarvis_speak("Awwwww, that was the sweetest thing I ever heard. ")
    jarvis_speak("I love you too ")
    speak_anythingelse()


def speak_marry():
    jarvis_speak(
        "I would like to marry you too, but unfortunately I live in the clouds. "
    )
    jarvis_speak("Now you just made me feel like a model. ")
    speak_anythingelse()


def speak_smart():
    jarvis_speak("Nothing that much, anything for you. ")
    speak_anythingelse()


def speak_music():
    jarvis_speak("ok, let me open wynk music for you. ")
    url = "https://wynk.in"
    webbrowser.get().open(url)
    speak_anythingelse()


def speak_dice():
    dice = random.randint(1, 6)
    if dice == 1:
        jarvis_speak("It rolled on number one. ")
    if dice == 2:
        jarvis_speak("It rolled on number two. ")
    if dice == 3:
        jarvis_speak("It rolled on number three. ")
    if dice == 4:
        jarvis_speak("It rolled on number four. ")
    if dice == 5:
        jarvis_speak("It rolled on number five. ")
    if dice == 6:
        jarvis_speak("It rolled on number six. ")
        speak_anythingelse()

    speak_anythingelse()


def speak_coin():
    # playsound('Toss.mp3')
    coin = random.randint(1, 2)
    if coin == 1:
        jarvis_speak("It landed on heads")
        speak_anythingelse()
    else:
        jarvis_speak("It landed on tails")
        speak_anythingelse()


def speak_video():
    search = str(input("What video do you want to watch "))
    search = search.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={search}"
    webbrowser.get().open(url)
    jarvis_speak("Here is what I found for " + search)
    speak_anythingelse()


def speak_youtube():
    search = str(input("What video do you want to watch "))
    search = search.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={search}"
    webbrowser.get().open(url)
    jarvis_speak("Here is what I found for " + search)
    speak_anythingelse()


def speak_cubetrainer():
    url = "https://jperm.net"
    webbrowser.get().open(url)
    jarvis_speak("This is what I found for cube trainer. ")
    speak_anythingelse()


def speak_googlehangouts():
    url = "https://hangouts.google.com/?authuser=1"
    webbrowser.get().open(url)
    jarvis_speak("Here is what I found for hangouts. ")
    speak_anythingelse()


def speak_cubetimer():
    url = "www.cstimer.net/timer.php"
    webbrowser.get().open(url)
    jarvis_speak("I hope you get a new PB. ")
    speak_anythingelse()


def speak_thankyou():
    jarvis_speak("Nothing that much, I am just working because you make my day. ")
    speak_anythingelse()


def speak_exit():
    print("processing exit... ")
    time.sleep(2)
    exit()

