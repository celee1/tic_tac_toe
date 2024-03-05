
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
        


class Tic_Tac_Toe:
        def __init__(self):
                self.player_1 = input('Hello player one, type in your name? ')
                self.player_2 = input('Hello player_two, type in your name? ')

                self.board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

                self.play_game()

        def make_board(self, board):
            return  f'''
                    {board[1]} |  {board[2]} |  {board[3]}
                    {board[4]} |  {board[5]} |  {board[6]}
                    {board[7]} |  {board[8]} |  {board[9]}
                    '''
        
        def make_turn(self, player):
            game_dict = self.board
            spot = int(input('Choose a spot: '))

            if player == self.player_1:
                mark = 'X'
            else:
                mark = 'O'

            if game_dict[spot] == ' ':
                game_dict[spot] = mark
            else:
                print('The spot is taken, try another spot')
                self.make_turn(player)

        def play_game(self):
              for i in range(9):
                if i % 2 == 0:
                    player = self.player_1
                else:
                    player = self.player_2
                self.make_turn(player)
                game = self.make_board(self.board)
                print(game)
                winner = self.determine_winner()
                if winner != "It's a draw!":
                    print(winner)
                    break
                else:
                    if i == 8:
                        print(winner)

        def determine_winner(self):
            board = self.board
            patterns = [[board[1], board[2], board[3]], [board[4], board[5], board[6]], [board[7], board[8], board[9]], [board[1], board[4], board[7]],
                        [board[2], board[5], board[8]], [board[3], board[6], board[9]], [board[1], board[5], board[9]], [board[3], board[5], board[7]]]
        
            for pattern in patterns:              
                if pattern == ['X', 'X', 'X']:
                        return f'{self.player_1} wins!'
                elif pattern == ['O', 'O', 'O']:
                        return f'{self.player_2} wins!'
                
            return "It's a draw!"


Tic_Tac_Toe()