# from battlefield import Battlefield
# battlefield = Battlefield()

# battlefield.run_game()

from human import Human
from ai import Ai

player_one_wins = True
player_two_wins = False

class Battlefield:
    def __init__(self):
        self.player_one = Ai
        self.player_two = Human or Ai
        # We would need to setup a input and if elif to setup how many players based off of selection
    
    def run_game(self):
        self.game_welcome()
        self.player_select()
        
    def game_welcome(self):
        print(f'Welcome to Rock, Paper, Scissors, Lizard, Spock!')
        pass
        
    def player_select(self):# need input to gather if they player wants 1 or 2 players
        if input == 1:
            self.player_one = Human()
            self.player_two = Ai()
            print('You are Human!')
        elif input == 2:
            self.player_one = Human()
            self.player_two = Human()
            self.player_two 
            print('Ai vs Ai')
            pass



    
