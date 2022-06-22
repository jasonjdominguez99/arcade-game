# projectile.py
# 
# source code relating to projectiles which
# can be fired at enemy objects by the player ship
# 
# author: jason dominguez
# date: 2022-06-06


# imports
import math


# class definition
# TODO: draw projectile as line on canvas
# TODO: control motion, speed etc. of projectile
# TODO: check for collision with enemy object
class Projectile():
    def __init__(self, canvas, ship_coords, ship_direction):
        self.canvas = canvas
        self.length = 10
        self.speed = 2
        self.direction = ship_direction

        self.set_initial_position(ship_coords)
        

    def set_initial_position(self, ship_coords):
        x1, y1 = ship_coords[4], ship_coords[5]

        rad_angle = math.radians(self.direction)
        x2 = x1 + self.length*math.sin(rad_angle)
        y2 = y1 + self.length*math.cos(rad_angle)

        self.coords = [x1, y1, x2, y2]