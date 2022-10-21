# please read docs @ https://pypi.org/project/PyAutoGUI/

import pyautogui
import time
import random

for z in range(1,14400):
    x=random.randint(400,800)
    y=random.randint(400,500)
    pyautogui.moveTo(x,y)

    pyautogui.click()

    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print("Moving at " + str(result) + ' (' + str(x) + "," + str(y) + ")")
    time.sleep(2)