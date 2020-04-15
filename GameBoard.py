class GameBoard:

    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __repr__(self):
        return self.board

    def draw(self):
        # "self.board" is a list of 10 strings representing the self.board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def isWinner(self, letter):
        # Given a self.board and a player's letter, this function returns True if that player has won.
        # We use self.board instead of self.board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == letter and self.board[8] == letter and self.board[9] == letter) or  # across the top
                (self.board[4] == letter and self.board[5] == letter and self.board[6] == letter) or  # across the middle
                (self.board[1] == letter and self.board[2] == letter and self.board[3] == letter) or  # across the self.boardttom
                (self.board[7] == letter and self.board[4] == letter and self.board[1] == letter) or  # down the left side
                (self.board[8] == letter and self.board[5] == letter and self.board[2] == letter) or  # down the middle
                (self.board[9] == letter and self.board[6] == letter and self.board[3] == letter) or  # down the right side
                (self.board[7] == letter and self.board[5] == letter and self.board[3] == letter) or  # diagonal
                (self.board[9] == letter and self.board[5] == letter and self.board[1] == letter))  # diagonal

    def clear(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def isFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True
