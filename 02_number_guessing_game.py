from random import randint

def guessNumber(start, stop):
    num = randint(start, stop+1)
    attempts = 0
    guess = start - 1
    while guess != num:
        guess = int(input(f"Guess the number (between {start} and {stop}): "))
        attempts += 1
        
        if guess < num: print("Too low!", end=" ")
        if guess > num: print("Too high!", end=" ")
    
    print(f"Congrats! {num} it was.")
    print(f"You guessed the number in {attempts} attempts.")


start = int(input("Starting number for guessing game: "))
stop = int(input("Ending number for guessing game: "))

guessNumber(start, stop)