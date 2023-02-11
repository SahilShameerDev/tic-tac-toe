import random

board = ['']*10
computer = 'X'
human = 'O'


# Board to be played is created
def display_board(board):
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("-" * 10)

# checks if the cells are filled


def is_vertically_filled():
    return board[1] == board[2] == board[3] and board[1] != '' or board[4] == board[5] == board[6] and board[4] != '' or board[7] == board[8] == board[9] and board[7] != ''


def is_horizontally_filled():
    return board[1] == board[4] == board[7] and board[1] != '' or board[2] == board[5] == board[8] and board[2] != '' or board[3] == board[6] == board[9] and board[3] != ''


def is_diaganolly_filled():
    return board[1] == board[5] == board[9] and board[1] != '' or board[3] == board[5] == board[7] and board[3] != ''


# checks if the game has ended
def check_win():
    if is_horizontally_filled() or is_diaganolly_filled() or is_vertically_filled():
        return True


def check_draw():
    return board.count('') < 2


def is_available(pos):
    return board[pos] == ''


def insert(letter, pos):
    if is_available(pos):
        board[pos] = letter
        display_board(board)
        if check_win() and letter == 'X':
            print('computer wins')
            exit()
        elif check_win():
            print('human wins')
            exit()

        if check_draw():
            print('draw')
            exit()
    else:
        if letter == 'O':
            pos = int(input('Not a free space pls re-enter a position: '))
        elif letter == 'X':
            pos = random.randint(1, 9)

        insert(letter, pos)


def computer_move(letter):
    pos = random.randint(1, 9)
    insert(letter, pos)


def human_move(letter):
    pos = int(input("Position to be inserted: "))
    insert(letter, pos)


while not check_win():
    display_board(board)
    computer_move(computer)
    human_move(human)
