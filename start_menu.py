# start_menu.py
# 
# source code relating to loading the
# start menu for the arcade game
# 
# author: Jason Dominguez
# date: 2022-05-28

# imports
import tkinter as tk


# class definitions
class StartMenu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.place_start_button(parent)

    
    def place_start_button(self, window):
        window.columnconfigure(0, weight=1, minsize=75)
        window.rowconfigure(0, weight=1, minsize=50)

        start_button = tk.Button(text="S T A R T")
        start_button.grid(row=0, column=0)
