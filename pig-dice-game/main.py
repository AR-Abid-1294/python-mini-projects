from random import randint


def showScore(turn_points, scores):
    print(f"\nYou scored {turn_points} this turn.")
    print(f"Current scores:")
    for player, score in scores.items():
        print(f"Player {player}: {score}")


def play(player_no, scores, winning_score=50):
    print(f"\nPlayer {player_no}'s turn")

    turn_points = 0
    prev_point = None

    while True:
        # --------------
        # Roll the dice
        # --------------
        point = randint(1, 6)
        print(f"You rolled a {point}.")

        # --------------------
        # Rule 1: Rolling a 1
        # --------------------
        if point == 1:
            print("1 means you lose all the points you scored this turn.")
            turn_points = 0
            showScore(turn_points, scores)
            return False        # game doesn't end

        # ------------------
        # Accumulate points
        # ------------------
        turn_points += point

        # -----------------------------------
        # Rule 2: Roll two 6's consecutively
        # -----------------------------------
        if prev_point == 6 and point == 6:
            scores[player_no] = 0
            turn_points = 0
            print("You rolled two 6's consecutively. This resets your score to 0!")
            prev_point = None
            continue

        # ------------------------
        # Check winning condition
        # ------------------------            
        if scores[player_no] + turn_points >= winning_score:
            scores[player_no] += turn_points
            showScore(turn_points, scores)
            print(f"Player {player_no} wins!")
            return True         # game ends

        # -------------------------------------
        # Player decision to roll again or not
        # -------------------------------------
        choice = input("Roll again? (y/n): ").lower()
        if choice == "n":
            scores[player_no] += turn_points
            showScore(turn_points, scores)
            return False        # game doesn't end
        
        # -------------------------------------
        # Update previous point after decision
        # -------------------------------------
        prev_point = point

players_no = int(input("How many players? "))
scores = {i+1: 0 for i in range(players_no)}
win_score = int(input("How much score to win? "))

game_end = False

while not game_end:
    for i in range(players_no):
        game_end = play(i+1, scores, win_score)
        if game_end:
            break
