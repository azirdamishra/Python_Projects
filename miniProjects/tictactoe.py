from IPython.display import clear_output
#make the display board displaying the marked Xs and Os taking info from the list called board

#this function can print out the board as a list using a 3x3 board vision
def display_board(board):
    clear_output() #this function only works in jupyter
    #this is used to clear memory of past boards
    print(' ' + '|' + ' ' + '|' + ' ')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(' ' + '|' + ' ' + '|' + ' ')
    print('-----')
    print(' ' + '|' + ' ' + '|' + ' ')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(' ' + '|' + ' ' + '|' + ' ')
    print('-----')
    print(' ' + '|' + ' ' + '|' + ' ')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(' ' + '|' + ' ' + '|' + ' ')


#this function can take in player input and mark it as X or O
def player_input():
    
    player1 = ''
    
    while(player1 != 'X' and player1 != 'O'):
        player1 = input("Player1, please pick a marker 'X' or 'O'")
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return [player1, player2]

#assigns stuff to the board
def place_marker(board, marker, position):
    board[position] = marker
    
     #the board is an empty list as of now


#checks whether the player has won
def win_check(board, mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) )


#randomly decides which player goes first
import random

def choose_first():
    num = random.randint(1, 16)
    if num > 8:
        return 'Player1'
    else:
        return 'Player2'

        #this will be used as a confirmational string to decide the 
        #steps played by the player and the marker assigned

#checks if the chosen space is empty on the board
def space_check(board, position):
    return board[position] == ' '


#checks if the board is full
def full_board_check(board):
    for num in board:
        if num == ' ':
            return False
    return True


#prompts the user to choose value for their turn
def player_choice(board):
    position = 0
    while not space_check(board, position) or position not in [1,2,3,4,5,6,7,8,9]:
        position = int(input('Choose your position from 1 - 9'))
    return position


#asks player if they want to play again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


#final game 
print('Welcome to Tic Tac Toe!')

while True:
    #reset the board
    board = [' '] * 11
    #make a list declarationn and do the list assignment
    [p1_marker, p2_marker] = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Are you ready to play? Yes or No')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player1':
            #player 1's turn
            
            display_board(board)
            print("Player1's turn")
            position = player_choice(board)
            place_marker(board, p1_marker, position)
            
            if win_check(board, p1_marker):
                display_board(board)
                print('Player1 won the game')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player2'
        
        else:
            #player 2's turn
            
            display_board(board)
            print("Player2's turn")
            position = player_choice(board)
            place_marker(board, p2_marker, position)
            
            if win_check(board, p2_marker):
                display_board(board)
                print('Player2 won the game')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player1'
        
    if not replay():
        break
            
    
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break
        


    
        
