# game.py
# 
# source code relating to the game
# 
# author: Jason Dominguez
# date: 2022-05-29

# imports
import tkinter as tk
from player_ship import PlayerShip


# class definitions
class Game(tk.Canvas):
    def __init__(self, master, w, h):
        tk.Canvas.__init__(self, master, width=w, height=h, bg="black")
        self.master = master
        
        self.pack()

        ship = PlayerShip(self)
        ship.draw()

        self.bind("<Right><Left", ship.move_forward)
        self.bind("<Up>w", ship.accelerate)
        self.focus_set()
