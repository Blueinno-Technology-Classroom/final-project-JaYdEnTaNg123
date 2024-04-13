from board import Board
from player import Player
import random
from com import ComputerPlayer

board = Board()

# print(board.row1)
# board.draw()

# board.row1 = ['X', 'O', 'X']
# board.row2 = [' ', 'X', 'O']
# board.row3 = ['O', 'X', 'O']
# board.draw()


print('Select a mode')
print('1. Player vs Player')
print('2. Player vs Computer')

mode = input()
while mode not in ['1','2']:
    mode = input('invalid input, please try again')

if mode == '2':

    namelist = [
    'clanker',
    'Roz',
    'tyro'
]
    nameid = input(f'Pick a name for the computer (0~{len(namelist)-1}): {namelist}')
    botname = namelist[int(nameid)]

player1 = Player('P1', 'o', board)
if mode == '1':
    player2 = Player('P2', 'x', board)
else:
    player2 = ComputerPlayer(botname, 'x', board)
current_player = random.choice([player1, player2])

while True:
    not_valid = True
    while not_valid:
        board.draw()
        if mode == 1 or current_player == player1:
            not_valid = not (current_player.get_input())
            if not_valid:
                print('-------------------')
                print('Invalid input, try again')
                print('-------------------')
                    
        else:
            not_valid = False
            current_player.move()

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

    winner = board.check_winner()
    tie = board.is_full()

    if winner == player1.piece:
        board.draw()
        print(f'{player1.name} wins!!')
        break
    elif winner == player2.piece:
        board.draw()
        print(f'{player2.name} wins!!')
        break
    elif tie:
        board.draw()
        print(f'Game tied beat {random.choice([player1.name, player2.name])} next time:(')
        break