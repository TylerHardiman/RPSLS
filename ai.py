from player import Player
from random import Random

class Ai(Player):
    def __init__(self):
        self.name = ""
        self.random_gestures = ""
        super().__init__()
    
    def ai_turn(self):
        # print(f"Ai randomly selects {self.random_gestures}")
        Player.self.random_gestures = Random(self.random_gestures)
        print(self.random_gestures)

Ai.ai_turn(Player)   
    # def chosen_gesture(self):
    #     self.random_gestures = self.random_number #random_number(Player.gestures)
    #     print(f"{self.random_gestures}")
    #     return self.random_gestures

    # def random_number(self):
    #  end_point = len(Player.gestures) - 1
    #  rng = Random(0,end_point)
    #  return (rng)

    

#     def choices(self):
#         print('Current gesture option: ')
#         i = 0
#         for self.gestures in Ai:
#             print(Random)
#         pass


