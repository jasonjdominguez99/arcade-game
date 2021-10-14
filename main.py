# Main
# 
# Main python file for python arcade-style game
# 
# Author: Jason Dominguez
# Date: 14-10-2021

# Imports
from tkinter import Tk

# Definition of utility functions
def configure_window(window):
    window.geometry("800x600")
    window.configure(background='#b3ffff')
    window.title("G A M E    T I T L E")

# Started implementing main but ran out of time
# come back to this
# def game_loop():
#     num1 = rand(1, 20)


# Definition and execution of main program
def main():
    window = Tk()
    configure_window(window)
    window.mainloop()

if __name__ == "__main__":
    main()