# enemies.py
# 
# source code relating to storage, generation and
# management of enemies in the game
# 
# author: jason dominguez
# date: 2022-07-09


# imports


# class definition
# TODO: add function which generates enemies
# TODO: make generation generate alien ships only once player score reach certain thresholds
# TODO: destroy alien ship when goes off screen
# TODO: destroy asteroid upon moving off screen
# TODO: implement splitting large asteroids into samller ones upon collision
class Enemies():
    def __init__(self, player):
        self.canvas = player.canvas
        self.player = player
        self.enemies = []

    def generate(self):
        pass