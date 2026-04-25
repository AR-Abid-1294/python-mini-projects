import string
import random

def genPass(length=12, upperCase=True, number=True, specialChar=True):
    if length < (upperCase + number + specialChar):
        raise ValueError
    
    password = ""
    allowed_characters = string.ascii_lowercase

    if upperCase:
        password += random.choice(string.ascii_uppercase)
        allowed_characters += string.ascii_uppercase
    if number:
        password += random.choice(string.digits)
        allowed_characters += string.digits
    if specialChar:
        password += random.choice(string.punctuation)
        allowed_characters += string.punctuation

    # Fill the remaining length with any allowed character
    for _ in range(length - len(password)):
        password += random.choice(allowed_characters)

    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)




def main():
    length = int(input("Enter password length: "))
    upperCase = input("Include uppercase letters? (y/n): ") == "y"
    number = input("Include numbers? (y/n): ") == "y"
    specialChar = input("Include special characters? (y/n): ") == "y"

    password = genPass(length, upperCase, number, specialChar)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()