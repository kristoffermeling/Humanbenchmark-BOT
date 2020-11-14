import d3dshot
import time
from PIL import Image
import io
import pyautogui,sys
import numpy as np
import random
cnt = 0
time.sleep(3)
#pyautogui.click(x=299, y=299)
d = d3dshot.create(capture_output="numpy")
#d.screenshot_to_disk(region=(350,215,1555,835))
#test = d.screenshot(region=(350,215,1555,835))
# target is 127x127 pixels, so no need to sample more often

d.capture(region=(350,215,1555,835))
time.sleep(2)
pyautogui.click(x=900, y=500)
cnt = 0
#leftmost search block
while True :
    check2 = 89
    check1 = 0

    #time.sleep(0.3)
    test = d.get_latest_frame()
    for i in range(18):
        check2 = 89
        check1 = check1 + 75
        if check1 >1204:
            check1 = 1202

        for j in range(8):
            #pyautogui.click(x=check1 + 350, y=check2 + 215)
            if check2 > 619:
                check2 = 617

            if (test[check2+random.randint(-2,2)][check1+random.randint(-2,2)] == np.array([149, 195, 232], dtype='uint8')).all():
                pyautogui.click(x=check1+350, y=check2+215)
                d.screenshot_to_disk(region=(350, 215, 1555, 835))
                pass


            check2 = check2 + 75
