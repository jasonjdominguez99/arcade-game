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
class StartMenu(tk.Canvas):
    def __init__(self, master, w, h):
        tk.Canvas.__init__(self, master, width=w, height=h)
        self.master = master

        self.create_start_button(self.master)

    
    def create_start_button(self, window):
        # window.columnconfigure(0, weight=1, minsize=75)
        # window.rowconfigure([0, 1], weight=1, minsize=50)

        start_button = tk.Button(
            self,
            text="S T A R T",
            command = lambda: window.load_page("Game")
        )
        # start_button.pack(side="bottom")
        start_button.place(relx=0.5, rely=0.5, anchor="c")
