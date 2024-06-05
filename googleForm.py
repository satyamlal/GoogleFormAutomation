from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pyautogui
from datetime import datetime
import csv
import random
import string
import time

# Disable the PyAutoGUI fail-safe
pyautogui.FAILSAFE = False # This will prevent the fail-safe trigger from occurring when your mouse moves to a corner of the screen.

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
driver.get('https://forms.gle/mkoRtj5CaYdaVANt8')
print("Link Opened")
time.sleep(5)

# Get the screen's dimensions
screen_width, screen_height = pyautogui.size()

# Calculate the coordinates for the middle of the screen
middle_x = screen_width // 2
middle_y = screen_height // 2

counter = 0  # counter variable initialized globally

# List of common First Names
first_names = [
    "Aaradhya", "Ananya", "Jiya", "Kavya", "Mahi", "Riya", "Shreya", "Aadhya", "Aanya", "Aarohi", "Aashi", "Anika",
    "Khushi", "Manvi", "Pari", "Roshni",  "Avni", "Gauri", "Sanvi", "Sara", "Siya", "Suhani", "Tanisha", "Trisha",
    "Amaira", "Arya", "Dhriti", "Isha", "Hansa",  "Aradhana", "Kashvi", "Kiara", "Kriti", "Mahira", "Nehal", "Pihu",
    "Ridhi", "Riva", "Ruchi", "Shruti", "Sneha", "Tanvi", "Vaani", "Vanya", "Akshara", "Anvi", "Aria", "Lakshita",
    "Ankita", "Bhavya", "Chahat", "Divya", "Devika", "Shivani", "Naina", "Navya", "Mehek",  "Tanya", "Nikita",
    "Poonam", "Palak", "Radhika", "Sonia", "Urvi", "Vaishnavi", "Vanshika", "Yashika", "Aarushi", "Amaya", "Aparna",
    "Dia", "Ishaani", "Nupur", "Nandita", "Jhanvi", "Kanak", "Mansi", "Neha", "Saniya", "Priya", "Priti", "Ritika",
    "Saumya", "Nimisha", "Shanaya", "Tara", "Urvashi", "Vidhi", "Yashvi", "Anushree", "Bhavika", "Chitra", "Drishti",
    "Ishita", "Ishika", "Lavanya", "Mehak", "Niharika", "Bhawna", "Nisha", "Rachana", "Rashi", "Ruchika", "Sanya",
    "Saanvi", "Shikha", "Vani", "Aditi", "Samaira", "Aadya", "Anisha", "Apoorva", "Anvita", "Aradhya", "Charu",
    "Deeksha", "Ishani", "Juhi", "Komal", "Kritika", "Mahika", "Nandini", "Navika", "Prerna", "Priyanka", "Rishika",
    "Shivangi", "Sarika", "Tanushree", "Ria", "Yamini", "Anushka", "Arunima", "Bhavna", "Devanshi", "Ishwarya", "Jagrati",
    "Kanishka", "Mahima", "Mansi", "Nitya", "Radha", "Reema", "Rhea", "Saisha", "Sakshi", "Aarohi", "Alisha", "Arushi",
    "Anshu",  "Minal", "Aashi", "Anupriya", "Bhoomi", "Chhaya", "Deepti", "Jasmine", "Kashish", "Kashvi", "Kirti", "Lakshmi", 
    "Pari", "Pragya", "Pooja", "Ritika", "Ritvi", "Sanya", "Sakshi", "Srishti", "Tanishka", "Vaishali", "Riddham",
]

# List of common North Indian surnames with corresponding probabilities
last_names = [
    ("Sharma", 25), 
    ("Verma", 20), 
    ("Jha", 20),
    ("Singh", 15),
    ("Yadav", 10),
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
    ("Arora", 2),
]

