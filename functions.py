from time import ctime
import os.path
import pyttsx3
import wikipedia
import smtplib
import datetime
import time
from PyDictionary import PyDictionary
import speech_recognition as sr
import webbrowser
import playsound
import os
import random
from gtts import gTTS
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def _respond(client):

    extra_client = client
    client = client.replace(" ", "")
    client = client.lower()

    if "name" in client:
        speak_name()

    if "weight" in client and "con" in client:
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

    elif "shopping" in client or "list" in client:
        speak_list()

    elif 'mail' in client:
        speak_mail()

    elif "game" in client:
        speak_games()

    elif "exit" in client:
        speak_exit()

    elif "thankyou" in client:
        speak_thankyou()
    elif "" in client:
        try:
            speak_wikipedia(extra_client)

        except:

            client = did_you_mean(client)
            _respond(client)

    else:
        client = did_you_mean(client)
        _respond(client)


functions_string = {
    "dictionary_function": "dictionary",
    "alarm_functions": "alarm",
    "music_functions": "music",
    "name_function": "name",
    "time_function": "time",
    "mail_function": "mail",
    "weather_function": "weather",
    "calculator_function": "calculator",
    "compliment_function": "compliment",
    "mood_function": "notinamood",
    "feelings_function": "feelingdepressed",
    "browse_function": "browse",
    "location_function": "location",
    "temperature_function": "temperature",
    "humidity_function": "humidity",
    "cool_function": "cool",
    "dang_function": "dang",
    "marry_function": "marryme",
    "love_function": "loveyou",
    "greeting_function": "goodmorning",
    "smart_function": "smart",
    "goodnight_function": "goodnight",
    "relaxmusic_function": "relaxingmusic",
    "coin_function": "flipacoin",
    "dice_function": "rolladice",
    "video_function": "video",
    "youtube_function": "youtube",
    "chess_function": "chess",
    "list_function": "list",
    "cubetrainer_function": "cubetrainer",
    "cubetutorial_function": "cubetutorial",
    "googlehangouts_function": "hangouts",
    "cubetimer_function": "cubetimer",
    "games_function": "games",
    "weight_converter_function": "weightcon",
    "thankyou_function": "thankyou",
    "exit_function": "exit",
}

r = sr.Recognizer()

dictionary = PyDictionary()


# def jarvis_speak(audio_string):
#     tts = gTTS(text=audio_string, lang="en")
#     r = random.randint(1, 10000000)
#     audio_file = "audio-" + str(r) + ".mp3"
#     tts.save(audio_file)
#     playsound.playsound(audio_file)
#     print(audio_string)
#     os.remove(audio_file)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi Kavin, how can I help you")


def speak_wikipedia(client):
    client = client.lower()
    #client = client.split(' ')
    #client = " ".join(client[2:])
    if 'who' in client:
        client = client.replace('who is', '')
    elif 'what' in client:
        client = client.replace('what is', '')
    wikipedia_input = str(wikipedia.summary(client, sentences=2))
    speak('According to wikipedia ')
    speak(wikipedia_input)
    speak_anythingelse()


def speak_list():
    if os.path.isfile("shopping_list.txt"):
        speak('These were the items that was present in your list...')
        with open('shopping_list.txt', 'r') as file1:
            while True:
                speak(file1.read())
                if file1.read() == "":
                    break
            speak('\n')
            speak('Do you want to edit your list? ')
            yes_no = input()
            if 'y' in yes_no.lower():
                change_list()
                while True:
                    print(file1.read())
                    if file1.read() == "":
                        break
            speak_anythingelse()

    else:
        speak('New shopping list has been made')
        speak("What item do you want to add in your list? ")
        change_list()
        while True:
            print(file1.read())
            if file1.read() == "":
                break
        speak_anythingelse()


def change_list():
    with open("shopping_list.txt", 'a') as file1:
        print('What do you want to do with the list ')
        n = 1
        while True:
            if n == 0:
                speak('What do you want to do with the list ')
                n = 1
            user_input = input()
            n = 0
            user_input = user_input.lower()
            if user_input[0:3] == 'add' or user_input[0:3] == 'put':
                user_input = user_input.replace(user_input[0:3], '')
                user_input = user_input.strip()
                user_input = '\n' + user_input
                file1.write(user_input)
                user_input = user_input.replace("\n", "")
                speak(
                    f'{user_input} has been added to the list')
                speak('Do you want to make anymore changes to the list ')
                if 'y' not in input():
                    return 0

            elif user_input[0:6] == 'remove' or user_input[0:6] == 'delete':
                with open("shopping_list.txt", 'r+') as file2:
                    data = file2.readlines()
                    print(data)
                    a = user_input.replace(user_input[0:6], '')
                    a = a.strip()
                    if a != data[len(data)-1]:
                        a += '\n'
                    if '\n' in data[len(data)-1]:
                        data[len(data)-1] = data[len(data)-1].replace('\n', '')
                    print(data)
                    data.remove(a)
                    print(data)
                    if '\n' in data[len(data)-1]:
                        data[len(data)-1] = data[len(data)-1].replace('\n', '')
                    print(data)
                    a = a.replace('\n', '')
                    speak(f"{a} has been removed from the list ")
                    with open("shopping_list.txt", "w") as f:
                        print(data)
                        f.write('\n')
                        print(data)
                        data.pop(0)
                        print(data)
                        file2.writelines(data)
                        print(data)
                    speak('Do you want to make anymore changes to the list ')
                    print(data)
                    if 'n' in input():
                        return 0
    print(data)


