from tkinter import *
from random import *
import time


class model(Frame):
    def __init__(self, q):
        super().__init__()
        self.get_graphics(q)


    def get_graphics(self, q):

        self.master.title("Plane")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self, width=1450, height=310, bg="gray80")

        x_help = 15
        y_help = 15
        for x in range(0, len(q)):
            for y in range(0, 7):
                if (q[x][y] == "0"):
                    canvas.create_rectangle(
                    x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                    outline="gray0", fill="salmon")

                elif (q[x][y] == "1"):
                    canvas.create_rectangle(
                    x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                    outline="gray0", fill="cyan4")

                elif (q[x][y] == "2"):
                    canvas.create_rectangle(
                    x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                    outline="gray0", fill="grey52")

                else:
                    if (y == 3):
                        canvas.create_rectangle(
                        x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                        outline="gray80", fill="gray80")

                    else:
                        canvas.create_rectangle(
                        x_help + x * 42, y_help + y * 42, x_help + x * 42 + 35, y_help + y * 42 + 35,
                        outline="gray0", fill="azure")

        canvas.pack(fill=BOTH, expand=1)


root = Tk()
root.geometry("1450x350" + "+" + str(10) + "+" + str(50))
root.title("Plane")
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
    win_1 = model(q).place(x = 20, y = 10)
    root.update()
    time.sleep(0.005)

root.mainloop()
