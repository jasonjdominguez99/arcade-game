# player_ship.py
# 
# source code relating to the player's
# ship class
# 
# author: Jason Dominguez
# date: 2022-06-03


# imports
import math
from projectile import Projectile


# class definition
# TODO: make ship lose a life if hits an enemy object
# TODO: add scoring
# TODO: add power ups
# TODO: add acceleration graphics, i.e. fire out of back of ship when accelerating
# TODO: improve motion control
class PlayerShip():
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = 10
        self.height = 20

        self.max_speed = 2
        self.min_speed = 0.5
        self.speed = 0
        self.acceleration = 1
        self.deceleration = 0.01
        self.rotation_speed = 10
        # directions in deg from upward
        self.direction = 0
        self.acc_direction = 0

        self.score = 0

        self.set_initial_position()

        self.player_ship = self.canvas.create_polygon(
            self.position, outline="white", fill="black"
        )


    def set_initial_position(self):
        center_coords = (self.canvas.master.width/2, self.canvas.master.height/2)
        coords = [
            center_coords[0] - self.width/2, center_coords[1] + self.height/3,
            center_coords[0] + self.width/2, center_coords[1] + self.height/3,
            center_coords[0], center_coords[1] - 2*self.height/3
        ]
        self.position = coords


    def draw(self):
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
            x_center - r*math.cos(theta), y_center + r*math.sin(theta),
            x_center + r*math.sin(phi - rad_angle), y_center + r*math.cos(phi - rad_angle),
            x_center + (2*self.height/3)*math.sin(rad_angle), y_center - (2*self.height/3)*math.cos(rad_angle)
        ]

        self.position = [round(coord) for coord in coords]
        self.canvas.coords(
            self.player_ship,
            self.position[0], self.position[1],
            self.position[2], self.position[3],
            self.position[4], self.position[5]
        )
        
        # print("Ship rotated")
        # print(event.keysym)
        

    def accelerate(self, event):
        self.acc_direction = self.direction
        if self.speed < self.max_speed:
            self.speed += self.acceleration

        # print("Ship accelerated")
        # print(event.keysym)


    def decelerate(self):
        if self.speed > self.min_speed:
            self.speed -= self.deceleration
    

    def move(self):
        if self.speed != 0:
            rad_angle = math.radians(self.acc_direction)

            x_increase = self.speed*math.sin(rad_angle)
            y_increase = self.speed*math.cos(rad_angle)

            for i in range(len(self.position)):
                if i%2 == 0:
                    self.position[i] += x_increase
                else:
                    self.position[i] -= y_increase

            # check is ship moves off screen, if so make appear on opposite side of screen
            x_coords = [self.position[i] for i in range(0, len(self.position), 2)]
            y_coords = [self.position[i] for i in range(1, len(self.position), 2)]
            
            self.canvas.master.update()
            if max(x_coords) < 0:
                x_coords = [x + self.canvas.winfo_width()
                            for x in x_coords]
            elif min(x_coords) > self.canvas.winfo_width():
                x_coords = [x - self.canvas.winfo_width()
                            for x in x_coords]
            elif max(y_coords) < 0:
                y_coords = [y + self.canvas.winfo_height()
                            for y in y_coords]
            elif min(y_coords) > self.canvas.winfo_height():
                y_coords = [y - self.canvas.winfo_height()
                            for y in y_coords]

            self.position = [
                x_coords[0], y_coords[0],
                x_coords[1], y_coords[1],
                x_coords[2], y_coords[2]
            ]
                
            self.canvas.coords(
                self.player_ship,
                self.position[0], self.position[1],
                self.position[2], self.position[3],
                self.position[4], self.position[5]
            )

        self.canvas.after(10, self.move)
        self.decelerate()


    def shoot(self, event):
        proj = Projectile(self.canvas, self.position,
                          self.direction, self.speed, self.max_speed)
        proj.draw()
        proj.move()
        