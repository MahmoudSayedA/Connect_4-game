from board import Board
import time
import random

# GAME LINK
# http://kevinshannon.com/connect4/


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