def radio_Buttons_Page_Four(): # Page 4: Climate Change and Long-term Impacts
    
    '''Page Scrolled'''
    pageScroll(12)

    '''select random option for climate change has significantly affected agricultural productivity'''

    # Define the coordinates
    x1, y1 = 594, 263
    x2, y2 = 594, 313
    x3, y3 = 594, 365
    x4, y4 = 594, 414
    x5, y5 = 594, 463

    # Define the probabilities
    probabilities = [0.01, 0.01, 0.20, 0.70, 0.35]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    '''select random option for climate change led to a noticeable change in traditional farming practices'''

    # Define the coordinates
    x1, y1 = 594, 823
    x2, y2 = 594, 872

    # Define the probabilities
    probabilities = [0.01, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    pageScroll(15)

    '''select random option for climate change has increased the frequency and severity of natural disasters'''

    # Define the coordinates
    x1, y1 = 594, 433
    x2, y2 = 594, 481
    x3, y3 = 594, 530

    # Define the probabilities
    probabilities = [0.01, 0.75, 0.40]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    '''select random option for change in the availability of traditional food sources'''

    # Define the coordinates
    x1, y1 = 594, 838
    x2, y2 = 594, 890
    x3, y3 = 594, 941

    # Define the probabilities
    probabilities = [0.03, 0.75, 0.40]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    pageScroll(13)

    '''select random option for women in your village are more vulnerable'''

    # Define the coordinates
    x1, y1 = 594, 628
    x2, y2 = 594, 673
    x3, y3 = 594, 727

    # Define the probabilities
    probabilities = [0.03, 0.75, 0.40]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    time.sleep(1)

    return "Page 4 Completed"

def radio_Buttons_Page_Three(): # Page 3: Climate Change and Daily Life

    '''Page Scrolled'''
    pageScroll(17)

    '''select random option for climate change has significantly affected agricultural productivity'''

    # Define the coordinates
    x1, y1 = 594, 263
    x2, y2 = 594, 313
    x3, y3 = 594, 365
    x4, y4 = 594, 414
    x5, y5 = 594, 463

    # Define the probabilities
    probabilities = [0.01, 0.01, 0.20, 0.70, 0.35]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    '''select random option for climate change has led to a decrease in water availability'''

    # Define the coordinates
    x1, y1 = 594, 672
    x2, y2 = 594, 721
    x3, y3 = 594, 773
    x4, y4 = 594, 822
    x5, y5 = 594, 873

    # Define the probabilities
    probabilities = [0.01, 0.01, 0.15, 0.65, 0.30]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    pageScroll(16)

    '''select random option for increase in health issues among women'''

    # Define the coordinates
    x1, y1 = 594, 276
    x2, y2 = 594, 331
    x3, y3 = 594, 381
    x4, y4 = 594, 428
    x5, y5 = 594, 480

    # Define the probabilities
    probabilities = [0.01, 0.01, 0.05, 0.80, 0.35]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    '''select random option for women in your village now spend more time collecting water'''

    # Define the coordinates
    x1, y1 = 594, 682
    x2, y2 = 594, 736
    x3, y3 = 594, 786
    x4, y4 = 594, 837
    x5, y5 = 594, 886

    # Define the probabilities
    probabilities = [0.01, 0.01, 0.05, 0.65, 0.25]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    pageScroll(12)

    '''select random option for Has climate change contributed to increased migration'''

    # Define the coordinates
    x1, y1 = 594, 526
    x2, y2 = 594, 575
    x3, y3 = 594, 628
    x4, y4 = 594, 679
    x5, y5 = 594, 725

    # Define the probabilities
    probabilities = [0.01, 0.01, 0.05, 0.65, 0.25]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "male to female ratio in high visibility roles" section 
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()

    return "Page 3 Completed"

def page_Two_Text_Fields():

    '''select random option for Married and UnMarried Marital Status'''
    # Define the coordinates
    x1, y1 = 647, 347
    x2, y2 = 650, 400

    # Define the probabilities
    probabilities = [0.07, 0.90]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Mouse moved to select 'UnMarried' or 'Married' marital status
    pyautogui.moveTo(x=x, y=y, duration=0.8)
    pyautogui.click()
    print("Marital Status Clicked")
    print("----------------------------------------------------------------------------")


    '''Random Contact Number Generated STARTS HERE'''

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(generate_random_mobile_number()) # Contact number added
    print("Contact Number Filled")

    '''Random Contact Number Generated ENDS HERE'''


    '''Random Email Generated STARTS HERE'''
    
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    print("Email Address added in the text field:", emailAddress)

    shortTextFields.send_keys(emailAddress) # Email added
    print("Email Filled")

    '''Random Email Generated ENDS HERE'''
    
    
    '''Highest Qualification START HERE'''
    
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    
    highest_Qualification = ['B.Tech', 'M.Tech', 'BCA', 'Masters']

    # Define the probabilities
    probabilities = [0.61, 0.23, 0.1, 0.05]

    # Random choice of highest Qualification based on the probability
    qualification = random.choices(highest_Qualification, weights=probabilities)[0]

    shortTextFields.send_keys(qualification) # Highest Qualification added
    
    print("Highest Qualification Filled")
    
    '''Highest Qualification selection END HERE'''
    
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
        "MoEngage",
        "GX Group",
        "Amazon",
    ]

    # Define the probabilities
    probabilities = [0.60, 0.25, 0.25, 0.30, 0.15, 0.10, 0.10, 0.10, 0.05, 0.05, 0.35, 0.05, 0.05, 0.03, 0.01, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    companyName = random.choices(organizationName, weights=probabilities)[0]
    
    shortTextFields.send_keys(companyName) # Organization Name and Type Added Randomly
    print("Organization Name Added")
    
    '''Oraganization Name and Type ENDS HERE'''

    randomNumber = [1,2,3] # List for choosing randomly Total Professional Experience, Tenure, Total Tenure in current position, and Functional Department

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(random.choice(randomNumber)) # Total Professional Experience Added

    print("Total Professional Experience Added")

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(random.choice(randomNumber)) # Tenure in Present Organization Added
    
    print("Tenure in Present Organization Added")

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(random.choice(randomNumber)) # Total Tenure in Current Position Added
    
    print("Total Tenure in current position Added")
    
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys("IT") # Functional Department Added

    print("Functional Department Added")
    
    # Scroll the screen to the 'Designation' Section
    driver.execute_script("arguments[0].scrollIntoView(true);", shortTextFields)
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[5]/div/span/div/div/div[1]/input')))
    
    designation = ['Developer', 'Software Engineer', 'Data Scientist', 'Data Engineer', 'DevOps Engineer', 'Team Leader', 'Senior Developer']
    probabilities = [0.7, 0.3, 0.22, 0.30, 0.12, 0.02, 0.01]
    shortTextFields.send_keys(random.choices(designation, weights=probabilities)[0]) # Team Designation selected randomly
    
    print("Team Designation Added")

    return "All Text Fields completed for this Page-2"


def ageField():
    # Wait for input field to be visible and clickable
    ageTextField = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    ageTextField.clear()

    age = [21,22,23,24,25]
    ageTextField.send_keys(random.choice(age))
    print("----------------------------------------------------------------------------")
    print("Age Filled")

    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", ageTextField) # Wait for a short time to ensure the scroll operation is completed
    
    page_Two_Text_Fields()
    print("----------------------------------------------------------------------------")

    return "All Text Fields and Radio button clicked"


def nameField():
    # Wait for input field to be visible and clickable
    nameTextField = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    
    # Scroll the element into view
    # driver.execute_script("arguments[0].scrollIntoView(true);", nameTextField) # Wait for a short time to ensure the scroll operation is completed
    nameTextField.clear()

    # fullName, emailAddress = generate_random_female_data() # Random name and email generated for female
    
    nameTextField.send_keys(fullName) # Name Added

    print("----------------------------------------------------------------------------")
    print("Full Name Printed in the Name Field:", fullName)
    print
    ("----------------------------------------------------------------------------")

    return "Name Added"


def consentButton():

    pageScroll(13)

    # Wait for the "Consent" button to be clickable
    consentButtonFound = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')))
    
    # Scroll the element into view (optional)
    driver.execute_script("arguments[0].scrollIntoView(true);", consentButtonFound)

    # drop down menu arrow clicked
    dropdownMenu = driver.find_element(By.CLASS_NAME, 'e2CuFe')
    dropdownMenu.click()

    # Mouse moved to the 'Clear form' button of the pop up menu
    pyautogui.moveTo(x=706, y=294, duration=0.5)  
    pyautogui.click()

    print("----------------------------PAGE 2 STARTED----------------------------------")


    return "Consent set to YES"


def submitNextForm(): # Click on 'Submit Another Response'

    time.sleep(3)

    xPath = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
    submit_Next_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xPath)))
    submit_Next_Form_Button.click()


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

    # Wait for email button to be clickable
    email_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'uHMk6b')))
    email_button.click()
    
    return "Email checked"

