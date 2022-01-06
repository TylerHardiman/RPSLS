from hand import Hand

class Human():
    def __init__(self, name ):
        self.name = name
        self.human = Human()
        self.hand = Hand()

    def human_hand_options(self):
        print('Current Hand options: ')
        i = 0
        for self.hand in Hand:
            print(f' Press {i} to select {self.hand}')
            i += 1