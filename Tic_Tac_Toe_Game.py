def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move as row and column (e.g., 1 3): ")
            row, col = map(int, move.strip().split())
            if row in [1, 2, 3] and col in [1, 2, 3]:
                return row - 1, col - 1
            else:
                print("Invalid input. Row and column must be 1, 2 or 3.")
        except ValueError:
            print("Invalid input format. Please enter two numbers separated by space.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player)
        if board[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue
        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
