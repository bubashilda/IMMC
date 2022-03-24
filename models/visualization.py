from tkinter import *
from random import *
import time


class model(Frame):
    def __init__(self, q):
        super().__init__()
        self.get_graphics(q)


    def get_graphics(self, q):

        self.master.title("самолётик")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self, width=1450, height=310, bg="bisque")

        x_help = 15
        y_help = 15
        for x in range(0, len(q)):
            for y in range(0, 7):
                if (q[x][y] == "0"):
                    canvas.create_rectangle(
                    x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                    outline="BurlyWood", fill="Red")

                elif (q[x][y] == "1"):
                    canvas.create_rectangle(
                    x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                    outline="BurlyWood", fill="Blue")

                elif (q[x][y] == "2"):
                    canvas.create_rectangle(
                    x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                    outline="BurlyWood", fill="Green")

                else:
                    if (y == 3):
                        canvas.create_rectangle(
                        x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                        outline="BurlyWood", fill="Grey")

                    else:
                        canvas.create_rectangle(
                        x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                        outline="BurlyWood", fill="Azure3")

        canvas.pack(fill=BOTH, expand=1)


root = Tk()
root.geometry("1500x350" + "+" + str(10) + "+" + str(50))
root.title("симулятор заразы")
root.configure(bg='Snow')
root.resizable(width=False, height=False)

f = open("data/simple_model_out/out_of_iteration_0.csv", "r").readlines()
for i in range(0, len(f)):
    q = []
    for j in range(0, 34):
        w = []
        for k in range(0, 7):
            w.append(f[i][7 * j + k])
        q.append(w)
    print(q)
    win_1 = model(q).place(x = 20, y = 0)
    root.update()
    time.sleep(0.01)




root.mainloop()
