# asteroid.py
# 
# source code relating to asteroid enemy object
# 
# author: jason dominguez
# date: 2022-07-09


# imports
from enemy import Enemy
from PIL import Image
import random


# class definition
# TODO: make asteroid start off screen and move onto the screen
# TODO: destroy asteroid upon moving off screen
# TODO: implement splitting large asteroids into samller ones upon collision
class Asteroid(Enemy):
    def __init__(self, canvas):
        super().__init__(canvas)

        self.set_center_coords()

        self.rotation_direction = [-1, 1][random.randint(0, 1)]
        self.rotation_speed = random.randint(1, 5)
        self.orientation = random.randint(0, 359)
        self.direction = random.randint(0, 359)
        self.speed = random.randint(1, 20)/10.

        # rand_n = random.randint(1, 1)
        rand_n = 1
        image_path = fr'images\asteroid-medium-{rand_n}.png'
        self.img = Image.open(image_path)
        self.generate_image()

    def set_center_coords(self):
        self.canvas.master.update()
        x = random.randint(0, self.canvas.winfo_width())
        y = random.randint(0, self.canvas.winfo_height())
        self.center_coords = [x, y]

    def rotate(self):
        self.orientation += self.rotation_direction*self.rotation_speed
        self.generate_image()
        self.object = self.canvas.create_image(
            self.center_coords[0], self.center_coords[1],
            image=self.tk_img
        )
        self.canvas.pack()
        self.canvas.after(20, self.rotate)