def remove_spaces(word):
    margin = 38
    no_of_spaces = 38 + len(word)
    with open
    print(data)

    # def takeCommand():
    #     # It takes microphone input from the user and returns string output

    #     r = sr.Recognizer()
    #     with sr.Microphone() as source:

    #         r.pause_threshold = 1
    #         audio = r.listen(source)

    #     try:

    #         query = r.recognize_google(audio, language='en')
    #         print(f"User said: {query}\n")

    #     except Exception as e:
    #         # print(e)

    #         return "None"
    #     return query


def speak_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kavinsivasu@gmail.com', 'Jupiter9')
    speak("Who do you want to send the email to?")
    client = input()
    try:
        if 'garvit' in client:
            speak("What should I say?")
            content = input()
            to = "sharmagarvit614@gmail.com"

            speak("Email has been sent!")

        elif 'mukil' in client:
            speak("What should I say?")
            content = input()
            to = "mukil2win@gmail.com"

            speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry Sir. I am not able to send this email")
    server.sendmail('kavinsivasu@gmail.com', to, content)

    server.close()
    speak_anythingelse()


def speak_dictionary():
    word = input("which word would you like me to define ")
    speak(str(dictionary.meaning(word)))
    speak_anythingelse()


def speak_weight_converter():
    weight = input('Weight: ')

    unit = input('Is the weight in (L)lbs (K)kg: ')

    if unit.upper() == 'L':
        final1 = (.45) * int(weight)
        print(f'The weight is {final1} Kilos ')

    else:
        final1 = (.45) / int(weight)
        print(f'The weight is {final1} pounds ')
    speak_anythingelse()


def alarm():
    subprocess.call(["dist/alarm/alarm.exe"])


def speak_location():
    location = str(input("What location would you like to look for? "))
    url = f"https://google.nl/maps/place/{location}/&amp;"
    webbrowser.get().open(url)
    speak("Here is what I found for " + location)
    speak_anythingelse()


def speak_time():
    list1 = ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday"]
    wday = list1[time.localtime().tm_wday]
    list2 = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    mon = list2[time.localtime().tm_mon - 1]
    mday = time.localtime().tm_mday
    hour = time.localtime().tm_hour
    minu = time.localtime().tm_min
    if hour > 12:
        hour -= 12
        minu = f"{minu} PM"
    elif hour == 12:
        minu = f"{minu} PM"
    else:
        minu = f"{minu} AM"

    year = time.localtime().tm_year
    string = f"{wday} {mon} {mday} {hour}:{minu} {year}"
    speak(string)
    speak_anythingelse()


def did_you_mean(input_string):
    input_list = remove_more_less(functions_string, input_string)
    speak("Sorry, I did not get that. ")
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
                speak(f"Did you mean {input_list[i]}")
                new_input = input()
                new_input = new_input.lower()
                if "y" in new_input:
                    m = 1
                    n = 0
                    _respond(input_list[i])
                else:
                    speak("What do you want me to do then? ")
                break
    speak("please type that again. ")
    input500 = input()
    return input500


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
            print("The time elapsed is", round(
                end_time - start_time, 2), "secs")
            break
    speak_anythingelse()


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
    speak("Is there anything else you want me to do. ")
    answer = input()
    if "n" == answer[0]:
        speak("You can ask me anything later. ")
        exit()
        return 0

    elif "y" == answer[0]:
        speak("What can I do for you. ")
        return 0
    else:
        return 0


def speak_calculator():
    speak("What do you want to calculate ")
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
            term2 = int(equation[i + 1:])

    if operator == "+":
        speak(str(term1 + term2))
    elif operator == "-":
        speak(str(term1 - term2))
    elif operator == "*":
        speak(str(term1 * term2))
    else:
        speak(str(term1 / term2))
    speak_anythingelse()


def speak_weather():
    from pyowm.owm import OWM

    owm = OWM("579ed7bb39f3bf7816212b6fadd195d3")
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place("Chennai").weather
    speak("The humidity percentage is " + str(weather.humidity))
    speak(
        "The temperature in fahrenheit is "
        + str(round(1.8 * (weather.temp["temp"] - 273) + 32))
    )
    speak("The weather status is " + str(weather.to_dict()["detailed_status"]))
    speak_anythingelse()


def speak_games():
    speak("What game do you want to play")
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
    speak("My name is Jarvis. ")
    speak_anythingelse()


def speak_chess():
    url = "www.chess.com"
    webbrowser.get().open(url)
    speak("I hope you win your chess match ")


