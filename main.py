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
        self.width = 500
        self.height = 500

        self.configure_window()

        # self.container = tk.Frame(
        #     self,
        #     height=self.height,
        #     width=self.width
        # )
        # self.configure_container()

        self.pages = {}
        
        frame = StartMenu(master=self, w=self.width, h=self.height)
        self.pages["StartMenu"] = frame
        # frame.grid(row=0, column=0, sticky="nsew")

        game_page = Game(master=self, w=self.width, h=self.height)
        self.pages["Game"] = game_page
        # game_page.grid(row=0, column=0, sticky="nsew")

        self.load_page("StartMenu")


    def configure_window(self):
        self.title("A  S  T  E  R  O  I  D  S")

        self.resizable(False, False)

        # place window in the center of the screen
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w//2) - (self.width//2)
        y = (screen_h//2) - (self.height//2)
        self.geometry(
            "{}x{}+{}+{}".format(self.width, self.height, x, y))


    # def configure_container(self):
    #     self.container.pack(side="top", fill="both", expand=True)
    #     self.container.grid_columnconfigure(0, weight=1)
    #     self.container.grid_rowconfigure(0, weight=1)

    
    def load_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
            # page.grid_remove()
        page = self.pages[page_name]
        # page.grid()
        page.pack()
        # page.tkraise()
        # print("Loaded: " + page_name)


# definition and execution of main program
def main():
    game = AsteroidsGame()
    game.mainloop()

if __name__ == "__main__":
    main()
