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
import csv
import random
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
        counter = 0

        formCleared = clearForm() # This function is used to clear the form using the 'Clear form' button
        print(formCleared)

        email_check = emailChecked() # This function is used for check box
        print(email_check)
        time.sleep(3)

        fiCodeAdded = addFiCode() # This function is used to fill the text field
        print(fiCodeAdded)

        locationAdded = addLocation() # This function is used to fill the text field
        print(locationAdded)

        companySelected = dropdownAction() # This function is used for drop down menu
        print(companySelected)
        time.sleep(1)

        consentButtonClicked = consentButton() # This function is used for drop down menu
        print(consentButtonClicked)
        time.sleep(1)

        nameAdded = nameField() # This function is used to fill the text field
        print(nameAdded)

        ageAdded = ageField() # This function is used to fill the text field
        print(ageAdded)

        page_Two_Radio_Buttons_Clicked = radio_Buttons_Page_Two()
        print(page_Two_Radio_Buttons_Clicked)

        counter += 1
        print(counter)

        time.sleep(100)


    except TimeoutException:
        print("Timeout occurred: Element not found within the specified time")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def radio_Buttons_Page_Three():


def radio_Buttons_Page_Two():
    # Page Scrolled down
    pageScroll(13)

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=654, y=428, duration=0.5)
    pyautogui.click()

    # Move the cursor to "authority to control decisions" section
    pyautogui.moveTo(x=645, y=834, duration=0.5)
    pyautogui.click()

    # Page Scrolled down
    pageScroll(17)

    # Move the cursor to "less informal gatherings" section
    pyautogui.moveTo(x=650, y=363, duration=0.5)
    pyautogui.click()

    # Move the cursor to "be a part of informal gathering" section 
    pyautogui.moveTo(x=645, y=816, duration=0.5)
    pyautogui.click()

    # Page Scrolled down
    pageScroll(17)

    # Move the cursor to "interests and hobbies" section 
    pyautogui.moveTo(x=637, y=376, duration=0.5)
    pyautogui.click()

    # Move the cursor to "enough qualified female managers" section 
    pyautogui.moveTo(x=634, y=733, duration=0.5)
    pyautogui.click()

    # Page Scrolled down
    pageScroll(15)

    # Move the cursor to "enough qualified female managers" section 
    pyautogui.moveTo(x=640, y=440, duration=0.5)
    pyautogui.click()

    # Move the cursor to "enough qualified female managers" section 
    pyautogui.moveTo(x=638, y=817, duration=0.5)
    pyautogui.click()

    # Page Scrolled down
    pageScroll(15)

    # Move the cursor to "gender-neutral and supportive" section 
    pyautogui.moveTo(x=650, y=492, duration=0.5)
    pyautogui.click()

    # Move the cursor to "transparent and objective recruitment" section 
    pyautogui.moveTo(x=638, y=850, duration=0.5)
    pyautogui.click()

    # Page Scrolled down
    pageScroll(15)

    # Move the cursor to "promotion criteria" section 
    pyautogui.moveTo(x=650, y=492, duration=0.5)
    pyautogui.click()

    # Move the cursor to "female managers at top levels" section 
    pyautogui.moveTo(x=637, y=884, duration=0.5)
    pyautogui.click()

    # Page Scrolled down
    pageScroll(15)

    # Next Button clicked to enter page - 3
    xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span'
    nextButton(xpath)

    return "Page - 2: Radio Buttons Clicked successfully"

def textFields():

    # Define the coordinates
    x1, y1 = 647, 347
    x2, y2 = 650, 400

    # Define the probabilities
    probabilities = [0.15, 0.85]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Mouse moved to select 'UnMarried' or 'Married' marital status
    pyautogui.moveTo(x=x, y=y, duration=0.5)
    pyautogui.click()
    
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys("8861037076") # Contact number added

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys("priyankasharma324@gmail.com") # Email added

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys("Graduate") # Highest Qualification added

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys("TCS - IT") # Organization Name and Type Added

    randomNumber = [1,2,3]

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(random.choice(randomNumber)) # Total Professional Experience Added

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(random.choice(randomNumber)) # Tenure in Present Organization Added

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(random.choice(randomNumber)) # Total Tenure in Current Position Added

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys("IT") # Functional Department Added

    # Scroll the screen to the 'Designation' Section
    driver.execute_script("arguments[0].scrollIntoView(true);", shortTextFields)
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[5]/div/span/div/div/div[1]/input')))
    shortTextFields.send_keys("Team Leader")

    return "All Text Fields completed for this Page-2"


