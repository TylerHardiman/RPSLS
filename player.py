class Player():
        def __init__(self, name): # remember all of the properties will be passed down to the child classes human and ai
            self.chosen_gesture = ""
            self.name = name
            self.wins = 0
            self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]


            # option A - leave this logic as pass and method override in human and ai to give this method new logic
            # or you could put the logic here for human and method override the logic in ai 
            pass
           