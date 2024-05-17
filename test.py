import random

def main():
    designation = ['Developer', 'Software Engineer', 'Data Scientist', 'Data Engineer', 'DevOps Engineer']
    probabilities = [0.7, 0.5, 0.45, 0.30, 0.21]
    print(random.choices(designation, weights=probabilities)[0]) # Team Designation selected randomly

main()
