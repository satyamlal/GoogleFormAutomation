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
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdmONEy9LcFGnlKWF7IEVlvvEm08-wvP2li7w_MDBicsdRZLw/viewform?vc=0&c=0&w=1&flr=0')
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


def radio_Buttons_Page_Eight(): # Page 8: Impact on the performance due to the perception of glass ceiling
    time.sleep(3)

    '''Page Scrolled'''
    pageScroll(10)
    
    '''select random option for more women participation'''
    # Define the coordinates
    x1, y1 = 593, 356
    x2, y2 = 593, 405
    x3, y3 = 590, 456
    x4, y4 = 593, 505
    x5, y5 = 593, 557

    # Define the probabilities
    probabilities = [0.02, 0.03, 0.37, 0.77, 0.05]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for zero tolerance over harassment'''
    # Define the coordinates
    x1, y1 = 592, 895
    x2, y2 = 594, 941
    x3, y3 = 590, 993

    # Define the probabilities
    probabilities = [0.05, 0.77, 0.34]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(18)


    '''select random option for Allowing more women to manage teams'''
    # Define the coordinates
    x1, y1 = 593, 399
    x2, y2 = 593, 448
    x3, y3 = 590, 500

    # Define the probabilities
    probabilities = [0.05, 0.77, 0.35]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for Women foster creativity'''
    # Define the coordinates
    x1, y1 = 593, 778
    x2, y2 = 593, 827
    x3, y3 = 590, 876

    # Define the probabilities
    probabilities = [0.02, 0.77, 0.45]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(16)


    '''select random option for Having higher women representation at decision making roles'''
    # Define the coordinates
    x1, y1 = 592, 435
    x2, y2 = 592, 483

    # Define the probabilities
    probabilities = [0.61, 0.23]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for Women qualities of  empathy and sensitivity lead to effective team management'''
    # Define the coordinates
    x1, y1 = 593, 793
    x2, y2 = 593, 842
    x3, y3 = 593, 890

    # Define the probabilities
    probabilities = [0.02, 0.87, 0.33]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(15)


    '''select random option for Women contribute to business sustainability through less risky decisions'''
    # Define the coordinates
    x1, y1 = 593, 580
    x2, y2 = 593, 633

    # Define the probabilities
    probabilities = [0.93, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    return "Page 8 Done: Full Form Submitted Completely"



def radio_Buttons_Page_Seven(): # Page 7: Perception of Glass Ceiling
    time.sleep(3)

    '''Page Scrolled'''
    pageScroll(10)

    '''select random option for women managers have to work harder than male'''
    # Define the coordinates
    x1, y1 = 592, 357
    x2, y2 = 592, 407
    x3, y3 = 592, 457
    x4, y4 = 592, 505
    x5, y5 = 592, 557

    # Define the probabilities
    probabilities = [0.02, 0.07, 0.10, 0.65, 0.10]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for women do not receive the same level of recognition like men'''
    # Define the coordinates
    x1, y1 = 595, 734
    x2, y2 = 592, 784
    x3, y3 = 592, 833
    x4, y4 = 592, 884
    x5, y5 = 593, 934

    # Define the probabilities
    probabilities = [0.02, 0.06, 0.10, 0.45, 0.12]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(17)


    '''select random option for leadership in my company supports the view of “think managers, think male attitude'''
    # Define the coordinates
    x1, y1 = 593, 290
    x2, y2 = 593, 338
    x3, y3 = 592, 392
    x4, y4 = 594, 439
    x5, y5 = 591, 488

    # Define the probabilities
    probabilities = [0.01, 0.10, 0.40, 0.30, 0.06]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for female managers face career plateaus'''
    # Define the coordinates
    x1, y1 = 595, 696
    x2, y2 = 592, 748
    x3, y3 = 593, 797
    x4, y4 = 593, 847
    x5, y5 = 593, 895

    # Define the probabilities
    probabilities = [0.01, 0.07, 0.40, 0.30, 0.05]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(17)


    '''select random option for male employees dominate the communication networks'''
    # Define the coordinates
    x1, y1 = 594, 283
    x2, y2 = 594, 333
    x3, y3 = 594, 388
    x4, y4 = 592, 435
    x5, y5 = 593, 482

    # Define the probabilities
    probabilities = [0.02, 0.07, 0.55, 0.25, 0.03]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for situations of downsizing, women employees are removed first'''
    # Define the coordinates
    x1, y1 = 593, 661
    x2, y2 = 593, 709
    x3, y3 = 592, 761
    x4, y4 = 592, 811
    x5, y5 = 593, 861

    # Define the probabilities
    probabilities = [0.05, 0.12, 0.75, 0.15, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    return "All Radion Button Clicked Successfully on Page - 7"


def radio_Buttons_Page_Six(): # Page 6: Perception of Differential treatment

    '''Page Scrolled'''
    pageScroll(10)
    
    '''select random option for My company honours the pay parity policies for same responsibilities to men and women'''
    # Define the coordinates
    x1, y1 = 592, 453
    x2, y2 = 592, 504

    # Define the probabilities
    probabilities = [0.01, 0.90]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()
    

    '''select random option for designations and titles for the same job responsibilities are different'''
    # Define the coordinates
    x1, y1 = 592, 813
    x2, y2 = 592, 911

    # Define the probabilities
    probabilities = [0.95, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''Page Scrolled'''
    pageScroll(18)

    '''select random option for scope of higher representation of women'''
    # Define the coordinates
    x1, y1 = 595, 322
    x2, y2 = 593, 369
    x3, y3 = 590, 419

    # Define the probabilities
    probabilities = [0.02, 0.15, 0.60]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''select random option for generally less accepting of a female leader'''
    # Define the coordinates
    x1, y1 = 595, 774
    x2, y2 = 593, 822

    # Define the probabilities
    probabilities = [0.30, 0.70]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''Page Scrolled'''
    pageScroll(16)

    '''select random option for routine jobs have more women compared to men'''
    # Define the coordinates
    x1, y1 = 594, 302
    x2, y2 = 595, 356

    # Define the probabilities
    probabilities = [0.60, 0.20]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''select random option for had to skip appraisal because of personal reasons'''
    # Define the coordinates
    x1, y1 = 594, 682
    x2, y2 = 595, 730
    x3, y3 = 595, 780

    # Define the probabilities
    probabilities = [0.60, 0.20, 0.02]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''Page Scrolled'''
    pageScroll(15)

    '''select random option for Senior management is vocal and supportive of the issues of female managers'''
    # Define the coordinates
    x1, y1 = 593, 358
    x2, y2 = 591, 411

    # Define the probabilities
    probabilities = [0.70, 0.10]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''select random option for Regular gender audits'''
    # Define the coordinates
    x1, y1 = 593, 720
    x2, y2 = 591, 764

    # Define the probabilities
    probabilities = [0.65, 0.8]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()
    
    return "All Radion Button Clicked Successfully on Page - 6"

def radio_Buttons_Page_Five(): # Page 5: Individual/ Personality Related Statements

    '''Page Scrolled'''
    pageScroll(10)

    '''Cursor moved to past career experiences'''
    # Define the coordinates
    x, y = 593, 403

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.click()

    '''select random option for lack of education : STEM'''
    # Define the coordinates
    x1, y1 = 593, 861
    x2, y2 = 590, 914
    x3, y3 = 592, 962

    # Define the probabilities
    probabilities = [0.05, 0.65, 0.35]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''Page Scrolled'''
    pageScroll(17)

    '''Select for averse to taking risky and challenging job assignments'''
    # Define the coordinates
    x, y = 594, 339

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.click()

    '''select random option encounter self limiting judgements'''
    # Define the coordinates
    x1, y1 = 593, 747
    x2, y2 = 591, 794
    x3, y3 = 590, 844

    # Define the probabilities
    probabilities = [0.05, 0.75, 0.40]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''Page Scrolled'''
    pageScroll(16)

    '''select random option shy from voicing my concerns'''
    # Define the coordinates
    x1, y1 = 593, 355
    x2, y2 = 592, 402
    x3, y3 = 592, 455

    # Define the probabilities
    probabilities = [0.10, 0.55, 0.40]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    
    '''select random option shy from voicing my concerns'''
    # Define the coordinates
    x1, y1 = 591, 763
    x2, y2 = 592, 810

    # Define the probabilities
    probabilities = [0.70, 0.30]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''Page Scrolled'''
    pageScroll(16)

    '''select random option for not comfortable in taking up roles that involve relocation'''
    # Define the coordinates
    x1, y1 = 593, 366
    x2, y2 = 592, 417
    x3, y3 = 592, 465
    x4, y4 = 594, 517

    # Define the probabilities
    probabilities = [0.30, 0.20, 0.45, 0.10]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''select random option for not comfortable in taking up roles that involve relocation'''
    # Define the coordinates
    x1, y1 = 593, 726
    x2, y2 = 592, 773
    x3, y3 = 592, 826
    x4, y4 = 594, 874
    x5, y5 = 593, 924

    # Define the probabilities
    probabilities = [0.10, 0.03, 0.05, 0.70, 0.20]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''Page Scrolled'''
    pageScroll(17)

    '''select random option for when my work interferes with my family sphere'''
    # Define the coordinates
    x1, y1 = 592, 283
    x2, y2 = 592, 333
    x3, y3 = 592, 381
    x4, y4 = 594, 431
    x5, y5 = 593, 483

    # Define the probabilities
    probabilities = [0.15, 0.40, 0.10, 0.05, 0.02]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''select random option for Post motherhood'''
    # Define the coordinates
    x1, y1 = 593, 659
    x2, y2 = 592, 709
    x3, y3 = 592, 759
    x4, y4 = 594, 805
    x5, y5 = 593, 857

    # Define the probabilities
    probabilities = [0.01, 0.05, 0.10, 0.70, 0.20]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    time.sleep(3)

    return "All Radion Buttons Clicked Successfully on Page - 5"


def radio_Buttons_Page_Four(): # Page 4: Social and Cultural Related Statements

    time.sleep(3)
    
    '''Page Scrolled'''
    pageScroll(10)

    '''select random option for women are conditioned to be the caregivers'''
    # Define the coordinates
    x1, y1 = 594, 356
    x2, y2 = 593, 402
    x3, y3 = 592, 454
    x4, y4 = 591, 505
    x5, y5 = 593, 555

    # Define the probabilities
    probabilities = [0.01, 0.02, 0.30, 0.35, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for women are stereotyped to be less ambitious'''
    # Define the coordinates
    x1, y1 = 594, 734
    x2, y2 = 593, 783
    x3, y3 = 594, 831
    x4, y4 = 591, 880
    x5, y5 = 593, 934

    # Define the probabilities
    probabilities = [0.01, 0.02, 0.30, 0.40, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(17)

    '''select random option for more family responsibilities slowing the rate of career advancement'''
    # Define the coordinates
    x1, y1 = 596, 284
    x2, y2 = 592, 337
    x3, y3 = 593, 388
    x4, y4 = 592, 440
    x5, y5 = 592, 490

    # Define the probabilities
    probabilities = [0.01, 0.02, 0.20, 0.35, 0.05]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''select random option for My family and spouse support me'''
    # Define the coordinates
    x1, y1 = 597, 668
    x2, y2 = 592, 714
    x3, y3 = 591, 767
    x4, y4 = 591, 818
    x5, y5 = 594, 867

    # Define the probabilities
    probabilities = [0.01, 0.02, 0.20, 0.35, 0.05]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(16)


    '''select random option for My paid domestic help'''
    # Define the coordinates
    x1, y1 = 594, 394
    x2, y2 = 592, 443

    # Define the probabilities
    probabilities = [0.25, 0.60]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''select random option for pre-defined gender roles'''
    # Define the coordinates
    x1, y1 = 593, 747
    x2, y2 = 593, 800

    # Define the probabilities
    probabilities = [0.60, 0.30]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    time.sleep(3)

    return "----------------------------PAGE 4 ENDS HERE--------------------------------"


def radio_Buttons_Page_Three(): # Page 3: Regulations Related Statements

    time.sleep(5)

    '''Page Scrolled'''
    pageScroll(11)

    '''select random option for organization is considerate of the requests'''
    # Define the coordinates
    x1, y1 = 593, 310
    x2, y2 = 590, 354
    x3, y3 = 592, 405
    x4, y4 = 593, 457
    x5, y5 = 592, 506

    # Define the probabilities
    probabilities = [0.01, 0.05, 0.40, 0.30, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for Company doesn't provide support facilities'''
    # Define the coordinates
    x1, y1 = 594, 680
    x2, y2 = 594, 733
    x3, y3 = 594, 783
    x4, y4 = 594, 831
    x5, y5 = 594, 883

    # Define the probabilities
    probabilities = [0.01, 0.25, 0.35, 0.10, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''Page Scrolled'''
    pageScroll(15)

    '''select random option for policies related to reentry of employees after sabbaticals'''
    # Define the coordinates
    x1, y1 = 590, 308
    x2, y2 = 592, 358
    x3, y3 = 592, 400
    x4, y4 = 590, 460
    x5, y5 = 592, 510

    # Define the probabilities
    probabilities = [0.01, 0.03, 0.40, 0.15, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for paid menstrual leaves'''
    # Define the coordinates
    x1, y1 = 592, 684
    x2, y2 = 594, 736
    x3, y3 = 593, 785
    x4, y4 = 593, 834
    x5, y5 = 593, 886

    # Define the probabilities
    probabilities = [0.01, 0.20, 0.40, 0.05, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(15)


    '''select random option for maternity leaves are honored'''
    # Define the coordinates
    x1, y1 = 593, 344
    x2, y2 = 592, 391
    x3, y3 = 590, 444
    x4, y4 = 591, 490
    x5, y5 = 590, 542

    # Define the probabilities
    probabilities = [0.01, 0.10, 0.25, 0.40, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    '''select random option for does not provide transportation facilities'''
    # Define the coordinates
    x1, y1 = 594, 749
    x2, y2 = 592, 800
    x3, y3 = 593, 851
    x4, y4 = 594, 902
    x5, y5 = 592, 948

    # Define the probabilities
    probabilities = [0.01, 0.60, 0.35, 0.10, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()
    
    '''Page Scrolled'''
    pageScroll(17)

    '''select random option for higher scope of women representation in the board positions'''
    # Define the coordinates
    x1, y1 = 592, 277
    x2, y2 = 594, 326
    x3, y3 = 592, 376
    x4, y4 = 592, 425
    x5, y5 = 593, 478

    # Define the probabilities
    probabilities = [0.01, 0.50, 0.35, 0.05, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()


    '''select random option for several important positions are occupied by the same set of women managers'''
    # Define the coordinates
    x1, y1 = 593, 687
    x2, y2 = 593, 733
    x3, y3 = 594, 786
    x4, y4 = 591, 836
    x5, y5 = 594, 883

    # Define the probabilities
    probabilities = [0.01, 0.10, 0.65, 0.05, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    # Move the cursor to "related to flexible timings" section 
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()

    return "Page 3 Completed"


def radio_Buttons_Page_Two(): # Page 2: Respondent Profile

    '''Page Scrolled'''
    pageScroll(13)

    '''select random option for Male to Female Ratio in high visibility roles'''

    # Define the coordinates
    x1, y1 = 698, 325
    x2, y2 = 636, 381
    x3, y3 = 654, 428
    x4, y4 = 638, 481
    x5, y5 = 686, 525

    # Define the probabilities
    probabilities = [0.01, 0.05, 0.40, 0.30, 0.01]

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
    probabilities = [0.01, 0.05, 0.50, 0.30, 0.01]

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
    probabilities = [0.05, 0.40, 0.30, 0.15, 0.02]

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
    probabilities = [0.01, 0.02, 0.10, 0.35, 0.40]

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
    probabilities = [0.01, 0.02, 0.05, 0.40, 0.50]

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
    probabilities = [0.01, 0.10, 0.40, 0.30, 0.03]

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
    probabilities = [0.01, 0.10, 0.40, 0.30, 0.02]

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
    probabilities = [0.01, 0.02, 0.35, 0.45, 0.12]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]
    pyautogui.moveTo(x=x, y=y, duration=0.2)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(15)


    '''select random option for gender-neutral and supportive'''
    # Define the coordinates
    x1, y1 = 725, 296
    x2, y2 = 666, 343
    x3, y3 = 644, 394
    x4, y4 = 645, 444
    x5, y5 = 663, 494

    # Define the probabilities
    probabilities = [0.01, 0.01, 0.25, 0.40, 0.15]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]
    pyautogui.moveTo(x=x, y=y, duration=0.5)
    pyautogui.click()


    '''select random option for transparent and objective recruitment'''
    # Define the coordinates
    x1, y1 = 595, 700
    x2, y2 = 592, 748
    x3, y3 = 592, 798
    x4, y4 = 591, 850
    x5, y5 = 594, 902

    # Define the probabilities
    probabilities = [0.01, 0.02, 0.35, 0.50, 0.02]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    pyautogui.moveTo(x=x, y=y, duration=0.5)
    pyautogui.click()


    '''Page Scrolled'''
    pageScroll(15)


    '''select random option based on probability for Promotion Criteria'''
    # Define the coordinates
    x1, y1 = 714, 326
    x2, y2 = 648, 378
    x3, y3 = 656, 428
    x4, y4 = 644, 478
    x5, y5 = 667, 528

    # Define the probabilities
    probabilities = [0.01, 0.02, 0.10, 0.50, 0.35]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    pyautogui.moveTo(x=x, y=y, duration=0.5)
    pyautogui.click()


    '''select random option for Female Managers at top levels'''
    # Define the coordinates
    x1, y1 = 676, 734
    x2, y2 = 639, 784
    x3, y3 = 656, 834
    x4, y4 = 653, 884
    x5, y5 = 684, 932

    # Define the probabilities
    probabilities = [0.01, 0.02, 0.30, 0.50, 0.25]

    # Choose between the two sets of coordinates based on probabilities
    x, y = random.choices([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], weights=probabilities)[0]

    pyautogui.moveTo(x=x, y=y, duration=0.5)
    pyautogui.click()

    # Page Scrolled down
    pageScroll(15)

    return "Page 2 Completed"

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
    print("----------------------------------------------------------------------------")
    print("Marital Status Clicked")

    time.sleep(5)    

    '''Random Contact Number Generated STARTS HERE'''

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(generate_random_mobile_number()) # Contact number added

    '''Random Contact Number Generated ENDS HERE'''


    '''Random Email Generated STARTS HERE'''
    
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    print("Email Address added in the text field:", emailAddress)

    shortTextFields.send_keys(emailAddress) # Email added

    '''Random Email Generated ENDS HERE'''
    
    
    '''Highest Qualification START HERE'''
    
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    
    highest_Qualification = ['B.Tech', 'M.Tech', 'BCA', 'Masters']

    # Define the probabilities
    probabilities = [0.61, 0.23, 0.1, 0.05]

    # Random choice of highest Qualification based on the probability
    qualification = random.choices(highest_Qualification, weights=probabilities)[0]

    shortTextFields.send_keys(qualification) # Highest Qualification added
    print("----------------------------------------------------------------------------")
    print("Highest Qualification Added Successfully")
    
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
        "Amazon,",
    ]

    # Define the probabilities
    probabilities = [0.60, 0.25, 0.25, 0.30, 0.15, 0.10, 0.10, 0.10, 0.05, 0.05, 0.35, 0.05, 0.05, 0.03, 0.01, 0.01]

    # Choose between the two sets of coordinates based on probabilities
    companyName = random.choices(organizationName, weights=probabilities)[0]
    
    shortTextFields.send_keys(companyName) # Organization Name and Type Added Randomly
    print("----------------------------------------------------------------------------")
    print("Organization Name Added")
    
    '''Oraganization Name and Type ENDS HERE'''


    randomNumber = [1,2,3] # List of three numbers

    time.sleep(5)

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(random.choice(randomNumber)) # Total Professional Experience Added

    time.sleep(5)

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(random.choice(randomNumber)) # Tenure in Present Organization Added

    time.sleep(5)

    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys(random.choice(randomNumber)) # Total Tenure in Current Position Added

    time.sleep(5)
    
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    shortTextFields.send_keys("IT") # Functional Department Added

    time.sleep(5)

    # Scroll the screen to the 'Designation' Section
    driver.execute_script("arguments[0].scrollIntoView(true);", shortTextFields)
    shortTextFields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[5]/div/span/div/div/div[1]/input')))
    
    designation = ['Developer', 'Software Engineer', 'Data Scientist', 'Data Engineer', 'DevOps Engineer', 'Team Leader', ]
    probabilities = [0.7, 0.3, 0.22, 0.30, 0.12, 0.02]
    shortTextFields.send_keys(random.choices(designation, weights=probabilities)[0]) # Team Designation selected randomly


    return "All Text Fields completed for this Page-2"


def ageField():
    # Wait for input field to be visible and clickable
    ageTextField = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    ageTextField.clear()

    age = [21,22,23,24,25]
    ageTextField.send_keys(random.choice(age))
    print("----------------------------------------------------------------------------")
    print("New Age Filled")

    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", ageTextField) # Wait for a short time to ensure the scroll operation is completed
    page_Two_Text_Fields()
    print("----------------------------------------------------------------------------")

    time.sleep(5)

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
    print("Email Address:", emailAddress)
    print
    ("----------------------------------------------------------------------------")
    
    time.sleep(5)

    return "Name Added"


def consentButton():
    # Wait for the "Clear" button to be clickable
    consentButtonFound = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')))
    
    # Scroll the element into view (optional)
    driver.execute_script("arguments[0].scrollIntoView(true);", consentButtonFound)

    # drop down menu arrow clicked
    dropdownMenu = driver.find_element(By.CLASS_NAME, 'e2CuFe')
    dropdownMenu.click()

    # Mouse moved to the 'Clear form' button of the pop up menu
    pyautogui.moveTo(x=650, y=300, duration=0.5)  
    pyautogui.click()

    time.sleep(5)

    print("----------------------------PAGE 2 STARTED----------------------------------")

    return "Consent set to YES"


def submitNextForm(): # Click on 'Submit Another Response'

    time.sleep(300)

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


def addFiCode():
    # Wait for fiCodeElement input field to be visible and clickable
    fiCodeElement = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", fiCodeElement) # Wait for a short time to ensure the scroll operation is completed
    fiCodeElement.clear()
    
    fiCodeElement.send_keys("12")
    
    return "FI Code: Text Field Cleared and Added 12 in it"

def addLocation():
    # Wait for location input field to be visible and clickable
    locationElement = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    
    locationElement.clear()

    locations = ['Gurgaon', 'Delhi', 'Gurugram']
    probabilities = [0.7, 0.3, 0.6]
    
    locationElement.send_keys(random.choices(locations, weights=probabilities)[0])
    
    return "Location Added"

def dropdownAction():
    dropdownMenu = driver.find_element(By.CLASS_NAME, 'e2CuFe')
    dropdownMenu.click()
    time.sleep(0.5)

    # Mouse moved to the 'Clear form' button of the pop up menu
    pyautogui.moveTo(x=850, y=850, duration=0.5)
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
    file_name = "google_Form_Female_Data.csv"
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def record_timestamp():
    # Get current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Write two empty lines to CSV file
    write_to_csv([])
    write_to_csv([])

    # Write timestamp to CSV file
    write_to_csv(["Timestamp", timestamp])


def main():
    global counter  # global counter variable

    try:

        # Record timestamp before adding any other data
        record_timestamp()

        # Write FULL NAME, EMAIL ADDRESS, CONTACT NUMBER before starting the to write any other data
        write_to_csv(["FULL NAME", "EMAIL ADDRESS", "CONTACT NUMBER"])

        while counter < 3:

            fullName, emailAddress = generate_random_female_data()
            mobileNumber = generate_random_mobile_number()

            '''Page 1 submission STARTS HERE'''

            print("----------------------------PAGE 1 STARTED----------------------------------")

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

            '''Page 1 submission ENDS HERE'''

            print("----------------------------PAGE 1 ENDS HERE-------------------------------")

            time.sleep(2)

            
            '''Page 2 submission STARTS HERE'''

            print("----------------------------PAGE 2 STARTED----------------------------------")


            consentButtonClicked = consentButton() # This function is used for drop down menu
            print(consentButtonClicked)
            time.sleep(1)

            nameAdded = nameField() # This function is used to fill the name text field
            print(nameAdded)

            ageAdded = ageField() # This function is used to fill the age text field
            print(ageAdded)
            
            page_Two_Radio_Buttons_Clicked = radio_Buttons_Page_Two()
            print(page_Two_Radio_Buttons_Clicked)

            
            '''Page 2 submission ENDS HERE'''

            print("----------------------------PAGE 2 ENDS HERE-------------------------------")


            time.sleep(2) # Wait for few seconds before clicking the NEXT button

            # Next Button clicked to enter page - 3
            xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span'
            nextButton(xpath)


            '''Page 3 submission STARTS HERE'''

            print("----------------------------PAGE 3 STARTED----------------------------------")

            page_Three_Radio_Button_Clicked = radio_Buttons_Page_Three()
            print(page_Three_Radio_Button_Clicked)
            print("All Radio Buttons Clicked Successfully")

            print("----------------------------PAGE 3 ENDS HERE-------------------------------")

            '''Page 3 submission ENDS HERE'''


            time.sleep(2)


            xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span'
            nextButton(xpath) # Next Button clicked to enter page - 4


            '''Page 4 submission STARTS HERE'''

            print("----------------------------PAGE 4 STARTED----------------------------------")

            page_Four_Radio_Button_Clicked = radio_Buttons_Page_Four()
            print("All Radion Button Clicked Successfully on Page - 4")
            print(page_Four_Radio_Button_Clicked)

            '''Page 4 submission ENDS HERE'''

            xPath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span' # XPATH for Page - 4 Next Button
            nextButton(xPath) # Next Button clicked to enter page - 5

            time.sleep(4) # Wait for the new page to load properly

            '''Page 5 submission STARTS HERE'''

            print("----------------------------PAGE 5 STARTED----------------------------------")

            page_Five_Radio_Button_Clicked = radio_Buttons_Page_Five()
            print(page_Five_Radio_Button_Clicked)

            print("----------------------------PAGE 5 ENDS HERE-------------------------------")

            '''Page 5 submission ENDS HERE'''

            time.sleep(2)

            xPath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span' # XPATH for Page - 5 Next Button
            nextButton(xPath) # Next Button clicked to enter page - 6

            '''Page 6 submission STARTS HERE'''
            
            print("----------------------------PAGE 6 STARTED----------------------------------")

            page_Six_Radio_Button_Clicked = radio_Buttons_Page_Six()
            print(page_Six_Radio_Button_Clicked)

            print("----------------------------PAGE 6 ENDS HERE-------------------------------")

            '''Page 6 submission ENDS HERE'''


            time.sleep(2)


            xPath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span' # XPATH for Page - 6 Next Button
            nextButton(xPath) # Next Button clicked to enter page - 7


            '''Page 7 submission STARTS HERE'''
            
            print("----------------------------PAGE 7 STARTED----------------------------------")

            page_Seven_Radio_Button_Clicked = radio_Buttons_Page_Seven()
            print(page_Seven_Radio_Button_Clicked)

            print("----------------------------PAGE 7 ENDS HERE-------------------------------")

            '''Page 7 submission ENDS HERE'''
            
            time.sleep(2)

            xPath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span' # XPATH for Page - 7 Next Button
            nextButton(xPath) # Next Button clicked to enter page - 8


            '''Page 8 submission STARTS HERE'''
            
            print("----------------------------PAGE 8 STARTED----------------------------------")

            page_Eight_Radio_Button_Clicked = radio_Buttons_Page_Eight()
            print(page_Eight_Radio_Button_Clicked)

            print("----------------------------PAGE 8 ENDS HERE-------------------------------")

            '''Page 8 submission ENDS HERE'''

            xPath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]/span/span' # XPATH for Page - 8 Submit Button
            nextButton(xPath) # Submit Button clicked to start new form Submission

            time.sleep(5)

            submitNextForm() # Click on 'Submit Next Form / Response'

            counter += 1 # Counter increases after every successful form submission

            # Write data to CSV file
            write_to_csv([fullName, emailAddress, mobileNumber])
            
        # Write counter value to CSV file
        write_to_csv(["Counter:", counter])

        print("~~~~~~~~~~~~~~~~~~~~")
        print("Counter:", counter)
        print("~~~~~~~~~~~~~~~~~~~~")

    except TimeoutException:
        print("Timeout occurred: Element not found within the specified time")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


fullName, emailAddress = generate_random_female_data()

if __name__ == "__main__":
    main()
