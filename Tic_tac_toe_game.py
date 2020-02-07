#--------- Global Variables -----------


# Board to hold the game
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


# Lets us know if the game is over yet
game_still_going = True


# Tells us who the winner is
winner = None


# Tells us who the current player is (X goes first)
current_player = 'X'


# ------------ Functions --------------


# Display the game board to the screen
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# Play a game of tic tac toe
def play_game():

    # Shows initial board
    display_board()

    # Game loop
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    '''Check if the winner global variable is 'X' or 'O', meaning somebody won, and if so, print out the winner. 
    Else print that there was a tie'''

    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')


# Handle a turn for an arbitrary player
def handle_turn(player):

    # Get the position from player
    print(player + "'s turn.")
    position = input('Choose a position from 1-9: ')

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Choose a position from 1-9: ')

        # Get correct index in the board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == '-':
            valid = True
        else:
            print('You can\'t go there. Go again.')

    # Take the position variable (it's a string) then input player variable into the board variable
    board[position] = player
    display_board()


# Check to see if the game should be over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check to see if somebody has won
def check_for_winner():

    # Global variables we need access to
    global winner

    # Check rows, columns and diagonals
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():

    # Global variables we need access to
    global game_still_going

    if board[0] == board[1] == board[2] != '-':
        game_still_going = False
        return board[0]
    elif board[3] == board[4] == board[5] != '-':
        game_still_going = False
        return board[3]
    elif board[6] == board[7] == board[8] != '-':
        game_still_going = False
        return board[6]


# Check the columns for a win
def check_columns():

    # Global variables we need access to
    global game_still_going

    if board[0] == board[3] == board[6] != '-':
        game_still_going = False
        return board[0]
    elif board[1] == board[4] == board[7] != '-':
        game_still_going = False
        return board[1]
    elif board[2] == board[5] == board[8] != '-':
        game_still_going = False
        return board[2]


# Check the diagonals for a win
def check_diagonals():

    # Global variables we need access to
    global game_still_going

    if board[0] == board[4] == board[8] != '-':
        game_still_going = False
        return board[0]
    elif board[6] == board[4] == board[2] != '-':
        game_still_going = False
        return board[6]


# Check if there is a tie on the board
def check_for_tie():

    # Global variables we need access to
    global game_still_going

    # Figure out the conditions for a tie
    if '-' not in board:
        game_still_going = False


# Flip the current player from X to O, or O to X
def flip_player():

    # Global variables we need access to
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


# ------------ Start Execution -------------


# Play a game of tic tac toe
play_game()
