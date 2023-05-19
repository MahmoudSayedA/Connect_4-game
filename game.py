from board import Board
import time
import math
import random
import copy

# GAME LINK
# http://kevinshannon.com/connect4/

rows = 6
cols = 7

EMPTY = 0
AI = 1 #R
COMPUTER = 2 #B

def getValidMoves (state):
    result =[]
    for i in range(cols):
        if state[0][i] == EMPTY:
            result.append(i)
    return result 

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

def isLeaf(state):
    return isWinner(state,AI) or isWinner(state, COMPUTER) or (len(getValidMoves(state)) ==0)

def get_opponent(player):
    if(player ==AI):
        return COMPUTER
    else:
        return AI

def evalFunction(board, player):
    score = 0
    
    # Check horizontal sequences of length 4
    for row in range(6):
        for col in range(4):
            seq = board[row][col:col+4]
            if seq.count(player) == 4:
                score += 10000
            elif seq.count(player) == 3 and seq.count(EMPTY) == 1:
                score += 100
            elif seq.count(player) == 2 and seq.count(EMPTY) == 2:
                score += 10
            elif seq.count(player) == 1 and seq.count(EMPTY) == 3:
                score += 1
            elif seq.count(get_opponent(player)) == 3 and seq.count(EMPTY) == 1:
                score -= 100
            elif seq.count(get_opponent(player)) == 2 and seq.count(EMPTY) == 2:
                score -= 10
            elif seq.count(get_opponent(player)) == 1 and seq.count(EMPTY) == 3:
                score -= 1
    
    # Check vertical sequences of length 4
    for row in range(3):
        for col in range(7):
            seq = [board[row+i][col] for i in range(4)]
            if seq.count(player) == 4:
                score += 10000
            elif seq.count(player) == 3 and seq.count(EMPTY) == 1:
                score += 100
            elif seq.count(player) == 2 and seq.count(EMPTY) == 2:
                score += 10
            elif seq.count(player) == 1 and seq.count(EMPTY) == 3:
                score += 1
            elif seq.count(get_opponent(player)) == 3 and seq.count(EMPTY) == 1:
                score -= 100
            elif seq.count(get_opponent(player)) == 2 and seq.count(EMPTY) == 2:
                score -= 10
            elif seq.count(get_opponent(player)) == 1 and seq.count(EMPTY) == 3:
                score -= 1
                
    # Check diagonal sequences of length 4 (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            seq = [board[row+i][col+i] for i in range(4)]
            if seq.count(player) == 4:
                score += 10000
            elif seq.count(player) == 3 and seq.count(EMPTY) == 1:
                score += 100
            elif seq.count(player) == 2 and seq.count(EMPTY) == 2:
                score += 10
            elif seq.count(player) == 1 and seq.count(EMPTY) == 3:
                score += 1
            elif seq.count(get_opponent(player)) == 3 and seq.count(EMPTY) == 1:
                score -= 100
            elif seq.count(get_opponent(player)) == 2 and seq.count(EMPTY) == 2:
                score -= 10
            elif seq.count(get_opponent(player)) == 1 and seq.count(EMPTY) == 3:
                score -= 1
    
    # Check diagonal sequences of length 4 (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            seq = [board[row-i][col+i] for i in range(4)]
            if seq.count(player) == 4:
                score += 10000
            elif seq.count(player) == 3 and seq.count(EMPTY) == 1:
                score += 100
            elif seq.count(player) == 2 and seq.count(EMPTY) == 2:
                score += 10
            elif seq.count(player) == 1 and seq.count(EMPTY) == 3:
                score += 1
            elif seq.count(get_opponent(player)) == 3 and seq.count(EMPTY) == 1:
                score -= 100
            elif seq.count(get_opponent(player)) == 2 and seq.count(EMPTY) == 2:
                score -= 10
            elif seq.count(get_opponent(player)) == 1 and seq.count(EMPTY) == 3:
                score -= 1
    
    return score

def play (state, column,player):
    flag = False
    for r in range(rows):
        if(state [r][column]!= EMPTY):
            state [r-1][column] = player
            flag = True
            break
    if(not flag):
        state[rows - 1][column] = player

def minimax (state, player, depth, alpha , beta):
    valid_moves =getValidMoves(state) #get list of columns numbers which can play in  
    if(isLeaf(state)): #base case
        if(isWinner(state , AI)):
            return None , 10000
        elif(isWinner(state,COMPUTER)):
            return None , -10000
        else:
            return None , 0   #game over no empty places
        
    elif (depth ==0): #base case
        return None , evalFunction(state , AI)
    
    if(player == AI): #recursive call mamimize player
        score = math.inf*-1
        toPlay = random.choice(valid_moves)
        for column in valid_moves:
            nextState = copy.deepcopy(state)
            # nextState = state.copy()
            play(nextState,column,player)
            newScore = minimax(nextState,COMPUTER,depth-1,alpha,beta)[1]
            if newScore > score:
                score = newScore
                toPlay = column
            alpha = max(alpha, score)
            if(alpha >= beta):
                break
        return toPlay , score
        
    if(player == COMPUTER):
        score = math.inf
        toPlay = random.choice(valid_moves)
        for column in valid_moves:
            nextState = copy.deepcopy(state)
            # nextState = state.copy()
            play(nextState,column,player)
            newScore=minimax(nextState,AI,depth-1,alpha,beta)[1]
            if newScore < score:
                score = newScore
                toPlay = column
            beta = min(beta,score) 
            if(alpha >= beta):
                break
        return toPlay , score    


def main():
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        
        # FOR DEBUG PURPOSES
        # board.print_grid(game_board)                 
        # YOUR CODE GOES HERE
        
        Gboard = copy.deepcopy(game_board)
        depth = 6
        random_column= minimax (Gboard, AI, depth, -math.inf ,math.inf)[0]
        print("c: ",random_column)
        
        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        #random_column = random.randint(0, 6)
        #random_column = 6
        
        # board.select_column(random_column)
        
        board.print_grid(game_board)
        print("000000000000000000000000000000000000000000000000000000000000000000000000000")  
        
        time.sleep(2)


if __name__ == "__main__":
    main()
