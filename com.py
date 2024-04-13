import math
import random

class ComputerPlayer:
    def __init__(self,name,piece,board):
        self.name = name
        self.piece = piece
        self.board = board

    def move(self):
        space = []
        for i in range(3):
            if self.board.row1[i] == ' ':
                space.append(10+i)
            if self.board.row2[i] == ' ':
                space.append(20+i)
            if self.board.row3[i] == ' ':
                space.append(30+i)

        my_move = random.choice(space)
        row = math.floor(my_move/10)-1
        col = my_move % 10
        print(f'Current player: {self.name} ({self.piece})')
        self.board.place_piece(self.piece,row,col)