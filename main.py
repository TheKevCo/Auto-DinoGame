import pyautogui
from PIL import ImageGrab
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# -------------------------------------------- Commands -----------------------------------------------#
def start_game():
    pyautogui.click(423, 569)
    pyautogui.typewrite(['up'])


# THIS WAS OLDER CODE, NOTICED THE BIGGEST HURDLE OF THIS GAME IS RUNTIME, GAVE A SMALLER TASK FOR PROGRAM TO ANALYZE
# AND PERFORM JUMP

# def small_tree_check(cactus):
#     try:
#         img = pyautogui.locateOnScreen(cactus, confidence=0.95)
#     except TypeError:
#         pass
#     else:
#         try:
#             if img[0] < 310:
#                 print("I see small")
#                 for i in range(3):
#                     pyautogui.typewrite(['up'])
#
#         except TypeError:
#             pass
#
#
# def big_tree_check(cactus):
#     try:
#         img = pyautogui.locateOnScreen(cactus, confidence=0.95)
#     except TypeError:
#         pass
#     else:
#         try:
#             if img[0] < 310:
#                 print("I see big")
#                 for i in range(3):
#                     pyautogui.typewrite(['up'])
#         except TypeError:
#             pass
#

#  ------------------------------------------- GUI Start Code -----------------------------------------#
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get(url="https://elgoog.im/t-rex/")
game_start = True
while game_start:
    time.sleep(2)
    start_game()
    time.sleep(1)
    no_tree = ImageGrab.grab(bbox=(220, 420, 254, 457))
    while True:
        check = ImageGrab.grab(bbox=(220, 420, 254, 457))
        if no_tree != check:
            pyautogui.typewrite(['up'])
