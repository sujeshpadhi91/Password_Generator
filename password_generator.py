import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    # print(letters, digits, special)

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_character = random.choice(characters)
        password += new_character

        if new_character in digits:
            has_number = True
        elif new_character in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password

minimum_password_length = int(input("What should be the minimum length of the password? "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == 'y'
has_special = input("Do you want to have special characters (y/n)? ").lower() == 'y'
password = generate_password(minimum_password_length, has_number, has_special)
print("The new password is below\n"+password+"\n")