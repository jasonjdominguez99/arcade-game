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
class Asteroid(Enemy):
    def __init__(self, canvas):
        super().__init__(canvas)

        self.set_center_coords()

        self.rotation_direction = [-1, 1][random.randint(0, 1)]
        self.rotation_speed = random.randint(1, 5)
        self.orientation = random.randint(0, 359)
        self.speed = random.randint(1, 20)/10.

        if self.center_coords[0] < 0:
            self.direction = random.randint(181, 359)
        else:
            self.direction = random.randint(0, 180)

        rand_n = random.randint(1, 1)
        self.size = "medium"
        self.image_path = fr'images\asteroid-{self.size}-{rand_n}.png'
        self.generate_image()

    def set_center_coords(self):
        self.canvas.master.update()

        rand_x = random.randint(1, self.canvas.winfo_width())
        x = [0, rand_x][random.randint(0, 1)]
        y = (
            random.randint(0, self.canvas.winfo_height())
            if x == 0 else 0
        )
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