def addLocation():
    # Wait for location input field to be visible and clickable
    locationElement = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    
    locationElement.clear()

    locations = [
        'Gurgaon', 'Delhi', 'Gurugram', 'Bangalore', 'London',
        'New York', 'Tokyo', 'Paris', 'Dubai', 'Singapore', 
        'Los Angeles', 'Chicago', 'Hong Kong', 'Sydney', 'San Francisco',
        'Toronto', 'Shanghai', 'Moscow', 'Mumbai', 'Mexico City',
        'Seoul', 'São Paulo', 'Istanbul', 'Jakarta', 'Buenos Aires',
        'Kuala Lumpur', 'Beijing', 'Bangkok', 'Rio de Janeiro', 'Melbourne',
        'Cairo', 'Berlin', 'Madrid', 'Rome', 'Vienna',
        'Zurich', 'Amsterdam', 'Brussels', 'Lima', 'Lisbon',
        'Johannesburg', 'Stockholm', 'Santiago', 'Warsaw', 'Munich',
        'Barcelona', 'Athens', 'Prague', 'Budapest', 'Milan'
    ]

    probabilities = [
        0.7, 0.3, 0.6, 0.65, 0.8, 0.9, 0.85, 0.8, 0.75, 0.85, 
        0.8, 0.75, 0.8, 0.7, 0.8, 0.75, 0.8, 0.65, 0.7, 0.65,
        0.8, 0.75, 0.7, 0.65, 0.7, 0.7, 0.8, 0.75, 0.7, 0.75,
        0.65, 0.7, 0.75, 0.75, 0.75, 0.8, 0.75, 0.75, 0.7, 0.75,
        0.7, 0.75, 0.7, 0.7, 0.75, 0.8, 0.7, 0.75, 0.7, 0.75
    ]

    
    locationElement.send_keys(random.choices(locations, weights=probabilities)[0])
    
    return "Location Added"

