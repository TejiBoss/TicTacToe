import GameBoard
import GamePlayer
import random


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = GameBoard.GameBoard()

    def __repr__(self):
        return "<" + "This game is between " + self.player1 + "and" + self.player2 + ">"

    def getPlayerLetters(self):
        letter = " "
        pick = random.randint(1, 2)
        if pick == 1:
            while not (letter == "X" or letter == "O"):
                letter = input(f"{self.player1.getName()}, choose if you want to be X or O ? : ").upper()
            if letter == "X":
                return ["X", "O"]
            else:
                return ["O", "X"]
        else:
            while not (letter == "X" or letter == "O"):
                letter = input(f"{self.player2.getName()}, choose if you want to be X or O ? : ").upper()
            if letter == "X":
                return ["O", "X"]
            else:
                return ["X", "O"]

    def whoGoesFirst(self):
        if random.randint(1, 2) == 1:
            return self.player1
        else:
            return self.player2

    def playAgain(self):
        choice = input("Do you want to play again? : ")
        return choice.lower().startswith("y")

    def play(self):
        letters = self.getPlayerLetters()
        self.player1.setLetter(letters[0])
        self.player2.setLetter(letters[1])
        self.board.clear()
        self.board.draw()

        turn = self.whoGoesFirst()

        while True:
            if turn == self.player1:
                if self.__playTurn(self.player1):
                    break
                else:
                    turn = self.player2
            else:
                if self.__playTurn(self.player2):
                    break
                else:
                    turn = self.player1

    def __playTurn(self, player):
        # This method gets player move and checks if he has won the game or the game is tied.
        # Return true if game is over. otherwise returns false
        self.__makeMove(player)
        if self.__checkWinner(player):
            return True
        else:
            if self.__gameIsTied():
                return True
        return False

    def __getPlayerMove(self, player):
        while True:
            move = int(player.getMove())
            if self.board.isSpaceFree(move):
                return int(move)

    def __gameIsTied(self):
        if self.board.isFull():
            print ("This game is a tie")
            return True
        return False;

    def __makeMove(self, player):
        move = self.__getPlayerMove(player)
        self.board.makeMove(player.getLetter(), move)
        self.board.draw()

    def __checkWinner(self, player):
        if self.board.isWinner(player.getLetter()):
            print(player.getName() + " has won the game.")
            return True
        return False

