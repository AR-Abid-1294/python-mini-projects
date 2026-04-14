def drawBoard(playerO, playerX):
    for i in range(7):
        if i%2 == 0:
            print("---+"*2 + "---")
        else:
            j = 1
            while(j <= 3):
                cell = ((i+1)/2, j)
                if cell in playerO:
                    print(" O ", end="")
                elif cell in playerX:
                    print(" X ", end="")
                else:
                    print("   ", end="")
                if j == 1 or j == 2:
                    print("|", end="")
                j += 1
            print()



def isWin(playerLst):
    pass

playerO = list()
playerX = list()

drawBoard(playerO, playerX)

while True:

    print("Player O's turn")
    rowO = int(input("Enter row (1-3): "))
    colO = int(input("Enter column (1-3): "))
    playerO.append((rowO, colO))

    drawBoard(playerO, playerX)

    if isWin(playerO):
        winner = "O"
        break
    elif isWin(playerX):
        winner = "X"
        break

    print("Player X's turn")
    rowX = int(input("Enter row (1-3): "))
    colX = int(input("Enter column (1-3): "))
    playerX.append((rowX, colX))

    drawBoard(playerO, playerX)

    if isWin(playerO):
        winner = "O"
        break
    elif isWin(playerX):
        winner = "X"
        break
            
            



print(f"Player {winner} is the winner.")


