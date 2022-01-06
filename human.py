from player import Player

class Human(Player):
    def __init__(self):
        pass # needs its super()__init__
    

    def human_hand_options(self):
        print('Current Hand options: ')
        i = 0
        for self.hand in Hand:
            print(f' Press {i} to select {self.hand}')
            i += 1
    def choose_gesture():
        pass