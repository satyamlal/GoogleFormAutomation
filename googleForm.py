from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pyautogui
import time


svc = webdriver.ChromeService(executable_path=binary_path)
# Set up ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\91844\AppData\Local\Google\Chrome\User Data")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(service=svc, options=options)
driver.maximize_window()
driver.implicitly_wait(5)  # Implicit wait to wait for elements to be available

# Open the Google Form URL
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdmONEy9LcFGnlKWF7IEVlvvEm08-wvP2li7w_MDBicsdRZLw/viewform?vc=0&c=0&w=1&flr=0')
print("Link Opened")
time.sleep(5)

# Get the screen's dimensions
screen_width, screen_height = pyautogui.size()

# Calculate the coordinates for the middle of the screen
middle_x = screen_width // 2
middle_y = screen_height // 2


def main():

    try:
        formCleared = clearForm()
        print(formCleared)

        email_check = emailChecked()
        print(email_check)
        time.sleep(5)

        fiCodeAdded = AddFiCode()
        print(fiCodeAdded)

        locationAdded = AddLocation()
        print(locationAdded)

        # companySelected = dropdownAction()
        # print(companySelected)
        print("companySelected")
        time.sleep(10)

    except TimeoutException:
        print("Timeout occurred: Element not found within the specified time")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def clearForm():
    # Wait for the "Clear" button to be clickable
    clearForm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[2]/div/span/span')))
    
    # Scroll the element into view (optional)
    driver.execute_script("arguments[0].scrollIntoView(true);", clearForm)
    
    # Click on the "Clear Form" button
    clearForm.click()
    
    print("Pop-up Menu Opened")

    # Use pyautogui to simulate mouse actions
    # Move the mouse pointer to the middle of the screen
    pyautogui.moveTo(x=middle_x+150, y=middle_y+100, duration=0.5)  # Adjust coordinates as needed
    pyautogui.click()

    # Pause briefly to let the action complete
    time.sleep(3)


    # Find and click on the "Clear form" button in the Pop Up Menu
    # clearFormPopUpButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'l4V7wb')))
    # clearFormPopUpButton.click()

    return "Form Cleared"

def emailChecked():
    # Find the element you want to interact with
    emailClass = driver.find_element(By.XPATH, '//*[@id="i5"]/div[2]')
    print("Email Class Found")

    # Wait for email button to be clickable
    email_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'uHMk6b')))
    email_button.click()
    
    return "Email checked"


def AddFiCode():
    # Wait for fiCodeElement input field to be visible and clickable
    fiCodeElement = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    print("FI Code Text Field: Found")
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", fiCodeElement) # Wait for a short time to ensure the scroll operation is completed
    fiCodeElement.clear()
    
    print("FI Code: Text Field Cleared")
    fiCodeElement.send_keys("12")
    
    return "FI Code: 12 - Added in the Text Field"

def AddLocation():
    # Wait for location input field to be visible and clickable
    locationElement = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    print("Location Text Field Found")
    
    locationElement.clear()
    print("Location: Text Field Cleared")
    
    locationElement.send_keys("Gurgaon")
    return "Location:Gurgaon Added"

def dropdownAction():
    dropdownMenu = driver.find_element(By.CLASS_NAME, 'e2CuFe')
    print("Dropdown menu Found")
    dropdownMenu.click()
    print("Dropdown menu Arrow Clicked")
    time.sleep(3)

    dropdownMenu = driver.find_element(By.CLASS_NAME, 'kRoyt')
    dropdownMenu.click()

    # Find and click on the option "Private Company" based on the data-value attribute
    options = driver.find_elements(By.CSS_SELECTOR, '[role="option"]')
    for option in options:
        time.sleep(5)
        if option.get_attribute('data-value') == 'Private Company':
            option.click()
            break
    return "Private Company selected"


main()
