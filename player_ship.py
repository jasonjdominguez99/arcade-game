# player_ship.py
# 
# source code relating to the player's
# ship class
# 
# author: Jason Dominguez
# date: 2022-06-03

# imports


# class definitions
class PlayerShip():
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = 10
        self.height = 20

        # key bindings
        # self.canvas.bind("<KeyPress-W>", self.move_forward)


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

    def move_forward(self, event):
        # print(event.keysym)
        self.position[1] -= 1
        self.position[3] -= 1
        self.position[4] -= 1

        self.canvas.move(
            self.player_ship, 0, -1
        )
        # print("Ship moved forward")
    