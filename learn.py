

functions_string = {
    "dictionary_function": "dictionary",
    "alarm_functions": "alarm",
    "music_functions": "music",
    "name_function": "name",
    "time_function": "time",
    "mail_function": "mail",
    "youtube_function": "youtube",
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


def did_you_mean(input_string):
    input_list = remove_more_less(functions_string, input_string)
    sixty = round((len(input_string) * 0.6))
    tries = 0
    tf = False
    input_list_string = list(input_string)
    for i in range(0, len(input_list) - 1):
        n = 0
        for j in range(0, len(input_list[i]) - 1):
            try:
                if input_list_string[j] == ((input_list[i])[j]):
                    n += 1
            except IndexError:
                continue
            if n >= sixty:
                print(f"Did you mean {input_list[i]}")
                new_input = input()
                new_input = new_input.lower()
                if "y" in new_input:
                    n = 0
                    print('Match has been found ')
                elif 'n' in new_input:
                    tries += 1
                if tries >= 1:
                    print("What did you mean? ")
                    tf = True
                break
    if tf != True:
        print("Sorry, I did not get that. ")
        print("please type that again. ")
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


did_you_mean('geme')
