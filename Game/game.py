#!/usr/bin/env python3
import random
from Game.players import Player, AI_Player, Human_Player
class Hangman:
    def __init__(self, p1:Player, p2:Player, word, chances):
        self.p1 = p1
        self.p2 = p2
        self.word = word
        self.chances = chances
        self.guessed_letters = []

        
        self.intro()
        self.play_the_game()
    def intro(self):
        print("Welcome to Hangman!")
        print(f"I am thinking of a word with {len(self.word)} letters.")
        print(f"can you guess the word in {self.chances} guesses?")

    def display_word(self):        
        for letter in self.word:
            if letter in self.guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
                
        print(f"\n\nChances left: {self.chances}")
    def player_turn(self, player):
        state = True
        print(f"{player.name} turn  ")
        p1_guess = player.guess_letter(self.guessed_letters)
        if p1_guess in self.word:
            print("correct guess")
            self.display_word()
            
            for i in self.word:
                if i not in self.guessed_letters:
                    state = False
            if state == True:
                player.score = 1
                self.game_over()
                
            self.player_turn(player)
        else:
            self.chances-=1
            print("wrong guess")
            self.display_word()
            if self.chances == 0:
                self.game_over()

    def play_the_game(self):

        while self.chances > 0:
            self.player_turn(self.p1)
            
            if self.chances == 0:
                break
            self.player_turn(self.p2)
    

    def game_over(self): 
        if self.chances <= 0:
            print("Game Over")
            print("No one wins the game!!") 
        elif self.p1.score == 1:
            print("Game Over")
            print(f"{self.p1.name} wins the game!!")            
        elif self.p2.score == 1:
            print("Game Over")
            print(f"{self.p2.name} wins the game!!")

        else:
            print("Error")
        exit()
    
def main():
    p1 = Human_Player("Human")
    p2 = AI_Player("Computer")
    words = ["house", "car", "program", "problem", "creative", "sphinx", "python", "maximum"]

    hangman = Hangman(p1, p2, random.choice(words),10)
    hangman.play_the_game()
