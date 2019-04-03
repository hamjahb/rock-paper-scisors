#!/usr/bin/env python3
# v 0.8
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


import random

class Player:
    def __init__(self):
        self.my_previous_move = random.choice(moves)
        self.their_previous_move = random.choice(moves)
    
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_previous_move = my_move
        self.their_previous_move = their_move

class Random_Player(Player):
    def move(self):
        return random.choice(moves)

class Human_Player(Player):
    def move(self):
        self.hand = input("What will you play? Rock, Paper or Scissors?\n").lower()
        if self.hand in moves:
            return self.hand
        else:
            print("Not a valid move")
            self.move()

class Reflect_Player(Player):
    def move(self):
        return self.their_previous_move


class Cycle_Player(Player):
    #player that cycles based on last play
    def move(self):
        
        n = moves.index(self.my_previous_move)
        if n == 2:
            return moves[0]
        else:
            return moves[n+1]
    

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.beats(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        
    def post_game(self):
        print(f"Final score P1: {self.p1.score}, P2: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print(f"Player 1 Wins with {self.p1.score} points!\n")
        elif self.p1.score < self.p2.score:
            print(f"Player 2 Wins with {self.p2.score} points!\n")
        elif self.p1.score == self.p2.score:
            print("TIE BREAKER ROUND!!")
            self.play_round()
            self.post_game()

    def play_again(self):
        another = input("play another 3 rounds or quit? quit/play?\n").lower()
        if another == "play":
            self.play_game()
        elif another == "quit":
            print("Game over!")        
        else:
            print("invalid command")
            self.play_again

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"P1: {self.p1.score}, P2: {self.p2.score}")
            print(f"Round {round}:")
            self.play_round()
        self.post_game()
        self.play_again()

    def beats(self, move1, move2):
        if move1 == move2:
            print("This round is a tie no winner \n")
        elif move1 == 'rock':
            if move2 == 'scissors':
                self.p1.score += 1
                print("Player 1 wins this round \n")
            else:
                self.p2.score += 1
                print("Player 2 wins this round \n")
        elif move1 == 'scissors':
            if move2 == 'paper':
                self.p1.score += 1
                print("Player 1 wins this round \n")
            else:
                self.p2.score += 1
                print("Player 2 wins this round \n")
        elif move1 == 'paper':
            if move2 == 'rock':
                self.p1.score += 1
                print("Player 1 wins this round\n")
            else:
                self.p2.score += 1
                print("Player 2 wins this round \n")




if __name__ == '__main__':
    game = Game(Random_Player(), Random_Player())
    game.play_game()