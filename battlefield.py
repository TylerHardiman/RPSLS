from ai import Ai
from human import Human

class Battlefield:
    def __init__(self):
        self.player_one = None
        self.player_two = None

    def run_game(self):
        self.setup_game()
        self.player_select() # TESTED
        self.battle_loop()  # Needs Testing after logic fixed
        self.winner() #needs testing 
    
    def setup_game(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print()
        print('Game Rules')
        print() 
        print('Rock crushes Scissors and Lizard')
        print('Paper covers Rock and disproves Spock')
        print('Scissors cuts Paper and decapitates Lizard')
        print('Lizard eats Paper and poisons Spock')
        print('Spock vaporises Rock and smashes Scissors')
        print()
        print('First to two wins!')
        print()
        print("Select game mode: ")
        
             

    def battle_loop(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture: 
                continue                                           
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == ("Scissors" or "Lizard"):
                print("player 1 wins this hand")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == ("Rock" or "Spock"):
                print("player 1 wins this hand")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == ("Papers" or "Lizard"):
                print("player 1 wins this hand")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == ("Paper" or "Spock"):
                print("player 1 wins this hand")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == ("Rock" or "Scissors"):
                print("player 1 wins this hand")
                self.player_one.wins += 1
            else:
                print("player 2 wins this hand")
                self.player_two.wins += 1

    def player_select(self):
        player_choice = input("Enter 1 for Single Player or 2 for Mulit-player: ")
        if player_choice == "1":
            self.player_one = Human()
            self.player_two = Ai()
            print('You have chosen Single-player! Please select your first gesture to being RPSLS! ')
        elif player_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
            print('You have chosen Multi-player! Please select your first gesture to being RPSLS! ')
            print()

        
    def winner(self):
            if self.player_two.wins == 2:
                print()
                print("Player 2 WINS!")
            else:
                print()
                print(f"Player 1 WINS!")
                pass




