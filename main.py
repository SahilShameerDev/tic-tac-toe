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


def is_vertically_filled(letter):
    return board[1] == board[2] == board[3] and board[1] != letter or board[4] == board[5] == board[6] and board[4] != letter or board[7] == board[8] == board[9] and board[7] != letter


def is_horizontally_filled(letter):
    return board[1] == board[4] == board[7] and board[1] != letter or board[2] == board[5] == board[8] and board[2] != letter or board[3] == board[6] == board[9] and board[3] != letter


def is_diaganolly_filled(letter):
    return board[1] == board[5] == board[9] and board[1] != letter or board[3] == board[5] == board[7] and board[3] != letter


# checks if the game has ended
def check_win():
    letter = ''
    if is_horizontally_filled(letter) or is_diaganolly_filled(letter) or is_vertically_filled(letter):
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
        pos = int(input('Not a free space pls re-enter a position: '))
        insert(letter, pos)


def is_win(letter):
    if is_horizontally_filled(letter) or is_diaganolly_filled(letter) or is_vertically_filled(letter):
        return True


def minimax(board, is_maximizing):
    if is_win(computer):
        return 1
    elif is_win(human):
        return -1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = -2
        for i in range(1, len(board)):
            if is_available(i):
                board[i] = computer
                score = minimax(board, False)
                board[i] = ''
                best_score = max(best_score, score)

        return best_score
    else:
        best_score = 2
        for i in range(1, len(board)):
            if is_available(i):
                board[i] = human
                score = minimax(board, True)
                board[i] = ''
                best_score = min(best_score, score)

        return best_score


def computer_move(letter):
    best_score = -2
    best_pos = 0

    for i in range(1, len(board)):
        if is_available(i):
            board[i] = letter
            score = minimax(board, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                best_pos = i

    insert(letter, best_pos)
    return


def human_move(letter):
    pos = int(input("Position to be inserted: "))
    insert(letter, pos)


while not check_win():
    display_board(board)
    computer_move(computer)
    human_move(human)
