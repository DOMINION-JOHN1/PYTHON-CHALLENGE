import random
import string
# Generating characters for the passwords
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
special_characters = string.punctuation
numbers = string.digits


def generate_password(length):
    # Ensure the password length is at least 1
    length = max(length, 1)
    # Ensure the password starts with an uppercase letter
    password = random.choice(uppercase_letters)
    # Fill the remaining length with a mix of characters
    remaining_length = length-1
    password += random.choice(lowercase_letters)
    password += random.choice(special_characters)
    password += random.choice(numbers)
    password += ''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(remaining_length-3))
    # Shuffle the password to randomize the characters
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password


while True:
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please do input a valid value (an integer)")
        continue
    if length < 4:
        print("input a number from greater than than three")
        break
    else:
        # Generate and print the password
        password = generate_password(length)
        print("Generated password:", password)
        break
