import random
import string


# Set to store generated numbers
generated_numbers = set()

# List of common First Names
first_names = [
    "Aaradhya", "Ananya", "Jiya", "Kavya", "Mahi", "Riya",
    "Shreya", "Aadhya", "Aanya", "Aarohi", "Aashi", "Anika",
    "Khushi", "Manvi", "Pari", "Roshni",  "Avni", "Gauri",
    "Sanvi", "Sara", "Siya", "Suhani", "Tanisha", "Trisha",
    "Amaira", "Arya", "Dhriti", "Isha", "Hansa",  "Aradhana",
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
]

def generate_random_mobile_number():
    
    global generated_numbers

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
    
    # If number is already generated, generate a new one recursively
    return generate_random_mobile_number()

# Generate random Indian names and corresponding email addresses
def generate_random_female_data():
    first_name = random.choice(first_names)
    # Select a single surname based on the probabilities
    surname = random.choices(*zip(*last_names))[0]
    full_name = first_name + " " + surname
    email = generate_random_username(full_name)
    return full_name, email.lower()  # Convert email address to lowercase

def generate_random_username(name):
    random_digit = random.choice([3, 4, 5])  # Randomly select digit to generate 3, 4, or 5 numbers
    random_number = ''.join(random.choices(string.digits, k=random_digit))  # Generate random numbers of digits
    
    # Probabilities for choosing whether to concatenate surname before first name or first name before surname
    probabilities = [0.65, 0.45]
    
    # Choose whether to concatenate surname before first name or first name before surname
    email_format = random.choices(['surname_first', 'first_surname'], weights=probabilities)[0]

    if email_format == 'surname_first':
        # Concatenate the surname before the first name
        email_name = name.split()[1] + name.split()[0]
    else:
        # Concatenate the first name before the surname
        email_name = name.split()[0] + name.split()[1]

    email_address_list = ['@gmail.com', '@outlook.com', '@yahoo.com']
    probabilities = [0.91, 0.05, 0.04]  # Probabilities for choosing email domains

    # Choose email domain based on probabilities
    email_domain = random.choices(email_address_list, weights=probabilities)[0]

    # Concatenate the email name with the random number and append the selected email domain
    return email_name + random_number + email_domain



def main():
    
    print("----------------------------------------------------------------------------")
    counter = 1

    while counter <= 10:
        fullName, emailAddress = generate_random_female_data()
        mobile_numbers = generate_random_mobile_number()
        print(fullName, emailAddress, mobile_numbers)
        counter += 1

main()
