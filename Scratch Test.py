class Player():
        def __init__(self, name): # remember all of the properties will be passed down to the child classes human and ai
            self.chosen_gesture = ""
            self.name = name
            self.wins = 0
            self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

