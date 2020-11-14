# hex color code: #4bdb6a
#rgb code : rgb(75, 219, 106)

import d3dshot
import time
from PIL import Image
import io
import pyautogui,sys

cnt = 0
#time.sleep(3)
pyautogui.click(x=299, y=299)
d = d3dshot.create(capture_output="numpy")


par = True
d.capture(region=(299, 299, 300, 300))
while True:
    if par:
        time.sleep(1)
        par = False
    #time.sleep(.1)
    test = d.get_latest_frame()
    if test[0][0][0] == 75 and test[0][0][1] == 219 and test[0][0][2] == 106 and cnt <= 5:
        pyautogui.click(x=299, y=299)
        cnt+=1
        time.sleep(0.5)
        pyautogui.click(x=299, y=299)
