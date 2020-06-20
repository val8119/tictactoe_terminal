def print_board(board):
    print(f"""
| {board[0]} | {board[1]} | {board[2]} |
|---|---|---|
| {board[3]} | {board[4]} | {board[5]} |
|---|---|---|
| {board[6]} | {board[7]} | {board[8]} |
""")


def check_board():
    global is_tie, turns

    game_finished = False

    if board[0] == board[1] and board[0] == board[2]:
        game_finished = True
    if board[3] == board[4] and board[3] == board[5]:
        game_finished = True
    if board[6] == board[7] and board[6] == board[8]:
        game_finished = True

    if board[0] == board[3] and board[0] == board[6]:
        game_finished = True
    if board[1] == board[4] and board[1] == board[7]:
        game_finished = True
    if board[2] == board[5] and board[2] == board[8]:
        game_finished = True

    if board[0] == board[4] and board[0] == board[8]:
        game_finished = True
    if board[2] == board[4] and board[2] == board[6]:
        game_finished = True

    if turns == 9 and not game_finished:
        is_tie = True

    return game_finished


current_player = "x"


def switch_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"


last_player = ""
command = ""
first_play = True
is_tie = False
turns = 0
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    print("\nStart the game? (yes/no)") if first_play else print("\nPlay again? (yes/no)")

    command = input("> ").lower()

    if command == "yes":

        turns = 0

        is_tie = False

        first_play = False

        while True:
            print_board(board)

            if check_board():
                print(f"\n{last_player} wins!")
                break
            else:
                pass

            if is_tie:
                print("It's a tie!")
                break

            print(f"{current_player}'s turn")

            location = int(input("> "))

            turns += 1

            board[location - 1] = current_player

            last_player = current_player

            switch_player()

    elif command == "no":
        break

print("Goodbye!")
