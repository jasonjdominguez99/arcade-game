# enemy.py
# 
# source code relating to enemy objects, including
# asteroids and alien space ships
# 
# author: jason dominguez
# date: 2022-06-23


# imports
# from tkinter import BitmapImage, PhotoImage
from PIL import ImageTk, Image
import math
import random


# class definitions
# TODO: create enemy object base class
# TODO: create asteroid class using inheritance
# TODO: implement collision dynamics and splitting large asteroids into samller ones
# TODO: create alien ship class using inheritance
class Asteroid():
    def __init__(self, canvas):
        self.canvas = canvas

        self.rotation_direction = [-1, 1][random.randint(0, 1)]
        # self.rotation_speed = random.randint(1, 10)
        self.rotation_speed = 50
        self.orientation = random.randint(0, 359)
        self.direction = random.randint(0, 359)
        self.speed = random.randint(1, 20)/10.

        # rand_n = random.randint(1, 1)
        rand_n = 1
        # self.image_path = fr'images\asteroid-medium-{rand_n}.xbm'
        self.image_path = fr'images\asteroid-medium-{rand_n}.png'

        self.set_center_coords()
        self.img = Image.open(self.image_path)
        self.generate_image()


    def generate_image(self):
        self.tk_img = ImageTk.PhotoImage(self.img.rotate(self.orientation))

        # self.img = BitmapImage(file=self.image_path, background='white')
        # # self.img = PhotoImage(file=self.image_path)
        # self.img.img = self.img


    def set_center_coords(self):
        self.canvas.master.update()
        rand_x = random.randint(0, self.canvas.winfo_width())
        rand_y = random.randint(0, self.canvas.winfo_height())
        self.center_coords = [rand_x, rand_y]


    def draw(self):
        self.asteroid = self.canvas.create_image(
            self.center_coords[0], self.center_coords[1],
            image=self.tk_img
        )
        self.canvas.pack()

    
    def rotate(self):
        self.orientation += self.rotation_direction*self.rotation_speed
        self.generate_image()
        self.asteroid = self.canvas.create_image(
            self.center_coords[0], self.center_coords[1],
            image=self.tk_img
        )
        self.canvas.after(10, self.rotate)


    def move(self):
        rad_angle = math.radians(self.direction)

        x_increase = self.speed*math.sin(rad_angle)
        y_increase = self.speed*math.cos(rad_angle)

        self.center_coords[0] += x_increase
        self.center_coords[1] -= y_increase

        self.canvas.coords(
            self.asteroid,
            self.center_coords[0], self.center_coords[1]
        )

        self.canvas.after(10, self.move)
