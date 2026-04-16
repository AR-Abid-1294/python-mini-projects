import random

word_list = [
    "apple", "banana", "orange", "grape", "mango", "peach", "pear", "cherry",
    "strawberry", "blueberry", "watermelon", "pineapple", "coconut", "papaya",
    "computer", "keyboard", "mouse", "monitor", "laptop", "python", "program",
    "code", "variable", "function", "loop", "string", "integer", "boolean",
    "planet", "galaxy", "universe", "rocket", "satellite", "asteroid",
    "tiger", "lion", "elephant", "giraffe", "zebra", "monkey", "rabbit",
    "school", "teacher", "student", "pencil", "notebook", "library",
    "bottle", "window", "chair", "table", "garden", "bridge"
]

secret_word = random.choice(word_list).lower()
guessed_letters = set()
attempts = 0

print("_"*len(secret_word))

while True:
    guess = input("\nEnter a letter: ").lower()
    attempts += 1

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter.")
        continue

    if guess in guessed_letters:
        print("Already guessed that letter")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Good guess")
    else:
        print("Wrong guess")

    display = ""

    for char in secret_word:
        if char in guessed_letters:
            display += char
        else:
            display += "_"

    print(display)

    if display == secret_word:
        print("Word guessed correctly!")
        print("Attempts taken:", attempts)
        break