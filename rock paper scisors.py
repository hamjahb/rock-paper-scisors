#!/usr/bin/env python3
# v 0.3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


import random

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class random_player(Player):
    def move(self):
        return random.choice(moves)


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
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.beats(move1, move2)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(f"Player 1 has {self.p1.score} points, Player 2 has {self.p2.score} points.")
        print("Game over!")

    def beats(self, one, two):
        one = self.p1.move()
        two = self.p2.move()
        if one == 'rock' and two == 'scissors':
            self.p1.score += 1
            print("Player 1 wins this round")
        elif one == 'scissors' and two == 'paper':
            self.p1.score += 1
            print("Player 1 wins this round")
        elif one == 'paper' and two == 'rock':
            self.p1.score += 1
            print("Player 1 wins this round")
        elif one == two:
            print("This round is a tie no winner")
        else:
            self.p2.score += 1
            print("Player 2 wins this Round")




if __name__ == '__main__':
    game = Game(random_player(), random_player())
    game.play_game()