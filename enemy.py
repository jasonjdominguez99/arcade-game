# enemy.py
# 
# source code relating to enemy objects, including
# asteroids and alien space ships
# 
# author: jason dominguez
# date: 2022-06-23


# imports
from tkinter import BitmapImage, PhotoImage
from PIL import Image, ImageTk


# class definitions
# TODO: create enemy object base class
# TODO: create asteroid class using inheritance
# TODO: implement collision dynamics and splitting large asteroids into samller ones
# TODO: create alien ship class using inheritance
class Asteroid():
    def __init__(self, canvas):
        self.canvas = canvas
        self.image_path = r'images\asteroid-medium-1.xbm'
        # self.image_path = r'images\asteroid-medium-1.png'

        self.set_center_coords()

        self.img = BitmapImage(file=self.image_path, background='white')
        # self.img = PhotoImage(file=self.image_path)
        self.img.img = self.img


    def set_center_coords(self):
        self.center_coords = [50, 50]


    def draw(self):
        self.asteroid = self.canvas.create_image(
            self.center_coords[0], self.center_coords[1],
            image=self.img
        )
        self.canvas.pack()
