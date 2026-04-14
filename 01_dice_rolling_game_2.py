from random import randint

count = 0
while True:
    choice = input("Roll the dice? (y/n): ").lower()
    
    if choice == 'y':
        dice1 = randint(1, 7)
        dice2 = randint(1, 7)
        print(f"({dice1}, {dice2})")
        count += 1
    elif choice == 'n':
        print(f"Thanks for playing! You've played {count} times.")
        break
    else:
        print("Invalid Input")