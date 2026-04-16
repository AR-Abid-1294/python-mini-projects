special_chars = set('!@#$%^&*()_-+={[}]|\\:;"\'<,>.?/')
passStrength = {0: 'Empty',
                1: 'Very Weak',
                2: 'Weak',
                3: 'Medium',
                4: 'Strong',
                5: 'Very Strong'}


password = input("Enter a password: ")

length = len(password)
print(f"The password has {length} characters.")
passLen = length >= 8

upperCase = any(char.isupper() for char in password)

lowerCase = any(char.islower() for char in password)

specialChar = any(char in special_chars for char in password)

number = any(char.isdigit() for char in password)

strength = sum([passLen, upperCase, lowerCase, specialChar, number])

print(f"Your password is {passStrength[strength]}.")

# messages
if strength < len(passStrength) - 1:
    print("Suggestions:")

    if not passLen: print("Use 8 characters or more.")

    if not (upperCase or lowerCase): print("Add some uppercase and lowercase letters.")
    elif not upperCase:              print("Add some uppercase letters.")
    elif not lowerCase:              print("Add some lowercase letters.")

    if not specialChar: print("Add some special characters.")
    if not number:      print("Add some numbers.")