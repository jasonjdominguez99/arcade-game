# alien_ship.py
# 
# source code relating to alien ship enemy object
# 
# author: jason dominguez
# date: 2022-07-10


# imports
from enemy import Enemy
from PIL import Image
import random


# class defintion
class AlienShip(Enemy):
    def __init__(self, canvas):
        super().__init__(canvas)

        self.speed = 0.5
        self.direction = [90, 270][random.randint(0, 1)]
        self.orientation = 0

        self.image_path = r'images\alien-ship.png'
        self.generate_image()

        self.set_center_coords()

    def set_center_coords(self):
        self.canvas.master.update()
        x = (
            0 - self.img_w if self.direction == 90
            else self.canvas.winfo_width() + self.img_w
        )
        y = random.randint(0 + self.img_h//2, self.canvas.winfo_height() - self.img_h//2)
        self.center_coords = [x, y]
