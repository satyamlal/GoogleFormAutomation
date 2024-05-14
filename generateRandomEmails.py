import random
import string

# List of common First Names
first_names = [
    "Aarav", "Aryan", "Aditya", "Ansh", "Ayush", "Dev", "Dhruv", "Kabir", "Karan", "Rohan",
    "Neha", "Aaradhya", "Ananya", "Isha", "Jiya", "Kavya", "Mahi", "Misha", "Prisha", "Riya",
    "Aadi", "Aaditya", "Aarush", "Advik", "Arjun", "Vivaan", "Vihaan", "Aayan", "Reyansh", "Atharva",
    "Sai", "Vedant", "Rudra", "Aaryan", "Shaurya", "Darsh", "Parth", "Daksh", "Yash", "Krish", "Shreya", "Riddham",
    "Pinky",
]

# List of common North Indian surnames with corresponding probabilities
last_names = [
    ("Sharma", 25), 
    ("Verma", 25), 
    ("Jha", 25), 
    ("Singh", 25), 
    ("Yadav", 15), 
    ("Gupta", 10), 
    ("Malhotra", 5), 
    ("Bhatia", 5), 
    ("Chopra", 5), 
    ("Mittal", 5),
    ("Pandey", 7), 
    ("Tiwari", 6), 
    ("Shukla", 6), 
    ("Garg", 4), 
    ("Agarwal", 10), 
    ("Kumar", 10), 
    ("Chauhan", 10), 
    ("Sinha", 10), 
    ("Joshi", 3), 
    ("Shah", 4),
    ("Goyal", 4), 
    ("Saxena", 4), 
    ("Choudhary", 6), 
    ("Seth", 3),
    ("Kapoor", 2), 
    ("Khanna", 2),
    ("Sachdeva", 3), 
    ("Chadha", 4),
    ("Arora", 2),
]

# Maintain a set to store generated email addresses
generated_emails = set()

def generate_random_username(name):
    randomDigit = [3, 4, 5]
    randomSelection = random.choice(randomDigit) # Randomly select digit to generate 3 or 4 or 5 numbers
    random_number = ''.join(random.choices(string.digits, k=randomSelection)) # Random numbers of digit is generated and added at the end of the email
    email_Addres_List = ['@gmail.com', '@outlook.com', '@yahoo.com']
    # Concatenate the full name with the random number and append "@gmail.com"
    return name.replace(" ", "") + random_number + random.choice(email_Addres_List)

# Generate random Indian names and corresponding email addresses
full_names = []
gmail_addresses = []
for _ in range(10):
    first_name = random.choice(first_names)
    # Select a single surname based on the probabilities
    surname = random.choices(*zip(*last_names))[0]
    full_name = first_name + " " + surname
    email = generate_random_username(full_name)
    # Check if the email has already been generated
    while email in generated_emails:
        email = generate_random_username(full_name)
    generated_emails.add(email)  # Add the generated email to the set
    full_names.append(full_name)
    gmail_addresses.append(email)

# Print the generated full names and email addresses
for name, email in zip(full_names, gmail_addresses):
    print(name)
    print(email.lower())