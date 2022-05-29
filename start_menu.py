# start_menu.py
# 
# source code relating to the
# start menu for the arcade game
# 
# author: Jason Dominguez
# date: 2022-05-28

# imports
import tkinter as tk


# class definitions
class StartMenu(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.create_start_button(parent, controller)

    
    def create_start_button(self, window, controller):
        window.columnconfigure(0, weight=1, minsize=75)
        window.rowconfigure([0, 1], weight=1, minsize=50)

        start_button = tk.Button(
            self,
            text="S T A R T",
            command = lambda: controller.load_frame("Game")
        )
        start_button.pack(side="bottom")
