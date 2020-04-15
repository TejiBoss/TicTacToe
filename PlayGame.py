import Game
import GamePlayer
import GameBoard

print('Welcome to Tic Tac Toe!')
player1Name = input('Player 1 : Please enter your name ? ').title()
player2Name = input('Player 2 : Please enter your name ? ').title()

player1 = GamePlayer.GamePlayer(player1Name)
player2 = GamePlayer.GamePlayer(player2Name)

tictactoe = Game.Game(player1, player2)

while True:
    tictactoe.play()
    if not tictactoe.playAgain():
        break
