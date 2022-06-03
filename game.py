# game.py
# 
# source code relating to the game
# 
# author: Jason Dominguez
# date: 2022-05-29

# imports
import tkinter as tk


# class definitions
class Game(tk.Canvas):
    def __init__(self, master, w, h):
        tk.Canvas.__init__(self, master, width=w, height=h, bg="black")
        self.master = master
        
        self.pack()
        # self.pack(fill="both", expand=True)

        size = 10
        ship = self.create_oval(
            self.master.height/2 - size/2, self.master.width/2 - size/2,
            self.master.height/2 + size/2, self.master.width/2 + size/2,
            outline="white"
        )

        self.pack()



    # def __init__(self, parent, controller, *args, **kwargs):
    #     tk.Frame.__init__(self, parent, *args, **kwargs)
    #     self.parent = parent
    #     self.controller = controller

    #     print(self.winfo_height())
    #     canvas = tk.Canvas(self, width=self.winfo_width(), height=self.winfo_height(), bg="black")
    #     canvas.pack()
    #     # canvas.pack(fill="both", expand=True)

    #     window_h = canvas.winfo_height()
    #     window_w = canvas.winfo_width()
    #     ship_h = 20
    #     ship_w = 10
    #     coords = [
    #         window_w/2 - ship_w/2, window_h/2 + ship_h/2,
    #         window_w/2 + ship_w/2, window_h/2 + ship_h/2,
    #         window_w/2, window_h/2 - ship_h/2
    #     ]
    #     print(window_h)
    #     print(window_w)
    #     print(coords)
    #     player = canvas.create_polygon(coords, outline="white", fill="black")
    #     canvas.pack(fill="both", expand=True)

        # self.create_start_button(parent, controller)

    
    # def create_start_button(self, window, controller):
    #     window.columnconfigure(0, weight=1, minsize=75)
    #     window.rowconfigure([0, 1], weight=1, minsize=50)

    #     start_button = tk.Button(
    #         self,
    #         text="E X I T",
    #         command = lambda: controller.load_frame("StartMenu")
    #     )
    #     start_button.pack(side="bottom")
