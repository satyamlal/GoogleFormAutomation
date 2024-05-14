import random

def generate_random_mobile_number():
    # Generate 10 random digits
    random_digits = ''.join([str(random.randint(6, 9)) for _ in range(10)])
    # Concatenate '+91' with the random digits
    return '+91' + " " + random_digits

# Generate 1000 random Indian mobile numbers
indian_mobile_numbers = [generate_random_mobile_number() for _ in range(1000)]

# Print the generated mobile numbers
for number in indian_mobile_numbers:
    print(number)
