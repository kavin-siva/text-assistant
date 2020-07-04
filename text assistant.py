import functions as fn
import time


# def authenticate_user():
#     time.sleep(1)
#     password = input("Type in the Password: ")
#     print("Checking Password... ")
#     if "space" != password:
#         fn.jarvis_speak("Incorrect password. ")
#         return False
#     else:
#         pin = input("type in the Pin. ")
#         if "2006" != pin:
#             fn.jarvis_speak("Incorrect pin. ")
#             exit()
#             return False

#         if "2006" == pin:
#             return True


if __name__ == "__main__":
    fn.wishMe()
    while True:
        client = input()
        fn._respond(client)
