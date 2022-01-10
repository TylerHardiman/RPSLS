from human import Human
from ai import Ai

class Battlefield():
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human() or Ai()
        # We would need to setup a input and if elif to setup how many players based off of selection
    
    def run_game():
        pass


    def game_welcome_and_rules(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
        print('')
    
    def game_play(): # remember first player with 2 round wins is the winner of best of 3
                    # check first to see if its a tie, then check all of the win conditions for player 1 finally our else can be player 2 wins 
        while self.player_one_wins < 2 and self.player_two_wins < 2:
            self.player_one_turn()
            if len(self.player_two_wins) == 0:
                pass
            else:
                self.player_two_turn

    def player_turn():
        # input
        # method that adds wins. ex win = + 1 tie = + 0
        # show option

    def player_options():
        # inheritance to player turn(?)
        print('Current Dino Herd')
        index = 0
        for dino in self.herd.dinos:
            print(f'Press {index} to select {dino.name} ({dino.health} health)')
            index += 1


    def winner():
            if self.player_two_wins == 0:
                print(f"")
                print(f"Player One WINS!")
            else:
                print("")
                print(f"Player WINS!")
                pass
