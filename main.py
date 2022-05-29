# main
# 
# main python file for python arcade-style game
# 
# author: Jason Dominguez
# date: 2021-10-14

# imports
import tkinter as tk
from start_menu import StartMenu


# class definitions
class AsteroidsGame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure_window(parent)

        self.frames = {
            "start-menu": StartMenu(self.parent)
        }

        self.loadframe("start-menu")


    def configure_window(self, window):
        window.geometry("800x600")
        window.title("A  S  T  E  R  O  I  D  S")

    
    def loadframe(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    


# definition and execution of main program
def main():
    window = tk.Tk()
    AsteroidsGame(window)
    window.mainloop()

if __name__ == "__main__":
    main()