def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")


def check_win(board, mark):

    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]           
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True
    return False

def check_draw(board):
    return all(spot != ' ' for spot in board)


def tic_tac_toe():
    board = [' '] * 9 
    current_player = 'X' 

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:

        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if move < 0 or move >= 9 or board[move] != ' ':
            print("Invalid move. Please try again.")
            continue

        board[move] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()