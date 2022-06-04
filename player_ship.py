# player_ship.py
# 
# source code relating to the player's
# ship class
# 
# author: Jason Dominguez
# date: 2022-06-03

# imports
import math


# class definitions
class PlayerShip():
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = 10
        self.height = 20

        self.max_speed = 5
        self.speed = 1
        self.direction = 0          # direction in deg from upward


    def draw(self):
        center_coords = (self.canvas.master.width/2, self.canvas.master.height/2)
        coords = [
            center_coords[0] - self.width/2, center_coords[1] + self.height/2,
            center_coords[0] + self.width/2, center_coords[1] + self.height/2,
            center_coords[0], center_coords[1] - self.height/2
        ]
        self.position = coords
        self.player_ship = self.canvas.create_polygon(
            self.position, outline="white", fill="black"
        )

        self.canvas.pack()

    def rotate(self, event):
        if event.keysym == "Right":
            angle = 5
        elif event.keysym == "Left":
            angle = -5

        rad_angle = math.radians(angle)
        sin_val = math.sin(rad_angle)
        cos_val = math.cos(rad_angle)

        x_center = sum([
            x for i, x in enumerate(self.position) if i%2 == 0 
        ]) / 3
        y_center = sum([
            y for i, y in enumerate(self.position) if i%2 == 1 
        ]) / 3

        # TODO: center ship coords, rotate coords, shift coords by center coords and reassign self.position
        

    def move_forward(self, event):
        print(event.keysym)
        self.position[1] -= 1
        self.position[3] -= 1
        self.position[4] -= 1

        self.canvas.move(
            self.player_ship, 0, -1
        )
        # print("Ship moved forward")
    