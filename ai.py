from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
    
    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f'AI has chosen {self.chosen_gesture}')