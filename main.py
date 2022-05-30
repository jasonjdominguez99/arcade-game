# main
# 
# main python file for python arcade-style game
# 
# author: jason dominguez
# date: 2021-10-14

# imports
import tkinter as tk
from start_menu import StartMenu
from game import Game


# class definitions
class AsteroidsGame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.configure_window()

        self.frames = {}
        for F in (StartMenu, Game):
            frame_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.load_frame("StartMenu")


    def configure_window(self):
        self.geometry("800x600")
        self.title("A  S  T  E  R  O  I  D  S")

        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

    
    def load_frame(self, frame_name):
        # for frame in self.frames.values():
        #     frame.grid_remove
        frame = self.frames[frame_name]
        # frame.grid()
        frame.tkraise()
        # print("Loaded: " + frame_name)


# definition and execution of main program
def main():
    game = AsteroidsGame()
    game.mainloop()

if __name__ == "__main__":
    main()
