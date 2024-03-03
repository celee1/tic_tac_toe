player_1 = input('Hello player one, type in your name? ')
player_2 = input('Hello player_two, type in your name? ')

instructions = input('If you need instruction, type in yes, if no just hit enter: ')
instructions = 'no'
if instructions.lower() == 'yes':
        print(''' 
An example of a board.
              
        1 | 2 | 3
        4 | 5 | 6
        7 | 8 | 9
        
If you wish to mark the spot, type in a number and you will mark it :)
''')
        print("player_1's spots will be marked as X")
        print("player_2's spots will be marked with O")
        

board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def make_board():
        return  f'''
        {board[1]} |  {board[2]} |  {board[3]}
        {board[4]} |  {board[5]} |  {board[6]}
        {board[7]} |  {board[8]} |  {board[9]}
'''

def play_game(player, game_dict = board):
        spot = int(input('Choose a spot: '))
        if player == player_1:
                mark = 'X'
        else:
                mark = 'O'

        if game_dict[spot] == ' ':
                game_dict[spot] = mark
        else:
                print('The spot is taken, try another spot')
                play_game(player, game_dict=board)

def determine_winner():
        patterns = [[board[1], board[2], board[3]], [board[4], board[5], board[6]], [board[7], board[8], board[9]], [board[1], board[4], board[7]],
                    [board[2], board[5], board[8]], [board[3], board[6], board[9]], [board[1], board[5], board[9]], [board[3], board[5], board[7]]]
        
        for pattern in patterns:              
                if pattern == ['X', 'X', 'X']:
                        return 'Player 1 wins!'
                elif pattern == ['O', 'O', 'O']:
                        return 'Player 2 wins!'
                
        return "It's a draw!"

for i in range(9):
        if i % 2 == 0:
                player = player_1
        else:
                player = player_2
        play_game(player)
        game = make_board()
        print(game)
        winner = determine_winner()
        if winner != "It's a draw!":
                print(winner)
                break
        else:
                if i == 8:
                        print(winner)