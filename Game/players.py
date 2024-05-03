import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def guess_letter(self, letter):
        pass
class AI_Player(Player):
    'Class representing the AI player'
    def __init__(self, name):
        super().__init__(name + '_bot')
        self.memory = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
    def guess_letter(self, choices):
        if len(self.memory) == 0:
            return "null"
        letter = self.memory.pop(random.randrange(len(self.memory)))
        if letter in choices:
            return self.guess_letter(choices)          
        else:
            choices.append(letter)
            print(f"{self.name} guessed: {letter}")
            return letter
class Human_Player(Player):
    def __init__(self, name):
        super().__init__(name)

    def guess_letter(self, choices):
        letter = input("Guess a letter: ")
        if letter in choices:
            print("That letter is already guessed, choose another letter!")
            return self.guess_letter(choices)
        elif len(letter) > 1:
            print("You can only guess one letter at a time!")
            return self.guess_letter(choices)
        elif letter not in "abcdefghijklmnopqrstuvwxyz":
            print("You can only guess letters!")
            return self.guess_letter(choices)
        else:
            choices.append(letter)
            return letter
