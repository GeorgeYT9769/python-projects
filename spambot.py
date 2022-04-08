import time
from pyautogui import *

for i in range(10):
    time.sleep(2)
    text = open("123.txt")
    for each_line in text:
        write(each_line)
    press('enter')