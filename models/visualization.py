from tkinter import *
from random import *


class cemetery(Frame):
    def __init__(self):
        super().__init__()
        self.get_graphics()


    def get_graphics(self):

        global list_of_agents

        self.master.title("симулятор заразы")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self, width=755, height=355, bg="bisque")

        canvas.pack(fill=BOTH, expand=1)

root = Tk()
root.geometry("800x400" + "+" + str(10) + "+" + str(50))
root.title("симулятор заразы")
root.configure(bg='Snow')
root.resizable(width=False, height=False)

win_1 = cemetery().place(x = 20, y = 20)

f = oopen()







root.mainloop()
