###
### Author: Tanner Jackson
### Description: This program recreates the game
### reversi. The program takes a user input of
### what place they would like to have their piece
### go and then the next person can play. Pieces
### can be taken from the other team if there are
### two pieces of the same team surrounding them.
### The game is over when the board is filled up and
### the team with the most pieces on the board wins.
###

from graphics import graphics

# Some constants to be used throughout the code
# The literals 'X' and 'O' and ' ' should not be used elsewhere
WHITE = 'O'
BLACK = 'X'
EMPTY = ' '

def is_move_acceptable(board, pos):
    '''
    This function checks to see if the move can be done
    for the board. If the position is less than one or
    greater than twelve the move is not acceptable. In
    addition, the move is not acceptable if their is a
    black or white piece already in that position.
    pos: Can be any integer.
    board: Is a list with spaces, Os, ans Xs.
    '''
    # Checks if the user input is between 1 and 12.
    if pos > -1 and pos < 12:
        # Checks if there is already a piece on the board
        # where the user wants to put theirs.
        if board[pos] == BLACK or board[pos] == WHITE:
            return False
        return True
    else:
        return False

def move(board, turn, pos):
    '''
    This functon makes the position chosen by the user
    have a black or white piece depending on the turn it
    is. This function also makes it so any connecting
    pices if they have the turn piece at the end will change
    to the turn piece.
    board: Is a list with spaces, Xs, and Os.
    turn: Can be either BLACK or WHITE which correlate to
    'X' or 'O'.
    pos: Can be any integer from 1-12.
    '''
    # Moves the piece to the user desired spot.
    for i in range(len(board)):
        if i == pos:
            board.append(turn)
            board[i] = board[len(board) - 1]
            board.pop(len(board) - 1)
    index = pos
    board[index] = turn
    i = index + 1
    # Checks to the right of the position to overtake
    # their pieces.
    while i < 12 and board[i] == get_opposite_turn(turn):
        i += 1
    if i == 12:
        i = 11
    if board[i] == turn:
        i = index + 1
        while i < 12 and board[i] == get_opposite_turn(turn):
            board[i] = turn
            i += 1
    index = pos
    board[index] = turn
    i = index - 1
    # Checks to the left of the position to overtake
    # their pieces.
    while i > 0 and board[i] == get_opposite_turn(turn):
        i -= 1
    if board[i] == turn:
        i = index - 1
        while i > 0 and board[i] == get_opposite_turn(turn):
            board[i] = turn
            i -= 1

def get_move(turn):
    '''
    This function gets the users move. It asks for a number
    from 1-12 but the user can input any integer into this
    input. Then the number is changed to minus one of itself
    to work in the list.
    turn: Can be either BLACK or WHITE which correlate to
    'X' or 'O'.
    '''
    number = input(turn + ' choose your move:\n')
    return(int(number) - 1)

def is_over(board, turn):
    '''
    This function determines if the game is over or not.
    It does this by counting the amount of pieces on
    the board. If the pieces equals 12 then the game is over.
    board: Is a list with spaces, Xs, and Os.
    turn: Can be either BLACK or WHITE which correlate to
    'X' or 'O'.
    '''
    # Checks to see if their are twelve pieces on the board.
    count = 0
    for i in board:
        if i == turn or i == get_opposite_turn(turn):
            count += 1
    if count == 12:
        return True
    pass

def get_opposite_turn(turn):
    '''
    This function gets the opposite turn whenever is
    necessary in the program. It changes from BLACK to
    WHITE and from WHITE to BLACK.
    turn: Can be either BLACK or WHITE which correlate to
    'X' or 'O'.
    '''
    if turn == BLACK:
        turn = WHITE
    elif turn == WHITE:
        turn = BLACK
    return turn

def print_board(board):
    '''
    This function prints the board in its entirety
    that the game can be played on. This board can
    be played on in the python console.
    board: Is a list with spaces, Xs, and Os.
    '''
    print('+' + ('-' * 23) + '+')
    for i in range(len(board)):
        print(('|' + board[i]), end = '')
    print('|')
    print('+' + ('-' * 23) + '+')
    return board

def draw_board(board, gui):
    '''
    This function draws the board through graphics.
    It looks pretty much the same as the board in
    the python console except for the fact that it is
    colored.
    board: Is a list with spaces, Xs, and Os.
    gui: Is the canvas for graphics.
    '''
    gui.text(235, 25, 'REVERSI', 'black', 50)
    i = 1
    count = 0
    x_coord = 50
    # Prints the square board with the user inputed numbers.
    while i < 13:
        gui.rectangle(x_coord, 125, 50, 50, 'green')
        gui.text(x_coord + 7.5, 120, board[count], 'black', 50)
        gui.line(x_coord, 125, x_coord + 50, 125, 'blue')
        gui.line(x_coord, 175, x_coord + 50, 175, 'blue')
        gui.line(x_coord, 125, x_coord, 175, 'blue')
        i += 1
        count += 1
        x_coord += 50
    gui.line(650, 125, 650, 175, 'blue')
    gui.update_frame(60)
def who_is_winner(board):
    '''
    This function determines who the winner of
    the game is. This is done by counting up
    the amount of black and white pieces and seeing
    which has more. Then it returns the winner of the
    game.
    board: Is a list with spaces, Xs, and Os.
    '''
    count_black = 0
    count_white = 0
    i = 0
    # Checks to see if there are twelve pieces
    # on the board and then checks to see who
    # has the most pieces.
    while i < 12:
        if board[i] == BLACK:
            count_black += 1
        if board[i] == WHITE:
            count_white += 1
        i += 1
    if count_white > count_black:
        return('WHITE WINS')
    elif count_black > count_white:
        return('BLACK WINS')
    else:
        return('THERE WAS A TIE')
def main():
    print('WELCOME TO REVERSI')

    gui = graphics(700, 200, 'reversi')

    # Initialize an empty list with 12 slots
    board = [EMPTY] * 12
    # State of whether or not the game is over
    over = False
    # Starting turn (should alternate as game goes on)
    turn = BLACK

    # Print out the initial board
    print_board(board)
    draw_board(board, gui)

    # Repeatedly process turns until the game should end (every slot filled)
    while not over:
        place_to_move = get_move(turn)
        while not is_move_acceptable(board, place_to_move):
            place_to_move = get_move(turn)
        move(board, turn, place_to_move)

        print_board(board)
        draw_board(board, gui)

        over = is_over(board, turn)
        turn = get_opposite_turn(turn)
    print('GAME OVER')
    print(who_is_winner(board))

main()
