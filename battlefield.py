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
        print("Welcome, we will begin the throw down shortly")
        print("Select player two Ai or Human?")
        # print README.md
             

    def battle_loop(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture: 
                print("Its a tie!")                                                  
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
        player_choice = input("enter 1 for single player or 2 for mulit player")
        if player_choice == "1":
            self.player_one = Human()
            self.player_two = Ai()
            print('You have chosen Single-player!')
        elif player_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
            print('You have chosen Multi-player!')

        
    def winner(self):
            if self.player_two.wins == 2:
                print()
                print("Player 2 WINS!")
            else:
                print()
                print(f"Player 1  WINS!")
                pass




