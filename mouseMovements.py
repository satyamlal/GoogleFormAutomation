import time
import pyautogui


pyautogui.moveTo(x=1910, y=1005, duration=0.5)
# Loop 15 times
for _ in range(15):
    pyautogui.click()