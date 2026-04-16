import random

def genNum(length=4):
    if length < 1 or length > 10:
        return None
    
    digits = list(range(10))
    first_digit = random.choice(range(1, 10))
    digits.remove(first_digit)
    rest_digits = random.sample(digits, length-1)
    return str(first_digit) + "".join(str(d) for d in rest_digits)

while True:
    number_length = int(input("Enter the length of the number: "))
    number = genNum(number_length)
    if number != None:
        break

print(f"I have generated a {number_length}-digit number with unique digits.")
print("Try to guess it!")

attempts = 0

while True:
    guess = input("Guess: ")
    cows = 0
    bulls = 0

    if len(guess) != number_length:
        print(f"The number has {number_length} digit(s).")
        continue

    for i in range(number_length):
        if guess[i] == number[i]:
            bulls += 1
        elif guess[i] in number:
            cows += 1

    attempts += 1
    print(f"{cows} cows, {bulls} bulls")

    if bulls == number_length:
        print("You guessed the number right!")
        print("Attempts:", attempts)
        break

    

