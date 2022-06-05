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
        self.rotation_speed = 15
        self.direction = 0          # direction in deg from upward


    def draw(self):
        center_coords = (self.canvas.master.width/2, self.canvas.master.height/2)
        coords = [
            center_coords[0] - self.width/2, center_coords[1] + self.height/3,
            center_coords[0] + self.width/2, center_coords[1] + self.height/3,
            center_coords[0], center_coords[1] - 2*self.height/3
        ]
        self.position = coords
        self.player_ship = self.canvas.create_polygon(
            self.position, outline="white", fill="black"
        )

        self.canvas.pack()

    
    def get_center_coords(self):
        x_center = sum([
            x for i, x in enumerate(self.position) if i%2 == 0 
        ]) / 3
        y_center = sum([
            y for i, y in enumerate(self.position) if i%2 == 1 
        ]) / 3

        return (x_center, y_center)


    def rotate(self, event):
        if event.keysym == "Right":
            self.direction += self.rotation_speed
        else:
            self.direction -= self.rotation_speed

        x_center, y_center = self.get_center_coords()

        rad_angle = math.radians(self.direction)
        phi = math.atan((self.width/2)/(self.height/3))
        theta = math.pi/2 - rad_angle - phi
        r = math.sqrt((self.height/3)**2 + (self.width/2)**2)
        coords = [
            x_center + (2*self.height/3)*math.sin(rad_angle), y_center - (2*self.height/3)*math.cos(rad_angle),
            x_center - r*math.cos(theta), y_center + r*math.sin(theta),
            x_center + r*math.sin(phi - rad_angle), y_center + r*math.cos(phi - rad_angle)
        ]

        self.position = coords
        self.canvas.coords(
            self.player_ship,
            self.position[0], self.position[1],
            self.position[2], self.position[3],
            self.position[4], self.position[5]
        )
        
        # print("Ship rotated")
        # print(event.keysym)
        

    def move_forward(self, event):
        print(event.keysym)
        self.position[1] -= 1
        self.position[3] -= 1
        self.position[4] -= 1

        self.canvas.move(
            self.player_ship, 0, -1
        )
        # print("Ship moved forward")
    