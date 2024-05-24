# Automate Google form

Specific for this google [form](https://docs.google.com/forms/d/e/1FAIpQLScGeZlDpHIDETBqFf-dabEpW-OV6Sd0nMeJGlC0olYuT2hySA/viewform?usp=sf_link).

This Python Script automatically fill Google Form.
This code is written for **Harvard CS50 Final Project**.


## Video Demo Link
Harvard CS50P Final Project YouTube Video [Link]()


## Requirements -
- Python3

- Selenium WebDriver

- Selenium Chrome Driver

- PyAutoGUI


## Project Description

This program is designed to automatically open the Google Chrome browser using Python Selenium and fill out Google Forms. Here are the key features:

- **Pre-requisite:** The program only functions if you are already logged into your Gmail account.

- **Automated Form Filling:** The program uses XPath to automatically fill in all short answer text fields on a Google Form.

- **Random Data Generation:** It can generate random contact numbers, full names, and email addresses for each form submission, ensuring no repetitions.

- **Dropdown Menus and Radio Buttons:** PyAutoGUI is used to explicitly move the cursor to fill dropdown menus and select radio buttons. This is achieved by using (x, y) coordinates to move the cursor.

- **Random Option Selection:** For each radio button question, the program randomly picks an option based on the probability associated with the (x, y) coordinates.

- **Unlimited Submissions:** The program can submit an unlimited number of forms non-stop once executed. This is controlled by a while loop that manages the number of submissions.


## Disclaimer

Disclaimer: This project is made solely for educational purpose and should be treated as proof of concept. This should not be used for any ill purpose.