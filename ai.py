from hand import Hand

class Ai():
    def __init__(self):
        pass #needs super init

    def ai_hand_options(self):
        print('Current Hand options: ')
        i = 0
        for self.hand in Hand:
            print(f' Press {i} to select {self.hand}')
            i += 1


    def choose_gesture(self):
        pass # this is where our random selection logic will go
