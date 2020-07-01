def respond(client):

    client = client.replace(" ", "")
    client = client.lower()

    if "name" in client:
        fn.speak_name()

    elif "stopwatch" in client:
        fn.stopwatch()

    elif "alarm" in client:
        fn.alarm()

    elif "dictionary" in client:
        fn.speak_dictionary()

    elif "cubetimer" in client:
        fn.speak_cubetimer()

    elif "time" in client:
        fn.speak_time()

    elif "weather" in client:
        fn.speak_weather()

    elif "calculat" in client:
        fn.speak_calculator()

    elif "compliment" in client:
        fn.speak_compliment()

    elif "mood" in client and "good" in client and "no" in client:
        fn.speak_mood()

    elif "depressed" in client and "feeling" in client:
        fn.speak_feelings()

    elif "browse" in client:
        fn.speak_browse()

    elif "location" in client:
        fn.speak_location()

    elif "temperature" in client:
        fn.speak_temperature()

    elif "humidity" in client:
        fn.speak_humidity()

    elif "cool" in client:
        fn.speak_cool()

    elif "marryme" in client:
        fn.speak_marry()

    elif "love" in client and "you" in client:
        fn.speak_love()

    elif "dang" in client:
        fn.speak_dang()

    elif "goodmorning" in client:
        fn.speak_greetings()

    elif "smart" in client:
        fn.speak_smart()

    elif "goodnight" in client:
        fn.speak_goodnight

    elif "music" in client:
        fn.speak_music()

    elif "rolladice" in client:
        fn.speak_dice()

    elif "flipacoin" in client:
        fn.speak_coin()

    elif "video" in client:
        fn.speak_video()

    elif "youtube" in client:
        fn.speak_youtube()

    elif "chess" in client:
        fn.speak_chess()

    elif "cube" in client and "trainer" in client:
        fn.speak_cubetrainer()

    elif "cube" in client and "tutorial" in client:
        fn.speak_cubetutorial()

    elif "hangouts" in client:
        fn.speak_googlehangouts()

    elif "game" in client:
        fn.speak_games()

    elif "exit" in client:
        fn.speak_exit()

    elif "thankyou" in client:
        fn.speak_thankyou()

    else:
        client = fn.did_you_mean(client)
        respond(client)
