from board import Board
import time
import random

# GAME LINK
# http://kevinshannon.com/connect4/

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
