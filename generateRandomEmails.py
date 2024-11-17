import random
import string

# List of common First Names
first_names = [
    "Aaradhya", "Ananya", "Jiya", "Kavya", "Mahi", "Riya",
    "Shreya", "Aadhya", "Aanya", "Aarohi", "Aashi", "Anika",
    "Khushi", "Manvi", "Pari", "Roshni",  "Avni", "Gauri",
    "Sanvi", "Sara", "Siya", "Suhani", "Tanisha", "Trisha",
    "Amaira", "Arya", "Dhriti", "Isha", "Hansa",  "Aradhana",
    "Kashvi", "Kiara", "Kriti", "Mahira", "Nehal", "Pihu",
    "Ridhi", "Riva", "Ruchi", "Shruti", "Sneha", "Tanvi",
    "Vaani", "Vanya", "Akshara", "Anvi", "Aria", "Lakshita",
    "Ankita", "Bhavya", "Chahat", "Divya", "Devika", "Shivani",
    "Kiran", "Naina", "Navya", "Mehek",  "Tanya",
    "Nikita", "Poonam", "Palak", "Radhika", "Sonia",
    "Urvi", "Vaishnavi", "Vanshika", "Yashika", "Aarushi",
    "Amaya", "Aparna", "Dia", "Ishaani", "Nupur", "Nandita",
    "Jhanvi", "Kanak", "Mansi", "Neha", "Saniya",
    "Priya", "Priti", "Ritika", "Saumya", "Nimisha",
    "Shanaya", "Tara", "Urvashi", "Vidhi", "Yashvi",
    "Anushree", "Bhavika", "Chitra", "Drishti", "Ishita",
    "Ishika", "Lavanya", "Mehak", "Niharika", "Bhawna",
    "Nisha", "Rachana", "Rashi", "Ruchika", "Sanya",
    "Saanvi", "Shikha", "Vani", "Aditi", "Samaira", 
    "Aadya", "Anisha", "Apoorva", "Anvita", "Aradhya",
    "Charu", "Deeksha", "Ishani", "Juhi", "Komal", "Kritika",
    "Mahika", "Nandini", "Navika", "Prerna", "Priyanka",
    "Rishika", "Shivangi", "Sarika", "Tanushree", "Ria",
    "Yamini", "Anushka", "Arunima", "Bhavna", "Devanshi",
    "Ishwarya", "Jagrati", "Kanishka", "Mahima", "Mansi", 
    "Nitya", "Radha", "Reema", "Rhea", "Saisha", "Sakshi",
    "Aarohi", "Alisha", "Arushi", "Anshu",  "Minal", 
    "Aashi", "Anupriya", "Bhoomi", "Chhaya", "Deepti",
    "Jasmine", "Kashish", "Kashvi", "Kirti", "Lakshmi", 
    "Pari", "Pragya", "Pooja", "Ritika", "Ritvi", "Sanya", 
    "Sakshi", "Srishti", "Tanishka", "Vaishali", "Riddham",
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