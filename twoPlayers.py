#Two player
# player 1 - x, player 2 - o

#function to update result string
def get_result(result,move,player) :
    
    if player == 1:
        char = 'x'

    else:
        char = 'o'
        
    if move == 1:
        result = result[0:17] + char + result[18:]

    if move == 2:
        result = result[0:23] + char + result[24:]

    if move == 3:
        result = result[0:29] + char + result[30:]

    if move == 4:
        result = result[0:65] + char + result[66:]

    if move == 5:
        result = result[0:71] + char + result[72:]

    if move == 6:
        result = result[0:77] + char + result[78:]

    if move == 7:
        result = result[0:113] + char + result[114:]

    if move == 8:
        result = result[0:119] + char + result[120:]

    if move == 9:
        result = result[0:125] + char + result[126:]

    return result

#function to update filling string
def update_filling(result,move) :
    
    char = ' '
        
    if move == 1:
        result = result[0:17] + char + result[18:]

    if move == 2:
        result = result[0:23] + char + result[24:]

    if move == 3:
        result = result[0:29] + char + result[30:]

    if move == 4:
        result = result[0:65] + char + result[66:]

    if move == 5:
        result = result[0:71] + char + result[72:]

    if move == 6:
        result = result[0:77] + char + result[78:]

    if move == 7:
        result = result[0:113] + char + result[114:]

    if move == 8:
        result = result[0:119] + char + result[120:]

    if move == 9:
        result = result[0:125] + char + result[126:]

    return result

#function to update score matrix
def update_score(score,move,player):

    x = int((move-1)/3)
    y = int((move-1)%3)

    score[x][y] = player

    return score;

#function to check player is winning or not
def isWinning(score,player):
    
    #it checks for horizontal sequence, vertical sequence and diagonal sequence
    for i in range(3) :
        for j in range(3) :
            if score[i][j] == player:

                if i+2 < 3 :
                    if score[i+1][j] == player and score[i+2][j] == player:
                        return True

                if j+2 < 3 :
                    if score[i][j+1] == player and score[i][j+2] == player:
                        return True

                if i+2 < 3 and j+2 < 3:
                    if score[i+1][j+1] == player and score[i+2][j+2] == player:
                        return True

                if i+2 < 3 and j-2 >= 0:
                    if score[i+1][j-1] == player and score[i+2][j-2] == player:
                        return True
    return False

#function to check illegal move
def isIllegal(score,move):

    #if move is out of grid numbers
    if move < 1 or move > 9:
        return True
    
    x = int((move-1)/3)
    y = int((move-1)%3)

    #if that block is empty
    if score[x][y] == 0 :
        return False
    
    return True

#Driver code
s = "   |       |   \n   |       |   \n___|_______|___\n   |       |   \n   |       |   \n___|_______|___\n   |       |   \n   |       |   \n   |       |   "   #string for grid
filling =  "   |       |   \n 1 |   2   | 3 \n___|_______|___\n   |       |   \n 4 |   5   | 6 \n___|_______|___\n   |       |   \n 7 |   8   | 9 \n   |       |   "  #string for numbering
result = s;
score = [[0,0,0],[0,0,0],[0,0,0]] #score matrix
i = 0

while i < 9:

    #Show current grid and numbering
    print()
    print(filling)
    print()
    print(result)
    print()

    #if player1's turn
    if i % 2 == 0 :
        move = int(input("Player 1, x "))   #take input

        #illegal move
        if isIllegal(score,move) :
            print("Illegal move, try again")

        else :
            result = get_result(result,move,1)  #update resutl string
            score = update_score(score,move,1)  #update score matrix
            filling = update_filling(filling,move); #update filling string(shows possible moves on grid)
        
            #if player1 is winning
            if isWinning(score,1):
                print("Player 1 won the game")
                print()
                print(result)
                break
            i+=1

    #player2's turn
    else :
        move = int(input("Player 2, 0 "))

        #illegal move
        if isIllegal(score,move) :
            print("Illegal move, try again")

        else :
            result = get_result(result,move,2)  #update result string
            score = update_score(score,move,2)  #update score matrix
            filling = update_filling(filling,move); #update filling string
        
            #if player2 is winning
            if isWinning(score,2):
                print("Player 2 won the game")
                print()
                print(result)
                break
            i+=1


#draw
if i == 9 :
    print(result)
    print("Draw")