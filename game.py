import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(707, 737):
        for j in range(350, 390):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(707, 737):
        for j in range(400, 420):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(1)
    print("2 seconds")
    time.sleep(1)
    print("1 seconds")
    time.sleep(1)
    print("0 second")
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))

        # Draw the rectangle for cactus
        for i in range(707, 720):
            for j in range(400, 405):
                data[i, j] = 0

        # Draw the rectangle for birds
        for i in range(707, 720):
            for j in range(385, 390):
                data[i, j] = 171

        image.show()
        break
