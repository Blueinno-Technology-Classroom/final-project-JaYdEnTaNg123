class Player:
    def __init__(self,name,piece,board):
        self.name = name
        self.piece = piece
        self.board = board

    def get_input(self):
        print(f'Current player: {self.name} ({self.piece})')
        row = input('Enter a row number (0 ~ 2): ')
        if not (row in ['0', '1', '2']):
            return False
        row = int(row)
        col = input('Enter a column number (0 ~ 2): ')
        if not (col in ['0', '1', '2']):
            return False
        col = int(col)
        return self.board.place_piece(self.piece,row,col)