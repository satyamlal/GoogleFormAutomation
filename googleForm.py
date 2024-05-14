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
import string
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
        counter = 0 # counter starts from 0

        # while counter <1000:

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

        nameAdded = nameField() # This function is used to fill the name text field
        print(nameAdded)

        ageAdded = ageField() # This function is used to fill the age text field
        print(ageAdded)

        page_Two_Radio_Buttons_Clicked = radio_Buttons_Page_Two()
        print(page_Two_Radio_Buttons_Clicked)

        '''Page 1 and Page 2 submission ends here'''

        page_Three_Radio_Button_Clicked = radio_Buttons_Page_Three()
        print(page_Three_Radio_Button_Clicked)

        counter += 1 # Counter increases after every successful form submission
        print(counter)

        time.sleep(100)


    except TimeoutException:
        print("Timeout occurred: Element not found within the specified time")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def radio_Buttons_Page_Three():

    # Page Scrolled down
    pageScroll(13)

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=654, y=428, duration=0.5)
    pyautogui.click()

    return "Page 3 Completed"


def radio_Buttons_Page_Two():

    # Page Scrolled down
    pageScroll(13)

    '''select random option for Male to Female Ratio in high visibility roles'''

    # Define the coordinates
    x1, y1 = 698, 325
    x2, y2 = 636, 381
    x3, y3 = 654, 428
    x4, y4 = 638, 481
    x5, y5 = 686, 525

    # Define the probabilities
    probabilities = [0.05, 0.15, 0.40, 0.30, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()


    '''select random option for Authority to Control Decisions'''
    # Define the coordinates
    x1, y1 = 683, 735
    x2, y2 = 640, 785
    x3, y3 = 667, 832
    x4, y4 = 648, 890
    x5, y5 = 700, 932

    # Define the probabilities
    probabilities = [0.05, 0.15, 0.40, 0.30, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "authority to control decisions" section
    pyautogui.moveTo(x=x, y=y, duration=0.5)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(17)
    
    
    '''select random option for less informal gatherings'''
    # Define the coordinates
    x1, y1 = 697, 258
    x2, y2 = 623, 308
    x3, y3 = 669, 360
    x4, y4 = 629, 409
    x5, y5 = 678, 461

    # Define the probabilities
    probabilities = [0.05, 0.15, 0.40, 0.30, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()


    '''select random option for be a part of informal gathering'''
    # Define the coordinates
    x1, y1 = 660, 665
    x2, y2 = 657, 721
    x3, y3 = 646, 766
    x4, y4 = 627, 820
    x5, y5 = 704, 870

    # Define the probabilities
    probabilities = [0.05, 0.15, 0.40, 0.30, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "be a part of informal gathering" section 
    pyautogui.moveTo(x=x, y=y, duration=0.5)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(17)


    '''select random option for interests and hobbies'''
    # Define the coordinates
    x1, y1 = 741, 228
    x2, y2 = 637, 277
    x3, y3 = 666, 326
    x4, y4 = 654, 375
    x5, y5 = 681, 424

    # Define the probabilities
    probabilities = [0.05, 0.15, 0.40, 0.30, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]
    
    # Move the cursor to "interests and hobbies" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()


    '''select random option for enough qualified female managers'''
    # Define the coordinates
    x1, y1 = 665, 633
    x2, y2 = 628, 681
    x3, y3 = 646, 732
    x4, y4 = 651, 779
    x5, y5 = 698, 834

    # Define the probabilities
    probabilities = [0.05, 0.15, 0.40, 0.30, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    pyautogui.moveTo(x=x, y=y, duration=0.5)
    pyautogui.click()

    '''Page Scrolled'''
    pageScroll(15)

 
    '''select random option for provides mentorship and counselling'''
    # Define the coordinates
    x1, y1 = 662, 289
    x2, y2 = 638, 340
    x3, y3 = 655, 388
    x4, y4 = 646, 437
    x5, y5 = 681, 488

    # Define the probabilities
    probabilities = [0.05, 0.15, 0.40, 0.30, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()


    '''select random option for regard my supervisor'''
    # Define the coordinates
    x1, y1 = 670, 666
    x2, y2 = 636, 717
    x3, y3 = 660, 767
    x4, y4 = 640, 818
    x5, y5 = 666, 864

    # Define the probabilities
    probabilities = [0.05, 0.15, 0.40, 0.30, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(15)


    time.sleep(1000000)

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

    return "Page 2 Completed"

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
    

    '''Random Contact Number Generated STARTS HERE'''
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    
    shortTextFields.send_keys(generate_random_mobile_number()) # Contact number added
    '''Random Contact Number Generated ENDS HERE'''


    '''Random Email Generated STARTS HERE'''
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    fullName, emailAddress = generate_random_female_data() # Random name and email generated for female    
    print("Email Address added in the text field:", emailAddress)
    print("Name:", fullName)

    shortTextFields.send_keys(emailAddress) # Email added
    print("Email Address Added Successfully")

    '''Random Email Generated END HERE'''
    
    
    '''Highest Qualification START'''
    
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    
    highest_Qualification = ['B.Tech', 'M.Tech']

    # Define the probabilities
    probabilities = [0.70, 0.30]

    # Random choice of highest Qualification based on the probability
    qualification = random.choices(highest_Qualification, weights=probabilities)[0]

    shortTextFields.send_keys(qualification) # Highest Qualification added
    print("Highest Qualification Added Successfully")
    
    '''Highest Qualification selection END'''
    
    
    '''Oraganization Name and Type'''
    
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    
    organizationName = [
        "Tata Consultancy Services (TCS)",
        "Infosys",
        "Wipro Limited",
        "Tech Mahindra",
        "Accenture India",
        "Capgemini",
        "Cognizant Technology Solutions",
        "Genpact",
        "SAP Labs India",
        "Oracle India",
        "TATA Elxsi",
        "Deloitte India",
        "Ernst & Young (EY)",
    ]

    # Define the probabilities
    probabilities = [0.60, 0.25, 0.25, 0.30, 0.15, 0.10, 0.10, 0.10, 0.05, 0.05, 0.35, 0.05, 0.05]

    # Choose between the two sets of coordinates based on probabilities
    companyName = random.choices(organizationName, weights=probabilities)[0]
    
    shortTextFields.send_keys(companyName) # Organization Name and Type Added Randomly
    print("Organization Name Added")
    
    '''Oraganization Name and Type END'''


    randomNumber = [1,2,3] # List of three numbers

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
    
    designation = ['Developer', 'Software Engineer', 'Data Scientist', 'Data Engineer', 'DevOps Engineer']
    shortTextFields.send_keys(random.choice(designation)) # Team Designation selected randomly

    return "All Text Fields completed for this Page-2"


def ageField():
    # Wait for input field to be visible and clickable
    ageTextField = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
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

    fullName, emailAddress = generate_random_female_data() # Random name and email generated for female
    
    nameTextField.send_keys(fullName) # Name Added

    print("Full Name Printed in the Name Field:", fullName) #
    print("Email Address:", emailAddress)
    
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

    locations = ['Gurgaon', 'Delhi']
    probabilities = [0.7, 0.3]
    
    locationElement.send_keys(random.choices(locations, weights=probabilities)[0])
    
    return "Location Added"

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



'''This script generate random numbers each time function is called and
    cross checks if the number already exists before return the number'''

# Set to store generated numbers
generated_numbers = set()

def generate_random_mobile_number():
    global generated_numbers
    while True:
        # Generate a random 10-digit number
        random_digits = ''.join([str(random.randint(6, 9)) for _ in range(10)])
        # Concatenate '+91' with the random digits
        number = '+91 ' + random_digits
        # Check if the number is already generated
        if number not in generated_numbers:
            generated_numbers.add(number)
            return number



'''This script generate random name with corresponding email each time without repetition'''

# List of common First Names
first_names = [
    "Aaradhya", "Ananya", "Isha", "Jiya", "Kavya", "Mahi", "Riya",
    "Shreya", "Aadhya", "Aanya", "Aarohi", "Aashi", "Anika", "Avni", "Gauri",
    "Ishita", "Janvi", "Khushi", "Manvi", "Mehak", "Myra", "Navya", "Pari", "Roshni",
    "Sanvi", "Sara", "Siya", "Suhani", "Tanisha", "Trisha", "Vani", "Vanya", "Anahita", "Aradhana",
    "Ariana", "Aarushi", "Amaira", "Arya", "Dhriti", "Esha", "Hansa",
    "Jhanvi", "Kashvi", "Kiara", "Kriti", "Mahira", "Nandini", "Nehal", "Pihu",
    "Ridhi", "Riva", "Ruchi", "Saanvi", "Samaira", "Shruti", "Sneha", "Tanvi", "Tanya", "Trisha",
    "Vaani", "Vanya", "Vedika", "Aadhira", "Aarna", "Aashi", "Akshara", "Anvi", "Aria",
    "Ankita", "Bhavya", "Chahat", "Divya", "Devika",
    "Kiran", "Lavanya", "Mansi", "Naina", "Navya",
    "Nikita", "Poonam", "Palak", "Radhika", "Ritika", "Samaira", "Sanya", "Sonia", "Tara",
    "Tanya", "Urvi", "Vaishnavi", "Vanshika", "Yashika", "Zara", "Aarushi", "Aayat", "Anoushka",
    "Amaya", "Anvita", "Anushka", "Aparna", "Charvi", "Dia", "Ishaani",
    "Jhanvi", "Jiya", "Khushi", "Kanak", "Kavya", "Leela", "Mansi", "Nikita", "Neha",
    "Priya", "Priti", "Ritika", "Saumya", "Kreeti", "Nimisha", "Nupur"
    "Shanaya", "Tara", "Urvashi", "Vidhi", "Vanshika", "Yashvi",
    "Anushree", "Anvi", "Bhavika", "Chitra", "Drishti", "Ishita",
    "Ishika", "Ishita", "Kavya", "Lavanya", "Mehak", "Mehek", "Niharika",
    "Nisha", "Pranjal", "Rachana", "Rashi", "Ruchika", "Saniya",
    "Saanvi", "Shikha", "Trisha", "Urvi", "Vani","Aditi",
    "Aadya", "Anisha", "Apoorva", "Anvita", "Aradhya", "Bhavana",
    "Charu", "Deeksha", "Eva", "Ishani", "Ishwari", "Juhi", "Komal", "Kritika", "Lakshita",
    "Mahika", "Nandini", "Navika", "Prerna", "Priyanka", "Ria",
    "Rishika", "Shivangi", "Sarika", "Tanushree", "Tara", "Uma", "Vaishali", "Vidhi",
    "Yamini", "Zara", "Anshika", "Anushka", "Arunima", "Bhavna", "Devanshi",
    "Ishwarya", "Ishika", "Jagrati", "Kanishka", "Lavanya", "Mahima",
    "Nitya", "Radha", "Reema", "Rhea", "Saisha", "Sakshi", "Sanya",
    "Aarohi", "Anshika", "Aadya", "Anvi", "Alisha", "Arushi", "Anshu", "Ankita",
    "Aashi", "Anupriya", "Anisha", "Bhoomi", "Chhaya", "Deepti", "Gauri", "Ishita",
    "Jasmine", "Kashish", "Kashvi", "Kirti", "Lakshmi", "Mansi", "Minal", "Nandita",
    "Pari", "Pragya", "Pooja", "Ritika", "Ritvi", "Sanya", "Shivani",
    "Sakshi", "Srishti", "Tanishka", "Trisha", "Urvi", "Vidhi", "Vaishali", "Riddham"
]

# List of common North Indian surnames with corresponding probabilities
last_names = [
    ("Sharma", 25), 
    ("Verma", 20), 
    ("Jha", 20), 
    ("Singh", 25), 
    ("Yadav", 15), 
    ("Gupta", 15), 
    ("Malhotra", 5), 
    ("Bhatia", 5), 
    ("Chopra", 5), 
    ("Mittal", 5),
    ("Pandey", 7), 
    ("Tiwari", 6), 
    ("Shukla", 6), 
    ("Garg", 4), 
    ("Agarwal", 10),
    ("Chauhan", 10), 
    ("Sinha", 10), 
    ("Joshi", 3),
    ("Shah", 4),
    ("Goyal", 4),
    ("Choudhary", 6),
    ("Kapoor", 2),
    ("Khanna", 2),
    ("Sachdeva", 3),
    ("Arora", 2),
]


# Generate random Indian names and corresponding email addresses
def generate_random_female_data():
    first_name = random.choice(first_names)
    # Select a single surname based on the probabilities
    surname = random.choices(*zip(*last_names))[0]
    full_name = first_name + " " + surname
    email = generate_random_username(full_name)
    return full_name, email.lower()  # Convert email address to lowercase

def generate_random_username(name):
    randomDigit = [3, 4, 5]
    randomSelection = random.choice(randomDigit) # Randomly select digit to generate 3 or 4 or 5 numbers
    random_number = ''.join(random.choices(string.digits, k=randomSelection)) # Random numbers of digit is generated and added at the end of the email
    email_Addres_List = ['@gmail.com', '@outlook.com', '@yahoo.com']
    # Concatenate the full name with the random number and append "@gmail.com"
    return name.replace(" ", "") + random_number + random.choice(email_Addres_List)


main()
