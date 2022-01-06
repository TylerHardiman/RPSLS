class Weapon:
    def __init__(self, name, rock, paper, scissors, lizard, spock):
        
            self.name = name
            self.hand = ['self', 'name', 'rock', 'paper', 'scissors', 'lizard', 'spock']
            print("Start dino turn")
            self.hand()
            self.hand = int(input("Select the robot to attack"))
            self.hand[self.hand]



class Hand(self):
    def __init__(self, name, rock, paper, scissors, lizard, spock):
        self.name = name
        self.rock = rock
        self.paper = paper
        self.scissors = scissors
        self.lizard = lizard
        self.spock = spock

    def rock(self):
        self.rock = self.rock > self.scissors or self.rock > self.lizard
        print(' ')

    def paper(self):
        self.paper = self.paper > self.rock or self.paper > self.spock
        print(' ')

    def scissor(self):
        self.scissor = self.scissors > self.lizard or self.scissors > self.paper
        print(' ')

    def lizard():
        self.lizard = self.lizard > self.spock or self.lizard > self.paper
        print(' ')
        
    def spock():
        self.spock = self.spock > self.rock or self.spock > self.scissors
        print(' ')