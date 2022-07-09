# enemies.py
# 
# source code relating to storage, generation and
# management of enemies in the game
# 
# author: jason dominguez
# date: 2022-07-09


# imports


# class definition
# TODO: Add function which generates enemies
# TODO: Make generation generate alien ships once player score reach certain thresholds
class Enemies():
    def __init__(self, player):
        self.canvas = player.canvas
        self.player = player
        self.enemies = []

    def generate(self):
        pass