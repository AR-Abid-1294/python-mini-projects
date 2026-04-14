from random import randint

def guessNumber(start, stop, max_attempt):

    with open("lowest_attempt.txt", "r") as file: min_attempt = int(file.read())

    num = randint(start, stop)
    attempts = 0
    guess = start - 1

    while guess != num:
        guess = int(input(f"Guess the number (between {start} and {stop}): "))
        attempts += 1
        
        if guess == num:
            print(f"Congrats! {num} it was.")
            print(f"You guessed the number in {attempts} attempts.")

        else:
            if guess < num: print("Too low!", end=" ")
            else:           print("Too high!", end=" ")

            if attempts < max_attempt:
                print("Try again.")
            else:
                print(f"\nMaximum Number of attempts ({attempts}) reached.")
                print(f"The number was {num}. You failed to guess it.")
                break

    if guess == num and attempts < min_attempt:
        min_attempt = attempts
        print("You've also unlocked new Lowest Attempt!")
        with open("lowest_attempt.txt", "w") as file:
            file.write(str(attempts))

    print(f"Lowest Attempts: {min_attempt}")



start = int(input("Starting number for guessing game: "))
stop = int(input("Ending number for guessing game: "))
max_attempt = int(input("How many attempts do you get? "))

guessNumber(start, stop, max_attempt)