from selenium import webdriver
from chromedriver_py import binary_path
import pyautogui
import time


# svc = webdriver.ChromeService(executable_path=binary_path)
# # Set up ChromeOptions
# options = webdriver.ChromeOptions()
# options.add_argument(r"user-data-dir=C:\Users\91844\AppData\Local\Google\Chrome\User Data")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])

# # Initialize Chrome WebDriver with options
# driver = webdriver.Chrome(service=svc, options=options)
# driver.maximize_window()
# driver.implicitly_wait(5)  # Implicit wait to wait for elements to be available

# # Open the Google Form URL
# driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdmONEy9LcFGnlKWF7IEVlvvEm08-wvP2li7w_MDBicsdRZLw/viewform?vc=0&c=0&w=1&flr=0')
# print("Link Opened")
# time.sleep(5)


print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')