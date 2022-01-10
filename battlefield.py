from ai import Ai
from human import Human

class Battlefield:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        # We would need to setup a input and if elif to setup how many players based off of selection
    def run_game(self):
        self.setup_game()
        self.player_select() # TESTED
        self.battle_loop()  # Needs Testing after logic fixed
        #self.winner() #needs testing 
    
    def setup_game(self):
        print("Welcome, we will begin the throw down shortly")
        print("Select player two Ai or Human?")
             

    def battle_loop(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture() # saves gesutre under self.chosen_gesture
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:   # make a check for each gesture player one could choose 
                print("its a tie")                                                  # check to see if its a tie, check if player one wins, else player 2 wins.
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == ("Scissors" or "Lizard"):
                print("player one winds this hand")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == ("Scissors" or "Lizard"):
                print("player one winds this hand")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == ("Scissors" or "Lizard"):
                print("player one winds this hand")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == ("Scissors" or "Lizard"):
                print("player one winds this hand")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == ("Scissors" or "Lizard"):
                print("player one winds this hand")
                self.player_one.wins += 1
            else:
                print("player 2 wins this hand")
                self.player_two.wins += 1

    def check_lives(self, player_one_lives):
        if(player_one_lives[0]<= 0):
            player_one_lives.pop(0)

    def declare_winner(self):
        if len(player_two_lives) == 0:
            print("Player One wins!!!")
        elif len(player_one_lives) == 0:
            print("Player Two Wins!!!")
        else:
            print("Tie Breakerrrr?")

    def player_select(self):# need input to gather if they player wants 1 or 2 players
        player_choice = input("enter 1 for single player or 2 for mulit player")
        if player_choice == "1":
            self.player_one = Human()
            self.player_two = Ai()
            print('You are Human!')
        elif player_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
            self.player_two 
            print('Ai vs Ai')
            pass
        


    def winner(self):
            if self.player_two.wins == 2:
                print()
                print("Player two WINS!")
            else:
                print()
                print(f"Player one  WINS!")
                pass




