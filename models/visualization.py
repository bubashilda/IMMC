from tkinter import *
from random import *
import time


class cemetery(Frame):
    def __init__(self, q):
        super().__init__()
        self.get_graphics(q)


    def get_graphics(self, q):

        self.master.title("симулятор заразы")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self, width=150, height=700, bg="bisque")

        x_help = 10
        y_help = 10
        for y in range(0, len(q)):
            for x in range(0, 7):
                if (q[y][x] == "0"):
                    canvas.create_rectangle(
                    x_help + x * 20, y_help + y * 20, x_help + x * 20 + 15, y_help + y * 20 + 15,
                    outline="BurlyWood", fill="Green")
                else:
                    canvas.create_rectangle(
                    x_help + x * 20, y_help + y * 20, x_help + x * 20 + 15, y_help + y * 20 + 15,
                    outline="BurlyWood", fill="Red")


        canvas.pack(fill=BOTH, expand=1)


root = Tk()
root.geometry("200x700" + "+" + str(10) + "+" + str(50))
root.title("симулятор заразы")
root.configure(bg='Snow')
root.resizable(width=False, height=False)

f = open("data/simple_model_out/out_of_iteration_0.csv", "r").readlines()
for i in range(0, len(f)):
    q = []
    for j in range(0, 33):
        w = []
        for k in range(0, 7):
            w.append(f[i][7 * j + k])
        q.append(w)
    print(q)
    win_1 = cemetery(q).place(x = 20, y = 20)
    root.update()
    time.sleep(0.01)




root.mainloop()
