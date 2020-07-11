

functions_string = [
    "dictionary",
    "alarm",
    "music",
    "name",
    "time",
    "mail",
    "youtube",
    "weather",
    "calculator",
    "notinamood",
    "compliment",
    "feelingdepressed",
    "browse",
    "location",
    "temperature",
    "humidity",
    "cool",
    "dang",
    "marryme",
    "loveyou",
    "goodmorning",
    "smart",
    "goodnight",
    "relaxingmusic",
    "flipacoin",
    "rolladice",
    "video",
    "games", "chess",
    "list",
    "cubetrainer",
    "cubetutorial",
    "hangouts",
    "cubetimer",
    "weightcon",
    "thankyou",
    "exit",
]


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
                    exit()
                elif 'n' in new_input:
                    tries += 1
                if tries >= 2:
                    print("What did you mean? ")
                    tf = True
                break
    # if tf != True:
        # print("Sorry, I did not get that. ")
        # print("please type that again. ")
    # input500 = input()
    # return input500


def remove_more_less(input_list, input_string):
    extra_list = []
    length_string = len(input_string)
    for i in range(0, len(input_list) - 1):
        if len(input_list[i]) != length_string:
            extra_list.append(input_list[i])
    for i in range(0, len(extra_list)):
        input_list.remove(extra_list[i])
    return input_list


while True:

    did_you_mean(input())
# chess.games
# loveyou.youtube
# notinamood.compliment
