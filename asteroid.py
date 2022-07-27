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
# TODO: improve random direction generation by normalizing coord to have screen center as (0, 0)
class Asteroid(Enemy):
    def __init__(self, canvas):
        super().__init__(canvas)

        self.rotation_direction = [-1, 1][random.randint(0, 1)]
        self.rotation_speed = random.randint(1, 5)
        self.orientation = random.randint(0, 359)
        self.speed = random.randint(1, 20)/10.

        rand_n = random.randint(1, 1)
        self.size = "medium"
        self.image_path = fr'images\asteroid-{self.size}-{rand_n}.png'
        self.generate_image()

        self.set_center_coords()

        # method for choosing asteroid direction to move onto screen assumes similar 
        # screen width and height
        coord_total = self.center_coords[0] + self.center_coords[1]
        self.canvas.master.update()
        if coord_total < self.canvas.winfo_width()/2:
            # asteroid starting in first quadrant of screen
            self.direction = random.randint(91, 179)
        elif coord_total < self.canvas.winfo_width() and self.center_coords[0] > self.canvas.winfo_width()/2:
            # second quadrant
            self.direction = random.randint(181, 269)
        elif coord_total < self.canvas.winfo_width() and self.center_coords[0] < self.canvas.winfo_width()/2:
            # fourth quadrant
            self.direction = random.randint(1, 89)
        else:
            # third quadrant
            self.direction = random.randint(271, 359)

    def set_center_coords(self):
        self.canvas.master.update()

        rand_x = random.randint(0, self.canvas.winfo_width())
        x = [0 - self.img_w, rand_x, self.canvas.winfo_width() + self.img_w][random.randint(0, 2)]
        y = (
            [0 - self.img_h, self.canvas.winfo_height() + self.img_h][random.randint(0, 1)]
            if x > 0 and x < self.canvas.winfo_width() else
            random.randint(0, self.canvas.winfo_height())            
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
