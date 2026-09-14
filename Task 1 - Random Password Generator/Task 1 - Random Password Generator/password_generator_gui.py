import random
import string

while True:

    length = int(input("Enter password length: "))

    if length < 8:
        print("Password length must be at least 8 characters.")
        continue

    uppercase = input("Include uppercase letters? (y/n): ").lower()
    lowercase = input("Include lowercase letters? (y/n): ").lower()
    numbers = input("Include numbers? (y/n): ").lower()
    symbols = input("Include symbols? (y/n): ").lower()

    if uppercase not in ("y", "n") or lowercase not in ("y", "n") or numbers not in ("y", "n") or symbols not in ("y", "n"):
        print("Please enter only y or n.")
        continue

    selected_types = 0

    if uppercase == "y":
        selected_types += 1
    if lowercase == "y":
        selected_types += 1
    if numbers == "y":
        selected_types += 1
    if symbols == "y":
        selected_types += 1

    if selected_types < 2:
        print("Please select at least 2 character types.")
        continue

    characters = ""

    if uppercase == "y":
        characters += string.ascii_uppercase
    if lowercase == "y":
        characters += string.ascii_lowercase
    if numbers == "y":
        characters += string.digits
    if symbols == "y":
        characters += string.punctuation

    password = ""

    if uppercase == "y":
        password += random.choice(string.ascii_uppercase)
    if lowercase == "y":
        password += random.choice(string.ascii_lowercase)
    if numbers == "y":
        password += random.choice(string.digits)
    if symbols == "y":
        password += random.choice(string.punctuation)

    while len(password) < length:
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    print("Generated Password:", password)

    again = input("Generate another password (y/n): ")

    if again != "y":
        print("Thank you for using the Password Generator!")
        break
