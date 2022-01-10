from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        

    def choose_gesture(self):
        
        i = 1
        for gesture in self.gestures:
            print(f' Press {i} to select {gesture}')
            i += 1
        user_choice = int(input("select a gesture with the number pad")) -1
        self.chosen_gesture = self.gestures[user_choice]
        print(f'you have chosen {self.chosen_gesture}')

        
        pass # this is where our random selection logic will go
    