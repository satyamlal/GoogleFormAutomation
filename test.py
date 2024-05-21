import random
import string

# List of common First Names
first_names = [
    "Aaradhya", "Ananya", "Jiya", "Kavya", "Mahi", "Riya",
    "Shreya", "Aadhya", "Aanya", "Aarohi", "Aashi", "Anika",
    "Khushi", "Manvi", "Pari", "Roshni",  "Avni", "Gauri",
]

# List of common North Indian surnames with corresponding probabilities
last_names = [
    ("Sharma", 25), 
    ("Verma", 20), 
    ("Jha", 20),
    ("Singh", 15)
]

# Generate random Indian names and corresponding email addresses
def generate_random_female_data():
    first_name = random.choice(first_names)
    surname = random.choices(*zip(*last_names))[0]
    full_name = first_name + " " + surname
    email = generate_random_username(first_name, surname)
    return full_name, email.lower()  # Convert email address to lowercase

def generate_random_username(first_name, surname):
    random_digit = random.choice([3, 4, 5])  # Randomly select digit to generate 3, 4, or 5 numbers
    random_number = ''.join(random.choices(string.digits, k=random_digit))  # Generate random numbers of digits
    
    # Choose whether to use an underscore or a period or no space between the names
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

# Example usage
for _ in range(50):  # Generate 5 examples
    full_name, email = generate_random_female_data()
    print(f"Name: {full_name}, Email: {email}")
