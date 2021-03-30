import random
#from IPython.display import clear_output
import os



# print the board
def board_display(board):
    #clear_output() # only works in jupyter
    os.system('cls')
    print(board[7]+'|'+board[8]+'|'+board[9]+'   '+'7'+'|'+'8'+'|'+'9')
    print('-----'+'   '+'-----')
    print(board[4]+'|'+board[5]+'|'+board[6]+'   '+'4'+'|'+'5'+'|'+'6')
    print('-----'+'   '+'-----')
    print(board[1]+'|'+board[2]+'|'+board[3]+'   '+'1'+'|'+'2'+'|'+'3')

# player 1 chooses X or O, player 2 is assigned the remaining letter
def player_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        
        marker = input("Player 1, please choose if you want to be X or O: ").upper()
        if marker != 'X' and marker != 'O':
            print('Sorry, please enter either X or O: ')
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def who_goes_first():
    # random to choose which player goes first
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# place X or O on chosen space
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,marker):
    
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # top
    (board[4] == marker and board[5] == marker and board[6] == marker) or # middle
    (board[1] == marker and board[2] == marker and board[3] == marker) or # bottom
    (board[7] == marker and board[4] == marker and board[1] == marker) or # left
    (board[8] == marker and board[5] == marker and board[2] == marker) or # middle
    (board[9] == marker and board[6] == marker and board[3] == marker) or # right
    (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal

def space_check(board,position):

    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # if board is full, return true
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):

        position = int(input('Choose a position (1-9): '))
        if position not in [1,2,3,4,5,6,7,8,9]:
            print('Sorry, please enter a number between 1 and 9: ') # add case for ValueError: invalid literal for int() with base 10: '' here and throughout to allow for double press of enter
        
        if position != space_check(board,position):
                print('Oops, that space is already taken. Please choose another number.')
    
    return position

def replay():
    
    choice = ''
    while choice != 'y' and choice != 'n':

        choice = input("Do you want to play again? y or n: ").lower()
        if choice != 'y' and choice != 'n':
            print('Sorry, please enter either y or n')
    
    return choice == 'y'

# while loop to keep running game
print("Welcome to Naughts and Crosses! \nYou will see two boards: one with numbers and a blank board. \nUse the number board to choose where you want to palce your marker on the blank board. \nYou will then be prompted to enter the number where you want your marker to be. Type in the number and press enter. \nKeep going until there is a winner or there is a tie!")


# game play
while True:
    # set everything up: board, choose markers, who's first
    num_board = ['#','1','2','3','4','5','6','7','8','9']
    board_in_play = [' ']*10
    player1_marker, player2_marker = player_input()
    player = who_goes_first()
    print(player + ' is going first!')
    
    ready = ''
    while ready != 'y' and ready != 'n':
    
        ready = input('Are you ready to play? y or n: ').lower()
        if ready != 'y' and ready != 'n':
            print('Sorry, please enter either y or n ')

        if ready == 'y':
            game_on = True
        else:
            game_on = False
    
    
        # game play
    while game_on:
        # player 1
        if player == 'Player 1':

            # show the board
            # board_display(num_board)
            board_display(board_in_play)
            # choose a position
            position = player_choice(board_in_play)
            # place marker on position
            place_marker(board_in_play, player1_marker, position)
            board_display(board_in_play)

            # check if they won
            if win_check(board_in_play,player1_marker):
                board_display(board_in_play)
                print('Player 1 in the winner!')
                game_on = False
            # check if there's a tie
            else:
                if full_board_check(board_in_play):
                    board_display(board_in_play)
                    print("It's a tie!")
                    game_on = False
            # no tie or win, move to player 2
                else:
                    player = 'Player 2'

        # player 2
        else:

            # show the board
            # board_display(num_board)
            board_display(board_in_play)
            # choose a position
            position = player_choice(board_in_play)
            # place marker on position
            place_marker(board_in_play, player2_marker, position)
            board_display(board_in_play)
            # check if they won
            if win_check(board_in_play,player2_marker):
                board_display(board_in_play)
                print('Player 2 in the winner!')
                game_on = False
            # check if there's a tie
            else:
                if full_board_check(board_in_play):
                    board_display(board_in_play)
                    print("It's a tie!")
                    game_on = False
            # no tie or win, move to player 1
                else:
                    player = 'Player 1'
    
    
 # break out of the while loop on replay()   
    if not replay():
        break