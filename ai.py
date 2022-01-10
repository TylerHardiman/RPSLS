from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
    
    def choose_gesture(self):
        # print(f"Ai randomly selects {self.random_gestures}")
        self.chosen_gesture = random.choice(self.gestures)
        print(f'AI has chosen {self.chosen_gesture}')


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


