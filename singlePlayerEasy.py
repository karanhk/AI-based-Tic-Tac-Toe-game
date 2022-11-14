# player 1 - x, computer - o
#Single player - Easy

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

#function to check player or computer is winning or not
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

#function to find best move
def findBestMove(score) :

    #it finds move where computer wins
    for i in range(3):
        for j in range(3):
            if score[i][j] == 0 :
                score[i][j] = 2
                move = 3*i + (j%3) + 1

                if isWinning(score,2) :
                    return move
                score[i][j] = 0

    #it finds move where opponent wins, it places o there so that opponent doesn't win
    for i in range(3):
        for j in range(3):
            if score[i][j] == 0 :
                score[i][j] = 1
                move = 3*i + (j%3) + 1

                if isWinning(score,1) :
                    return move
                score[i][j] = 0
                

    #center position
    if score[1][1] == 0 :
        return 5

    if score[0][0] == 0 :
        return 1

    if score[0][2] == 0 :
        return 3
    
    if score[2][0] == 0 :
        return 7

    if score[2][2] == 0 :
        return 9

    for i in range(3):
        for j in range(3):
            if score[i][j] == 0 :
                move = 3*i + (j%3) + 1
                return move

#driver code
s = "   |       |   \n   |       |   \n___|_______|___\n   |       |   \n   |       |   \n___|_______|___\n   |       |   \n   |       |   \n   |       |   "   #string for grid
filling =  "   |       |   \n 1 |   2   | 3 \n___|_______|___\n   |       |   \n 4 |   5   | 6 \n___|_______|___\n   |       |   \n 7 |   8   | 9 \n   |       |   "  #string for numbering
result = s;
score = [[0,0,0],[0,0,0],[0,0,0]]  #score matrix
i = 0

while i < 9:

    #player's turn
    if i % 2 == 0 :

        #shows current grid and possible moves
        print()
        print(filling)
        print()
        print(result)

        print()


        move = int(input("Your turn , x "))

        #illegal move
        if isIllegal(score,move) :
            print("Illegal move, try again")

        else :
            result = get_result(result,move,1)  #update result string
            score = update_score(score,move,1)  #update score matrix
            filling = update_filling(filling,move); #update filling string(shows possible moves on grid)
        
            #if player is winning
            if isWinning(score,1):
                print("Congrulations, you won the game")
                print()
                print(result)
                print(score)
                break
            i+=1

    #computer's turn
    else :
        
        move = findBestMove(score)

        result = get_result(result,move,2)
        score = update_score(score,move,2)
        filling = update_filling(filling,move);
        
        if isWinning(score,2):
            print("Computer won the game")
            print()
            print(result)
            print(score)
            break
        i+=1


#draw
if i == 9 :
    print(result)
    print("Draw")