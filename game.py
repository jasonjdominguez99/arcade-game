# game.py
# 
# source code relating to the game
# 
# author: Jason Dominguez
# date: 2022-05-29

# imports
import tkinter as tk


# class definitions
class Game(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        canvas = tk.Canvas(self, bg="black")
        canvas.pack(fill="both", expand=True)

        points = [400, 300, 410, 300, 405, 320]
        canvas.create_polygon(points, outline="white", fill="black")
        canvas.pack(fill="both", expand=True)

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