def ageField():
    # Wait for input field to be visible and clickable
    ageTextField = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    print("Age Text Field: Found")
    ageTextField.clear()
    print("Age Text Field Cleared")

    age = [21,22,23,24,25]
    ageTextField.send_keys(random.choice(age))

    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", ageTextField) # Wait for a short time to ensure the scroll operation is completed
    textFields()
    
    return "Age Added"


def nameField():
    # Wait for input field to be visible and clickable
    nameTextField = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    print("Name Text Field: Found")
    
    # Scroll the element into view
    # driver.execute_script("arguments[0].scrollIntoView(true);", nameTextField) # Wait for a short time to ensure the scroll operation is completed
    nameTextField.clear()
    print("Name Text Field Cleared")
    nameTextField.send_keys("Priyanka Sharma")
    
    return "Name Added"


def consentButton():
    # Wait for the "Clear" button to be clickable
    consentButtonFound = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')))
    
    # Scroll the element into view (optional)
    driver.execute_script("arguments[0].scrollIntoView(true);", consentButtonFound)
    print("Screen Scrolled down to the consent Part")

    # drop down menu arrow clicked
    dropdownMenu = driver.find_element(By.CLASS_NAME, 'e2CuFe')
    print("Dropdown menu Found")
    dropdownMenu.click()
    print("Dropdown menu Arrow Clicked")

    # Mouse moved to the 'Clear form' button of the pop up menu
    pyautogui.moveTo(x=650, y=300, duration=0.5)  
    pyautogui.click()

    return "Consent set to YES"


def nextButton(path): # Next Button Function to move to another page
    xPath = path
    clickNextButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xPath)))
    clickNextButton.click()

    return "Next Button Clicked - Waiting for next page to load"

def clearForm():
    # Wait for the "Clear" button to be clickable
    clearForm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[2]/div/span/span')))
    
    # Scroll the element into view (optional)
    driver.execute_script("arguments[0].scrollIntoView(true);", clearForm)
    
    # Click on the "Clear Form" button
    clearForm.click()
    
    print("Pop-up Menu Opened")

    # Use pyautogui to simulate mouse actions
    # Move the mouse pointer to the middle of the screen with additional movements
    pyautogui.moveTo(x=middle_x+150, y=middle_y+100, duration=0.5)  # Mouse moved to the 'Clear form' button of the pop up menu
    pyautogui.click()

    return "Form Cleared"

def emailChecked():
    # Find the element you want to interact with
    # emailClass = driver.find_element(By.XPATH, '//*[@id="i5"]/div[2]')
    print("Email Class Found")

    # Wait for email button to be clickable
    email_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'uHMk6b')))
    email_button.click()
    
    return "Email checked"


def addFiCode():
    # Wait for fiCodeElement input field to be visible and clickable
    fiCodeElement = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    print("FI Code Text Field: Found")
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", fiCodeElement) # Wait for a short time to ensure the scroll operation is completed
    fiCodeElement.clear()
    
    print("FI Code: Text Field Cleared")
    fiCodeElement.send_keys("12")
    
    return "FI Code: 12 - Added in the Text Field"

def addLocation():
    # Wait for location input field to be visible and clickable
    locationElement = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    print("Location Text Field Found")
    
    locationElement.clear()
    print("Location: Text Field Cleared")

    locations = ['Gurgaon, Haryana', 'Delhi']
    locationElement.send_keys(random.choice(locations))
    
    return "Location:Gurgaon Added"

def dropdownAction():
    dropdownMenu = driver.find_element(By.CLASS_NAME, 'e2CuFe')
    print("Dropdown menu Found")
    dropdownMenu.click()
    print("Dropdown menu Arrow Clicked")
    time.sleep(0.5)

    # Mouse moved to the 'Clear form' button of the pop up menu
    pyautogui.moveTo(x=850, y=850, duration=0.5)
    pyautogui.click()

    xPath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span' # XPATH for Page - 1 Next Button
    nextButton(xPath)

    return "Private Company selected and Moved to the Page - 2"

def pageScroll(n):
    pyautogui.moveTo(x=1910, y=1005, duration=0.5)
    # n clicks
    for _ in range(n):
        pyautogui.click()

main()
