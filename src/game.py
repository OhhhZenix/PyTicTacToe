import random
import time


def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[7] + "|" + board[6] + "|" + board[8])


def check_valid_move(board, position):
    return board[position] == " "


def make_move(board, player, position):
    board[position] = player


def player_make_move(board, player):
    position = int(input("Please enter a number from 1 to 9 to make a move! "))
    result = check_valid_move(board, position - 1)

    while not result:
        print_board(board)
        position = int(
            input(
                "Invalid move! please enter again a number from 1 to 9 to make a move! "
            )
        )
        result = check_valid_move(board, position - 1)

    make_move(board, player, position - 1)
    print_board(board)
    print("You make a move at position " + str(position))


def computer_make_move(board, player):
    position = random.randint(0, 8)
    while not check_valid_move(board, position):
        position = random.randint(0, 8)
    make_move(board, player, position)
    print_board(board)
    print("Computer made a move at position " + str(position + 1))


def is_board_full(board):
    position_left = 0
    for i in range(0, 9):
        if board[i] == " ":
            position_left += 1
    return position_left == 0


def check_winner(board, player, computer, score):
    x_win = 0
    o_win = 0
    game_over = False

    # Horizontal Checks for Player X
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        print("Player X wins!")
        x_win += 1
        game_over = True

    if board[3] == "x" and board[4] == "x" and board[5] == "x":
        print("Player X wins!")
        x_win += 1
        game_over = True

    if board[6] == "x" and board[7] == "x" and board[8] == "x":
        print("Player X wins!")
        x_win += 1
        game_over = True

    # Horizontal Checks for Player O
    if board[0] == "o" and board[1] == "o" and board[2] == "o":
        print("Player O wins!")
        o_win += 1
        game_over = True

    if board[3] == "o" and board[4] == "o" and board[5] == "o":
        print("Player O wins!")
        o_win += 1
        game_over = True

    if board[6] == "o" and board[7] == "o" and board[8] == "o":
        print("Player O wins!")
        o_win += 1
        game_over = True

    # Vertical Checks for Player X
    if board[0] == "x" and board[3] == "x" and board[6] == "x":
        print("Player X wins!")
        x_win += 1
        game_over = True

    if board[1] == "x" and board[4] == "x" and board[7] == "x":
        print("Player X wins!")
        x_win += 1
        game_over = True

    if board[2] == "x" and board[5] == "x" and board[8] == "x":
        print("Player X wins!")
        x_win += 1
        game_over = True

    # Vertical Checks for Player O
    if board[0] == "o" and board[3] == "o" and board[6] == "o":
        print("Player O wins!")
        o_win += 1
        game_over = True

    if board[1] == "o" and board[4] == "o" and board[7] == "o":
        print("Player O wins!")
        o_win += 1
        game_over = True

    if board[2] == "o" and board[5] == "o" and board[8] == "o":
        print("Player O wins!")
        o_win += 1
        game_over = True

    # Diagonal Checks for Player X
    if board[0] == "x" and board[4] == "x" and board[8] == "x":
        print("Player X wins!")
        x_win += 1
        game_over = True

    if board[2] == "x" and board[4] == "x" and board[6] == "x":
        print("Player X wins!")
        x_win += 1
        game_over = True

    # Diagonal Checks for Player O
    if board[0] == "o" and board[4] == "o" and board[8] == "o":
        print("Player O wins!")
        o_win += 1
        game_over = True

    if board[2] == "o" and board[4] == "o" and board[6] == "o":
        print("Player O wins!")
        o_win += 1
        game_over = True

    # Tie Check
    if is_board_full(board):
        print("Its a tie!")
        game_over = True

    print(x_win)
    print(o_win)
    print(score)

    if player == "x":
        score["player"] += x_win
    if player == "o":
        score["player"] += o_win

    if computer == "x":
        score["computer"] += x_win
    if computer == "o":
        score["computer"] += o_win

    return game_over


def play():
    game_over = False
    play_again = True
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "x" if random.randint(0, 1) == 1 else "o"
    computer = "o" if player == "x" else "x"
    score = {"player": 0, "computer": 0}

    print("Welcome to Tic-Tac-Toe by OhhhZenix!")
    while play_again:
        while not game_over:
            print_board(board)
            player_make_move(board, player)
            game_over = check_winner(board, player, computer, score)
            if game_over:
                break

            computer_make_move(board, computer)
            game_over = check_winner(board, player, computer, score)
            if game_over:
                break
        print("Player Score: " + str(score["player"]))
        print("Computer Score: " + str(score["computer"]))
        result = str(input("Would you like to play again? Y/N "))
        if result.upper() == "Y":
            play_again = True
            print("Alright! Lets play again!")
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            game_over = False
            print_board(board)
        if result.upper() == "N":
            play_again = False
            print("It was great playing with you!")
            time.sleep(0.25)


if __name__ == '__main__':
    play()
