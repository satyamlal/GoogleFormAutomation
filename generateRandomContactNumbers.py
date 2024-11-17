import random

'''This Program generates 1000 random numbers and store it into a csv file'''

# def generate_random_mobile_number():
#     # Generate 10 random digits
#     random_digits = ''.join([str(random.randint(6, 9)) for _ in range(10)])
#     # Concatenate '+91' with the random digits
#     return '+91 ' + random_digits

# # Generate 1000 random Indian mobile numbers
# indian_mobile_numbers = [generate_random_mobile_number() for _ in range(1000)]

# # Write the generated mobile numbers to a CSV file
# with open('randomContactNumbers.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     # Write the header
#     writer.writerow(['Mobile Number'])
#     # Write the mobile numbers
#     for number in indian_mobile_numbers:
#         writer.writerow([number])


'''This script generate random numbers each time function is called and cross checks if the number already exists before return the number'''

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

# Example usage:
number1 = generate_random_mobile_number()
print("First number:", number1)

# Call the function again to generate another number
number2 = generate_random_mobile_number()
print("Second number:", number2)
