from board import Board
import time
import random

# GAME LINK
# http://kevinshannon.com/connect4/

def getValidMoves (state):
    result =[]
    for i in range(cols):
        if state[0][i] == EMPTY:
            result.append(i)
    return result 

def play (state, column,player):
    flag = False
    for r in range(rows):
        if(state [r][column]!= EMPTY):
            state [r-1][column] = player
            flag = True
            break
    if(not flag):
        state[rows - 1][column] = player
        
def isWinner(GameBoard,player): 
    for j in range(cols-3):#horizontal
        for i in range (rows):
            if GameBoard[i][j]== player and GameBoard[i][j+1]== player and GameBoard[i][j+2]==player and GameBoard[i][j+3]==player:
                return True
    for j in range(cols): #vertical
        for i in range (rows-3): 
            if GameBoard[i][j]== player and GameBoard[i+1][j]== player and GameBoard[i+2][j]==player and GameBoard[i+3][j]==player:
                return True
            
    for j in range(cols-3): #top left
        for i in range (rows-3): 
            if GameBoard[i][j]== player and GameBoard[i+1][j+1]== player and GameBoard[i+2][j+2]==player and GameBoard[i+3][j+3]==player:
                return True
            
    for j in range(cols-3):  #top right
        for i in range (3,rows):
            if GameBoard[i][j]== player and GameBoard[i-1][j+1]== player and GameBoard[i-2][j+2]==player and GameBoard[i-3][j+3]==player:
                return True 

def willWin(GameBoard,player):
    for j in range(cols-2):#horizontal
        for i in range (rows):
            if GameBoard[i][j]== player and GameBoard[i][j+1]== player and GameBoard[i][j+2]==player:
                return -100
            
    for j in range(cols): #vertical
        for i in range (rows-2): 
            if GameBoard[i][j]== player and GameBoard[i+1][j]== player and GameBoard[i+2][j]==player:
                return -500
            
    for j in range(cols-2): #top left
        for i in range (rows-2): 
            if GameBoard[i][j]== player and GameBoard[i+1][j+1]== player and GameBoard[i+2][j+2]==player:
                return -500
            
    for j in range(cols-2):  #top right
        for i in range (2,rows):
            if GameBoard[i][j]== player and GameBoard[i-1][j+1]== player and GameBoard[i-2][j+2]==player :
                return -500
    return 0  

def evalFunction(state, player):
    inRows =[0]*rows
    inCols = [0]*cols
    inDiag =[0]*2
    for i in range(rows):
        for j in range (cols):
            if state[i][j] ==player :
                inRows[i] +=1
                inCols[j]+=1
                if (i == j):
                    inDiag[0] +=1
                elif ((i+j)==6):
                    inDiag[1]+=1 
    score =0
    for x in range(rows):
        if(inRows[x] == 4):
            score += 100
        elif(inRows[x]==3):
            score += 30 
        else:
            score += inRows[x]      

    for x in range(cols):
        if (x ==3):
            score += 80
        elif(inCols[x]==4):
            score += 100
        elif(inCols[x]==3):
            score += 30 
        else:
            score += inCols[x]   

    for x in range(2):
        if(inDiag[x]==4):
            score += 100
        elif(inDiag[x]==3):
            score += 30 
        else:
            score += inDiag[x]
    if player == AI:
        score + willWin(state,COMPUTER)
    else:
        score + willWin(state,AI)
    return score 

def main():
    board = Board()

    time.sleep(5)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        # YOUR CODE GOES HERE

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        # random_column = random.randint(0, 6)
        var = 3
        board.select_column(var)

        time.sleep(2)


if __name__ == "__main__":
    main()
