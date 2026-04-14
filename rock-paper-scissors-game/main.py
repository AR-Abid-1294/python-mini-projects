from random import choice

def rockPaperScissors():
    options = ['Rock 🪨', 'Paper 📄', 'Scissors ✂️']
    win_lose = [('Rock 🪨', 'Scissors ✂️'),
                ('Scissors ✂️', 'Paper 📄'),
                ('Paper 📄', 'Rock 🪨')]

    computer = choice(options)
    user_choice = input("Your Choice: ")
    for option in options:
        if user_choice[0].upper() == option[0]:
            user = option
            break
    else:
        return "quit"

    print(f"Computer's choice: {computer}")
    print(f"Your choice: {user}")

    if user == computer:
        print("Tie")
        return 0
    elif (user, computer) in win_lose:
        print("You win!")
        return 1
    else:
        print("Computer wins.")
        return -1


tie = 0
win = 0
lose = 0

while True:
    score = rockPaperScissors()

    if score == 0: tie += 1
    elif score == 1: win += 1
    elif score == -1: lose += 1
    elif score == "quit":
        print(f"Your Score: {win}")
        print(f"Computer's Score: {lose}")
        print(f"Tie: {tie} times")
        break