import random
import string
import csv

# List of common First Names
first_names = [
    "Aaradhya", "Ananya", "Isha", "Jiya", "Kavya", "Mahi", "Riya",
    "Shreya", "Aadhya", "Aanya", "Aarohi", "Aashi", "Anika", "Avni", "Gauri",
    "Ishita", "Janvi", "Khushi", "Manvi", "Mehak", "Myra", "Navya", "Pari", "Roshni",
    "Sanvi", "Sara", "Siya", "Suhani", "Tanisha", "Trisha", "Vani", "Vanya", "Anahita", "Aradhana",
    "Ariana", "Aarushi", "Amaira", "Arya", "Dhriti", "Esha", "Hansa",
    "Jhanvi", "Kashvi", "Kiara", "Kriti", "Mahira", "Nandini", "Nehal", "Nyra", "Pihu",
    "Ridhi", "Riva", "Ruchi", "Saanvi", "Samaira", "Shruti", "Sneha", "Tanvi", "Tanya", "Trisha",
    "Vaani", "Vanya", "Vedika", "Aadhira", "Aarna", "Aashi", "Akshara", "Anvi", "Aria",
    "Ankita", "Bhavya", "Chahat", "Divya", "Devika",
    "Kiran", "Lakshmi", "Lavanya", "Mansi", "Naina", "Navya",
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
    "Yamini", "Zara", "Anshika", "Anushka", "Arunima", "Bhavna", "Devanshi", "Gargee",
    "Ishwarya", "Ishika", "Jagrati", "Kanishka", "Lavanya", "Mahima", "Manya",
    "Nitya", "Parnika", "Radha", "Reema", "Rhea", "Saisha", "Sakshi", "Sanya",
    "Shalini", "Tanya", "Urvashi", "Yashika", "Zoya", "Anika",
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


'''This Program generates 1000 random names and corresponding email address and stores it into a csv file'''

# # Maintain a set to store generated email addresses
# generated_emails = set()

# def generate_random_username(name):
#     randomDigit = [3, 4, 5]
#     randomSelection = random.choice(randomDigit) # Randomly select digit to generate 3 or 4 or 5 numbers
#     random_number = ''.join(random.choices(string.digits, k=randomSelection)) # Random numbers of digit is generated and added at the end of the email
#     email_Addres_List = ['@gmail.com', '@outlook.com', '@yahoo.com']
#     # Concatenate the full name with the random number and append "@gmail.com"
#     return name.replace(" ", "") + random_number + random.choice(email_Addres_List)

# # Generate random Indian names and corresponding email addresses
# full_names = []
# gmail_addresses = []
# for _ in range(1000):
#     first_name = random.choice(first_names)
#     # Select a single surname based on the probabilities
#     surname = random.choices(*zip(*last_names))[0]
#     full_name = first_name + " " + surname
#     email = generate_random_username(full_name)
#     # Check if the email has already been generated
#     while email in generated_emails:
#         email = generate_random_username(full_name)
#     generated_emails.add(email)  # Add the generated email to the set
#     full_names.append(full_name)
#     gmail_addresses.append(email)

# # Write the generated full names to a CSV file
# with open('full_names.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Full Name'])
#     for name in full_names:
#         writer.writerow([name])

# # Write the generated email addresses to a CSV file
# with open('email_addresses.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Email Address'])
#     for email in gmail_addresses:
#         writer.writerow([email.lower()])



'''This script generate random name with corresponding email each time without repetition'''

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

# Example usage:
fullName, emailAddress = generate_random_female_data()
print("Full Name:", fullName)
print("Email Address:", emailAddress)