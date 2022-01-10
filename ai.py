from typing_extensions import Self
from player import Player
from random import Random, randint

class Ai(Player):
    def __init__(self):
        self.name = ""
        self.random_gestures = ""
        super().__init__()
        
    # def random(self):
    #    Random(randint[self.random_gestures])
    #    print(self.random_gestures)
    
    def random_number(self):
     end_point = len(self.random_gestures) - 1
     rng = randint(0,end_point)
     return (rng)


    def chosen_gesture(self):
        self.random_gestures = self.random_number(Player.gestures)
        print(f"{self.random_gestures}")
        return self.random_gestures

#     def choices(self):
#         print('Current gesture option: ')
#         i = 0
#         for self.gestures in Ai:
#             print(Random)
#         pass



Ai.chosen_gesture()