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
# TODO: check for collision with enemy object
# TODO: create different types of projectiles using inheritance
class Projectile():
    def __init__(self, canvas, ship_coords, ship_direction,
                 ship_speed, ship_max_speed):
        self.canvas = canvas
        self.length = 10
        self.speed = ship_speed + ship_max_speed
        self.direction = ship_direction

        self.set_initial_position(ship_coords)

        self.projectile = self.canvas.create_line(
            self.coords, fill="white", width=3
        )
        

    def set_initial_position(self, ship_coords):
        x1, y1 = ship_coords[4], ship_coords[5]

        rad_angle = math.radians(self.direction)
        x2 = x1 + self.length*math.sin(rad_angle)
        y2 = y1 - self.length*math.cos(rad_angle)

        self.coords = [x1, y1, x2, y2]


    def draw(self):
        self.canvas.pack()


    def move(self):
        coords = self.coords
    
        rad_angle = math.radians(self.direction)

        x_increase = self.speed*math.sin(rad_angle)
        y_increase = self.speed*math.cos(rad_angle)

        self.coords[0] += x_increase
        self.coords[1] -= y_increase
        self.coords[2] += x_increase
        self.coords[3] -= y_increase

        self.canvas.coords(
            self.projectile,
            self.coords[0], self.coords[1],
            self.coords[2], self.coords[3]
        )

        self.canvas.after(10, self.move)