def natureOfCompany():

    pageScroll(12)

    pyautogui.moveTo(x=722, y=716, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)

    pyautogui.moveTo(x=753, y=853, duration=0.5)
    pyautogui.click()

    xPath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span' # XPATH for Page - 1 Next Button
    nextButton(xPath)

    return "Private Company selected and Moved to the Page - 2"

def pageScroll(n):
    pyautogui.moveTo(x=1910, y=1007, duration=0.5)
    # n clicks
    for _ in range(n):
        pyautogui.click()


'''This function generates random numbers each time it is called and cross checks if the number already exists before return the number'''

# Set to store generated numbers
generated_numbers = set()

def generate_random_mobile_number():
    
    global generated_numbers
    
    while True:
        # Generate a random 10-digit number
        random_digits = ''.join([str(random.randint(6, 9)) for _ in range(10)])

        # Define the prefixes with corresponding probabilities
        prefix = ['+91', '0', '']
        probabilities = [0.2, 0.3, 0.65]

        # Concatenate '+91' with the random digits
        number_prefix = random.choices(prefix, weights=probabilities)[0]
        number = number_prefix + random_digits

        # Check if the number is already generated
        if number not in generated_numbers:
            generated_numbers.add(number)
            return number


def generate_random_username(first_name, surname):
    random_digit = random.choice([3, 4, 5])  # Randomly select digit to generate 3, 4, or 5 numbers
    random_number = ''.join(random.choices(string.digits, k=random_digit))  # Generate random numbers of digits
    
    # Choose whether to use an underscore or a period between the names
    separator = random.choice(['_', '.', ''])
    
    # Concatenate the first name and surname with the separator
    email_name = f"{first_name}{separator}{surname}"
    
    # Randomly decide whether to add an additional period after the names
    if random.choice([True, False]):
        email_name += '.'
    
    # Choose email domain based on probabilities
    email_address_list = ['@gmail.com', '@outlook.com', '@yahoo.com']
    probabilities = [0.91, 0.05, 0.04]
    email_domain = random.choices(email_address_list, weights=probabilities)[0]
    
    # Concatenate the email name with the random number and append the selected email domain
    return email_name + random_number + email_domain


# Generate random Indian names and corresponding email addresses
def generate_random_female_data():
    
    # Select a first name randomly
    first_name = random.choice(first_names)

    # Select a single surname based on the probabilities
    surname = random.choices(*zip(*last_names))[0]
    
    # Generate a full name by concatenating first_name and surname
    full_name = first_name + " " + surname
    
    # New email will be generate by passing the full_name as parameter to the generate_random_username function
    email = generate_random_username(first_name, surname)
    
    return full_name, email.lower()  # Convert email address to lowercase


