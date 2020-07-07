import os
import time
import pyautogui


def remove_those_idiot_question_mark():
    os.startfile('shopping_list.txt')
    time.sleep(0.5)
    pyautogui.press('down')
    for i in range(0, 125):
        pyautogui.press('backspace')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('ctrl', 'w')


remove_those_idiot_question_mark()
