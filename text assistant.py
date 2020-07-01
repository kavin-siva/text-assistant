import functions as fn
import time


def authenticate_user():
    time.sleep(1)
    password = input("Type in the Password: ")
    print("Checking Password... ")
    if "space" != password:
        fn.jarvis_speak("Incorrect password. ")
        return False
    else:
        pin = input("type in the Pin. ")
        if "2006" != pin:
            fn.jarvis_speak("Incorrect pin. ")
            exit()
            return False

        if "2006" == pin:
            return True


fn.jarvis_speak("My name is Jarvis ")
fn.jarvis_speak("Hi, Kavin, Is there anything I can do for you. ")





if __name__ == "__main__":
    while True:
        client = input()
        fn._respond(client)