# Function to write data to CSV file
def write_to_csv(data):
    file_name = "google_Form_Submissions.csv"
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def record_timestamp():
    # Get current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Write two empty lines to CSV file
    for _ in range (2):
        write_to_csv([])

    # Write timestamp to CSV file
    write_to_csv(["Timestamp", timestamp])


def main():

    global counter # global counter variable initialized

    try:

        # Record timestamp before adding any other data
        record_timestamp()

        # Write FULL NAME, EMAIL ADDRESS, CONTACT NUMBER before starting the to write any other data
        write_to_csv(["FULL NAME", "EMAIL ADDRESS", "CONTACT NUMBER"])

        while counter <= 1:

            fullName, emailAddress = generate_random_female_data()
            mobileNumber = generate_random_mobile_number()

            '''Page 1 submission STARTS HERE'''

            print("----------------------------PAGE 1 STARTED----------------------------------")

            formCleared = clearForm() # This function is used to clear the form using the 'Clear form' button
            print(formCleared)

            email_check = emailChecked() # This function is used for check box
            print(email_check)
            time.sleep(1)

            currentlyLiving = addLocation() # Currently Living In Text Field
            print(currentlyLiving)

            companySelected = natureOfCompany() # This function is used for drop down menu
            print(companySelected)
            time.sleep(1)

            '''Page 1 submission ENDS HERE'''

            print("----------------------------PAGE 1 ENDS HERE-------------------------------")

            time.sleep(1)

            '''Page 2 submission STARTS HERE'''

            print("----------------------------PAGE 2 STARTED----------------------------------")

            # Climate Change and Rural Women: Insights from Urban Professionals

            consentButtonClicked = consentButton() # This function is used for drop down menu
            print(consentButtonClicked)

            nameAdded = nameField() # This function is used to fill the name text field
            print(nameAdded)

            ageAdded = ageField() # This function is used to fill the age text field
            print(ageAdded)
            
            '''Page 2 submission ENDS HERE'''

            print("----------------------------PAGE 2 ENDS HERE-------------------------------")

            time.sleep(1) # Wait for 2 seconds before clicking the NEXT button

            # Next Button clicked to enter page - 3
            xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span'
            nextButton(xpath)

            time.sleep(5)

            '''Page 3 submission STARTS HERE'''

            # print("----------------------------PAGE 3 STARTED----------------------------------")

            page_Three_Radio_Buttons_Clicked = radio_Buttons_Page_Three()
            print(page_Three_Radio_Buttons_Clicked)

            time.sleep(2)

            # Next Button clicked to enter page - 4
            xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span'
            nextButton(xpath)

            # print("All Radio Buttons Clicked Successfully")

            # print("----------------------------PAGE 3 ENDS HERE-------------------------------")

            '''Page 3 submission ENDS HERE'''

            time.sleep(5)

            '''Page 4 submission STARTS HERE'''

            print("----------------------------PAGE 4 STARTED----------------------------------")
            
            '''Topic: Climate Change and Long-term Impacts'''

            page_Four_Radio_Buttons_Clicked = radio_Buttons_Page_Four()
            print(page_Four_Radio_Buttons_Clicked)

            # Next Button clicked to enter page - 4
            xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span'
            nextButton(xpath)

            print("All Radio Buttons Clicked Successfully")

            print("----------------------------PAGE 4 ENDS HERE-------------------------------")
            print()
            print()

            '''Page 4 submission ENDS HERE'''

            submitNextForm() # Click on 'Submit Next Form / Response'

            # Write data to CSV file
            write_to_csv([fullName, emailAddress, mobileNumber])
            
            counter += 1 # Counter increases after every successful form submission
            
        # Write counter value to CSV file
        write_to_csv(["Counter:", counter])

        print("~~~~~~~~~~~~~~~~~~~~")
        print("Counter:", counter)
        print("~~~~~~~~~~~~~~~~~~~~")
        print()
        print()

    except TimeoutException:
        print("Timeout occurred: Element not found within the specified time")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


fullName, emailAddress = generate_random_female_data()

if __name__ == "__main__":
    main()
