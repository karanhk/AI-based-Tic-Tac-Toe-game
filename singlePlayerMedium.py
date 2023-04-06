# Python3 program to find the next optimal move for a player
player, opponent = 'o', 'x'
 
# This function returns true if there are moves
# remaining on the board. It returns false if
# there are no moves left to play.
def isMovesLeft(board) :
 
    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == '_') :
                return True
    return False
 
# This is the evaluation function as discussed
def evaluate(b) :
   
    # Checking for Rows for X or O victory.
    for row in range(3) :    
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :       
            if (b[row][0] == player) :
                return 10
            elif (b[row][0] == opponent) :
                return -10
 
    # Checking for Columns for X or O victory.
    for col in range(3) :
      
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
         
            if (b[0][col] == player) :
                return 10
            elif (b[0][col] == opponent) :
                return -10
 
    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
     
        if (b[0][0] == player) :
            return 10
        elif (b[0][0] == opponent) :
            return -10
 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
     
        if (b[0][2] == player) :
            return 10
        elif (b[0][2] == opponent) :
            return -10
 
    # Else if none of them have won then return 0
    return 0
 
# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, isMax) :
    score = evaluate(board)
 
    # If Maximizer has won the game return his/her
    # evaluated score
    if (score == 10) :
        return score
 
    # If Minimizer has won the game return his/her
    # evaluated score
    if (score == -10) :
        return score
 
    # If there are no more moves and no winner then
    # it is a tie
    if (isMovesLeft(board) == False) :
        return 0
 
    # If this maximizer's move
    if (isMax) :    
        best = -1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (board[i][j]=='_') :
                 
                    # Make the move
                    board[i][j] = player
 
                    # Call minimax recursively and choose
                    # the maximum value
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax) )
 
                    # Undo the move
                    board[i][j] = '_'
        return best
 
    # If this minimizer's move
    else :
        best = 1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (board[i][j] == '_') :
                 
                    # Make the move
                    board[i][j] = opponent
 
                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1, not isMax))
 
                    # Undo the move
                    board[i][j] = '_'
        return best
 
# This will return the best possible move for the player
def findBestMove(board) :
    bestVal = -1000
    bestMove = (-1, -1)
 
    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3) :    
        for j in range(3) :
         
            # Check if cell is empty
            if (board[i][j] == '_') :
             
                # Make the move
                board[i][j] = player
 
                # compute evaluation function for this
                # move.
                moveVal = minimax(board, 0, False)
 
                # Undo the move
                board[i][j] = '_'
 
                # If the value of the current move is
                # more than the best value, then update
                # best/
                if (moveVal > bestVal) :               
                    bestMove = (i, j)
                    bestVal = moveVal
                    
    return bestMove

def findBestMove1(board):
    bestMove = findBestMove(board)
    move = bestMove[0]*3 + bestMove[1]%3 + 1
    return move
# player 1 - x, player 2 - 0

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

def update_score(score,move,player):

    x = int((move-1)/3)
    y = int((move-1)%3)

    score[x][y] = player

    return score;

def isWinning(score,player):
    
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

def isIllegal(score,move):

    x = int((move-1)/3)
    y = int((move-1)%3)

    if score[x][y] == 0 :
        return False
    
    return True

def update_grid(grid,move,c):

    x = int((move-1)/3)
    y = int((move-1)%3)

    grid[x][y] = c
    return grid

s = "   |       |   \n   |       |   \n___|_______|___\n   |       |   \n   |       |   \n___|_______|___\n   |       |   \n   |       |   \n   |       |   "
filling =  "   |       |   \n 1 |   2   | 3 \n___|_______|___\n   |       |   \n 4 |   5   | 6 \n___|_______|___\n   |       |   \n 7 |   8   | 9 \n   |       |   "
result = s;
score = [[0,0,0],[0,0,0],[0,0,0]]
grid = [['_','_','_'],['_','_','_'],['_','_','_']]
i = 0

while i < 9:

    print()
    print(filling)
    print()
    print(result)
    print()

    if i % 2 == 0 :
        move = int(input("Your turn , x "))

        if isIllegal(score,move) :
            print("Illegal move, try again")

        else :
            result = get_result(result,move,1)
            score = update_score(score,move,1)
            filling = update_filling(filling,move)
            grid = update_grid(grid,move,'x')
        
            if isWinning(score,1):
                print("Congrulations, you won the game")
                print()
                print(result)
                print(score)
                break
            i+=1

    else :
        
        move = findBestMove1(grid)

        result = get_result(result,move,2)
        score = update_score(score,move,2)
        filling = update_filling(filling,move)
        grid = update_grid(grid,move,'o')
        
        if isWinning(score,2):
            print("I won the game")
            print()
            print(result)
            print(score)
            break
        i+=1



if i == 9 :
    print(result)
    print("Draw")