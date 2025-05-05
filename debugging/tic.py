#!/usr/bin/python3

def print_board(board):
    """
    Prints the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks whether there is a winner. 
    Returns True if there's a winner, otherwise False.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Checks if the board is full, indicating a draw.
    Returns True if the board is full and there's no winner.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function that runs the Tic Tac Toe game.
    It alternates between two players 'X' and 'O', handles input and checks for winners or draws.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize empty board
    player = "X"
    while True:
        print_board(board)

        # Get valid row input
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2]:
                    print("Invalid row! Please enter a value between 0 and 2.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a number between 0 and 2.")

        # Get valid column input
        while True:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in [0, 1, 2]:
                    print("Invalid column! Please enter a value between 0 and 2.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a number between 0 and 2.")

        # Check if the selected spot is available
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken! Try again.")
            continue

        # Check if there's a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        player = "O" if player == "X" else "X"

# Start the game
tic_tac_toe()
