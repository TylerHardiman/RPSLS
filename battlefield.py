player_one_lives = 2
player_two_lives = 2

class Battlefield:
    def __init__(self):
        self.human = ''
        self.ai = ''
        # We would need to setup a input and if elif to setup how many players based off of selection
    
    def setup_game(self):
        print("Welcome, we will begin the throw down shortly")
        print("Select player two Ai or Human?")
        self.ai()
        self.human()     

    def run_game_welcome(self):
        lives = 2
        while len(player_one_lives) > 0 and len(player_two_lives) > 0:
            self.round()
        self.declare_winner()

    def round(self):
        self.player_one_turn()
        self.player_two_turn()

    def player_one_turn(self):
        if len(player_one_lives) != 0:
            player_one_lives[0].attack(player_two_lives[0])
            self.check_lives(player_one_lives)

    def player_two_turn(self):
        if len(player_two_lives) != 0:
            player_two_lives[0].attack(player_one_lives[0])
            self.check_lives(player_two_lives)

    def check_lives(self, player_one_lives):
        if(player_one_lives[0]<= 0):
            player_one_lives.pop(0)

    def declare_winner(self):
        if len(player_two_lives) == 0:
            print("Player One wins!!!")
        elif len(player_one_lives) == 0:
            print("Player Two Wins!!!")
        else:
            print("How?")

    # def player_select(self):# need input to gather if they player wants 1 or 2 players
    #     if input == 1:
    #         self.player_one = Human()
    #         self.player_two = Ai()
    #         print('You are Human!')
    #     elif input == 2:
    #         self.player_one = Human()
    #         self.player_two = Human()
    #         self.player_two 
    #         print('Ai vs Ai')
    #         pass
        
    #         # remember first player with 2 round wins is the winner of best of 3
    #                 # check first to see if its a tie, then check all of the win conditions for player 1 finally our else can be player 2 wins 
        
    #                                     #Ai is set for player 2
    
    # def game_play(self): 
    #     while self.player_one_wins < 2 and self.player_two_wins < 2:
    #         self.player_one_turn()
    #         if len(self.player_two_wins) == 0:
    #             pass
    #         else:
    #             self.player_two_turn

    # def player_turn(self):


    #     # input
    #     # method that adds wins. ex win = + 1 tie = + 0
    #     # show option

    #     def player_options(self):
  


    def winner(self):
            if self.player_two_wins == 0:
                print(f"")
                print(f"Player One WINS!")
            else:
                print("")
                print(f"Player WINS!")
                pass




# from human import Human
# from ai import Ai

# class Battlefield:
#     def __init__(self):
#         self.player_one = Ai
#         self.player_two = Human or Ai
#         # We would need to setup a input and if elif to setup how many players based off of selection
    
#     def run_game(self):
#         self.game_welcome()
#         self.player_select()
        
#     def game_welcome(self):
#         print(f'Welcome to Rock, Paper, Scissors, Lizard, Spock!')
#         pass
        
#     def player_select(self):# need input to gather if they player wants 1 or 2 players
#         if input == 1:
#             self.player_one = Human()
#             self.player_two = Ai()
#             print('You are Human!')
#         elif input == 2:
#             self.player_one = Human()
#             self.player_two = Human()
#             self.player_two 
#             print('Ai vs Ai')
#             pass