def speak_compliment():
    speak(
        "I admire you. You can do it. I value you. You can count on me. I believe in you. You are kind. I trust you. You are smart. "
    )
    speak_anythingelse()


def speak_mood():
    speak("well seeing you in this mood makes me sad ")
    speak("I think you had a tough day")
    speak("lets relax ")
    url = "www.youtube.com"
    webbrowser.get().open(url)
    speak_anythingelse()


def speak_feelings():
    speak(
        "I admire you. You can do it. I value you. You can count on me. I believe in you. You are kind. I trust you. You are smart. "
    )
    speak("how about we relax")
    url = "www.youtube.com"
    webbrowser.get().open(url)
    speak_anythingelse()


def speak_browse():
    find = str(input("What would you like to browse "))
    find = find.replace(" ", "+")
    url = f"https://google.com/search?q={find}"
    webbrowser.get().open(url)
    speak("Here is what I found for " + find)
    speak_anythingelse()


def speak_greetings():
    speak("Good Morning to you to")
    speak("It is ")
    speak(ctime())
    speak("You better get going now, as today is a big day. ")
    speak_anythingelse()


def speak_goodnight():
    speak("Good Night to you as well")
    speak("Sleep tite and do not let the bed bugs bite. ")
    speak(ctime())
    # add alarm after 8 hours with clients permission


def speak_cubetutorial():
    cubetutorial = input(
        "Which instructor would you like to have,  " "Jperm, Brody the cuber: "
    )
    cubetutorial = cubetutorial.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={cubetutorial}"
    webbrowser.get().open(url)
    speak("I hope you learn something new in cubing ")
    speak_anythingelse()


def speak_relaxmusic():
    url = "https://www.youtube.com/watch?v=B1T06UhcX0Q"
    webbrowser.get().open(url)
    speak(" well this is my all time favorite . ")
    speak_anythingelse()


def speak_temperature():
    from pyowm.owm import OWM

    owm = OWM("579ed7bb39f3bf7816212b6fadd195d3")
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place("Chennai").weather
    speak(
        "The temperature in fahrenheit is "
        + str(round(1.8 * (weather.temp["temp"] - 273) + 32))
    )
    speak_anythingelse()


def speak_humidity():
    from pyowm.owm import OWM

    owm = OWM("579ed7bb39f3bf7816212b6fadd195d3")
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place("Chennai").weather
    speak("The humidity percentage is " + str(weather.humidity))
    speak_anythingelse()


def speak_cool():
    speak("Thank you for that heart melting compliment. ")
    speak_anythingelse()


def speak_dang():
    speak("Nothing that much. ")
    speak_anythingelse()


def speak_love():
    speak("Awwwww, that was the sweetest thing I ever heard. ")
    speak("I love you too ")
    speak_anythingelse()


def speak_marry():
    speak(
        "I would like to marry you too, but unfortunately I live in the clouds. "
    )
    speak("Now you just made me feel like a model. ")
    speak_anythingelse()


def speak_smart():
    speak("Nothing that much, anything for you. ")
    speak_anythingelse()


def speak_music():
    speak("ok, let me open wynk music for you. ")
    url = "https://wynk.in"
    webbrowser.get().open(url)
    speak_anythingelse()


def speak_dice():
    dice = random.randint(1, 6)
    if dice == 1:
        speak("It rolled on number one. ")
    if dice == 2:
        speak("It rolled on number two. ")
    if dice == 3:
        speak("It rolled on number three. ")
    if dice == 4:
        speak("It rolled on number four. ")
    if dice == 5:
        speak("It rolled on number five. ")
    if dice == 6:
        speak("It rolled on number six. ")
        speak_anythingelse()

    speak_anythingelse()


def speak_coin():
    # playsound('Toss.mp3')
    coin = random.randint(1, 2)
    if coin == 1:
        speak("It landed on heads")
        speak_anythingelse()
    else:
        speak("It landed on tails")
        speak_anythingelse()


def speak_video():
    search = str(input("What video do you want to watch "))
    search = search.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={search}"
    webbrowser.get().open(url)
    speak("Here is what I found for " + search)
    speak_anythingelse()


def speak_youtube():
    search = str(input("What video do you want to watch "))
    search = search.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={search}"
    webbrowser.get().open(url)
    speak("Here is what I found for " + search)
    speak_anythingelse()


def speak_cubetrainer():
    url = "https://jperm.net"
    webbrowser.get().open(url)
    speak("This is what I found for cube trainer. ")
    speak_anythingelse()


def speak_googlehangouts():
    url = "https://hangouts.google.com/?authuser=1"
    webbrowser.get().open(url)
    speak("Here is what I found for hangouts. ")
    speak_anythingelse()


def speak_cubetimer():
    url = "www.cstimer.net/timer.php"
    webbrowser.get().open(url)
    speak("I hope you get a new PB. ")
    speak_anythingelse()


def speak_thankyou():
    speak("Nothing that much, I am just working because you make my day. ")
    speak_anythingelse()


def speak_exit():
    print("processing exit... ")
    time.sleep(2)
    exit()
