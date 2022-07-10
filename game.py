# game.py
# 
# source code relating to the game
# 
# author: jason dominguez
# date: 2022-05-29


# imports
import tkinter as tk
from player_ship import PlayerShip
from asteroid import Asteroid
from alien_ship import AlienShip


# class definitions
class Game(tk.Canvas):
    def __init__(self, master, w, h):
        tk.Canvas.__init__(self, master, width=w, height=h, bg="black")
        self.master = master
        
        self.pack()

        ship = PlayerShip(self)
        ship.draw()
        ship.move()

        asteroid = Asteroid(self)
        asteroid.draw()
        asteroid.move()
        asteroid.rotate()

        alien_ship = AlienShip(self)
        alien_ship.draw()
        alien_ship.move()

        self.bind("<Right>", ship.rotate)
        self.bind("<Left>", ship.rotate)
        self.bind("<Up>", ship.accelerate)
        self.bind("<space>", ship.shoot)
        self.focus_set()
