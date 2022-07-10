# enemy.py
# 
# source code relating to base class for enemy objects
# 
# author: jason dominguez
# date: 2022-06-23


# imports
from PIL import ImageTk
import math


# class definition
# TODO: implement collision dynamics and
class Enemy():
    def __init__(self, canvas):
        self.canvas = canvas

        self.center_coords = None
        self.speed = None
        self.direction = None
        self.orientation = None
        
        self.tk_img = None
        self.img = None
        self.object = None

    def generate_image(self):
        self.tk_img = ImageTk.PhotoImage(self.img.rotate(self.orientation))

    def draw(self):
        self.object = self.canvas.create_image(
            self.center_coords[0], self.center_coords[1],
            image=self.tk_img
        )
        self.canvas.pack()

    def move(self):
        rad_angle = math.radians(self.direction)

        x_increase = self.speed*math.sin(rad_angle)
        y_increase = self.speed*math.cos(rad_angle)

        self.center_coords[0] += x_increase
        self.center_coords[1] -= y_increase

        self.canvas.coords(
            self.object,
            self.center_coords[0], self.center_coords[1]
        )

        self.canvas.after(10, self.move)
