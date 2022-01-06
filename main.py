from hand import Hand

class Ai():
    def __init__(self, name):
        self.name = name
        self.human = Ai()
        self.hand = Hand()

    def ai_hand_options(self):
        print('Current Hand options: ')
        i = 0
        for self.hand in Hand:
            print(f' Press {i} to select {self.hand}')

    
