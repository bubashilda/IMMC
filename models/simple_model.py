import random


class passenger():
    '''класс пасажир'''
    def __init__(self, number):
        global ambition_list
        global plane

        self.number = number
        self.ambition = ambition_list[self.number]
        self.position = [0, 3]
        plane[self.position[0]][self.position[1]] = 1

        self.other_time = 3
        self.speed = 1

        self.condition = 0 # 0 - идёт 1 - садится 2 - сидит


    def move(self):
        global plane

        if ((self.condition == 0) and (self.position[0] == self.ambition[0])):
            self.condition = 1

            additional_time = 0
            if (self.ambition[1] > 3):
                for i in range(4, self.ambition[1], 1):
                    if (plane[self.position[0]][i] != 0):
                        additional_time += 1

            if (self.ambition[1] < 3):
                for i in range(2, self.ambition[1], -1):
                    if (plane[self.position[0]][i] != 0):
                        additional_time += 1

            self.other_time += additional_time * 4

        elif (self.condition == 0):
            if (plane[self.position[0] + 1][self.position[1]] == 0):
                plane[self.position[0]][self.position[1]] = 0
                self.position[0] += 1
                plane[self.position[0]][self.position[1]] = 1

        elif (self.condition == 1):
            self.other_time -= 1

            if (self.other_time <= 0):
                plane[self.position[0]][self.position[1]] = 0
                self.position = self.ambition
                plane[self.position[0]][self.position[1]] = 1
                self.condition = 2

    def get_condition(self):
        return self.condition


def let_one_in():
    global on_board_now
    global passenger_list
    global plane

    if ((plane[0][3] == 0) and (on_board_now < len(ambition_list))):
        passenger_list.append(passenger(on_board_now))
        on_board_now += 1


def sort_random(n):
    global ambition_list
    global number_of_seats

    ambition_list = []
    for i in range(1, number_of_seats + 1):
        for j in range(0, 7):
            if (j == 3):
                continue
            ambition_list.append([i, j])
    random.shuffle(ambition_list)
    ambition_list = ambition_list[0: int(number_of_seats * 6 * n)]


def sort_sections(n, p1, p2, p3):
    global ambition_list
    global number_of_seats

    ambition_list = []
    for i in range(1, number_of_seats + 1):
        for j in range(0, 7):
            if (j == 3):
                continue
            ambition_list.append([i, j])
    random.shuffle(ambition_list)
    ambition_list = ambition_list[0: int(number_of_seats * 6 * n)]

    parts = [[], [], []]
    for i in range(0, len(ambition_list)):
        if (ambition_list[i][0] <= 11):
            parts[0].append(ambition_list[i])

        elif (ambition_list[i][0] <= 22):
            parts[1].append(ambition_list[i])

        elif (ambition_list[i][0] <= 33):
            parts[2].append(ambition_list[i])

    random.shuffle(parts[0])
    random.shuffle(parts[1])
    random.shuffle(parts[2])

    ambition_list = (parts[p1 - 1] + parts[p2 - 1] + parts[p3 - 1])


def sort_windows(n):
    global ambition_list
    global number_of_seats

    ambition_list = []
    for i in range(1, number_of_seats + 1):
        for j in range(0, 7):
            if (j == 3):
                continue
            ambition_list.append([i, j])
    random.shuffle(ambition_list)
    ambition_list = ambition_list[0: int(number_of_seats * 6 * n)]

    parts = [[], [], []]
    for i in range(0, len(ambition_list)):
        if (ambition_list[i][1] == 0 or ambition_list[i][1] == 6):
            parts[0].append(ambition_list[i])

        if (ambition_list[i][1] == 1 or ambition_list[i][1] == 5):
            parts[1].append(ambition_list[i])

        if (ambition_list[i][1] == 2 or ambition_list[i][1] == 4):
            parts[2].append(ambition_list[i])

    random.shuffle(parts[0])
    random.shuffle(parts[1])
    random.shuffle(parts[2])

    ambition_list = (parts[0] + parts[1] + parts[2])


for iteration in range(0, 11):
    number_of_seats = 33

    plane = [] # список с координатами
    for i in range(0, number_of_seats + 1):
        plane.append([0, 0, 0, 0, 0, 0, 0]) # проход с индексом 0

    ambition_list = []

    #################################
    #sort_random(1)
    #sort_sections(0.8, 1, 3, 2)
    sort_windows(1)
    ################################


    on_board_now = 0

    passenger_list = []

    passenger_list.append(passenger(on_board_now))
    on_board_now += 1

    sat_down_now = 0
    sat_down_step_forward = 0

    step_now = 1
    with open("data/simple_model_out/out_of_iteration_" + str(iteration) + ".csv", "w") as f:
        while (sat_down_now != len(ambition_list)):
            #f.write(str(step_now) + ";" + str(sat_down_now) + "\n")

            let_one_in()
            sat_down_step_forward = 0
            for i in range(0, len(passenger_list)):
                passenger_list[i].move()
                if (passenger_list[i].get_condition() == 2):
                    sat_down_step_forward += 1

            if (sat_down_step_forward != sat_down_now):
                print(sat_down_step_forward)

            step_now += 1

            sat_down_now = sat_down_step_forward


            #f.write(str(step_now) + ";" + str(sat_down_now) + "\n")


            s = ""
            for i in range(0, 34):
                for j in range(0, 7):
                    s += str(plane[i][j])
            f.write(s + "\n")
