class Board:
    def __init__(self):
        self.row1 = [" ", " "," "]
        self.row2 = [" ", " "," "]
        self.row3 = [" ", " "," "]

    def draw(self):
        print(' '*5+'|'+' '*5+'|'+' '*5)
        print(f'  {self.row1[0]}  |  {self.row1[1]}  |  {self.row1[2]}  ')
        print('-----|-----|-----')
        print(f'  {self.row2[0]}  |  {self.row2[1]}  |  {self.row2[2]}  ')
        print('-----|-----|-----')
        print(f'  {self.row3[0]}  |  {self.row3[1]}  |  {self.row3[2]}  ')
        print(' '*5+'|'+' '*5+'|'+' '*5)

    def place_piece(self,piece,row,col):
        if(row == 0):
            if(self.row1[col]!=' '):
                return False
            else:
                self.row1[col] = piece
                return True
        if(row == 1):
            if(self.row2[col]!=' '):
                return False
            else:
                self.row2[col] = piece
                return True
        if(row == 2):
            if(self.row3[col]!=' '):
                return False
            else:
                self.row3[col] = piece
                return True
            

    def check_winner(self):
        if self.row1[0] == self.row1[1] == self.row1[2] != ' ':
            return self.row1[0]
        if self.row2[0] == self.row2[1] == self.row2[2] != ' ':
            return self.row2[0]
        if self.row3[0] == self.row3[1] == self.row3[2] != ' ':
            return self.row3[0]
        if self.row1[0] == self.row2[0] == self.row3[0] != ' ':
            return self.row1[0]
        if self.row1[0] == self.row2[1] == self.row3[2] != ' ':
            return self.row1[0]
        if self.row3[0] == self.row2[1] == self.row1[2] != ' ':
            return self.row3[0]
        if self.row2[0] == self.row2[1] == self.row2[2] != ' ':
            return self.row3[0]
        if self.row2[0] == self.row2[1] == self.row2[2] != ' ':
            return self.row3[0]
        if self.row1[0] == self.row2[1] == self.row3[2] != ' ':
            return self.row3[0]
        return ' '
        
    def is_full(self):
        if' ' in self.row1:
            return False
        if' ' in self.row2:
            return False
        if' ' in self.row3:
            return False
        return True