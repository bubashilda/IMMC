import random


class passenger():
    def __init__(self, number):
        global ambition_list
        global plane
        random.seed(1)
        self.number = number
        self.ambition = ambition_list[self.number]
        self.position = [0, 3]
        plane[self.position[0]][self.position[1]] = 1
        self.other_time_for_feet = random.choice([1, 2, 3]) # от 1 до 3
        self.other_time_for_bags = random.choice([2, 3, 4]) # от 2 до 4
        self.time_to_stand = 0
        self.speed = 1
        self.condition = 0 # 0 - идёт,  1 - садится, 2 - сидит

    def move(self):
        global plane
        global other_time_list
        global conditions_list
        if (self.condition == 0) and (self.position[0] == self.ambition[0]):
            self.condition = 1
            conditions_list[self.position[0]][self.position[1]] = self.condition
            self.time_to_stand = self.other_time_for_feet + self.other_time_for_bags
            additional_time = 0
            if self.ambition[1] > 3:
                for i in range(4, self.ambition[1], 1):
                    if (other_time_list[self.position[0]][i] != 0):
                        additional_time += other_time_list[self.position[0]][i]
            if self.ambition[1] < 3:
                for i in range(2, self.ambition[1], -1):
                    if (other_time_list[self.position[0]][i] != 0):
                        additional_time += other_time_list[self.position[0]][i]
            self.time_to_stand += additional_time * 2
        elif self.condition == 0:
            if (plane[self.position[0] + 1][self.position[1]] == 0):
                plane[self.position[0]][self.position[1]] = 0
                conditions_list[self.position[0]][self.position[1]] = 3
                self.position[0] += 1
                plane[self.position[0]][self.position[1]] = 1
                conditions_list[self.position[0]][self.position[1]] = self.condition
        elif self.condition == 1:
            self.time_to_stand -= 1
            if self.time_to_stand <= 0:
                plane[self.position[0]][self.position[1]] = 0
                conditions_list[self.position[0]][self.position[1]] = 3
                self.position = self.ambition
                plane[self.position[0]][self.position[1]] = 1
                self.condition = 2
                conditions_list[self.position[0]][self.position[1]] = self.condition
                other_time_list[self.position[0]][self.position[1]] = self.other_time_for_feet

    def get_condition(self):
        return self.condition


def let_one_in():
    global on_board_now
    global passenger_list
    global plane
    if plane[0][3] == 0 and on_board_now < len(ambition_list):
        passenger_list.append(passenger(on_board_now))
        on_board_now += 1


def sort_random(n):
    global ambition_list
    global number_of_seats
    ambition_list = []
    for i in range(1, number_of_seats + 1):
        for j in range(0, 7):
            if j == 3:
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
            if j == 3:
                continue
            ambition_list.append([i, j])
    random.shuffle(ambition_list)
    ambition_list = ambition_list[0: int(number_of_seats * 6 * n)]

    parts = [[], [], []]
    for i in range(0, len(ambition_list)):
        if ambition_list[i][0] <= 11:
            parts[0].append(ambition_list[i])
        elif ambition_list[i][0] <= 22:
            parts[1].append(ambition_list[i])
        elif ambition_list[i][0] <= 33:
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
            if j == 3:
                continue
            ambition_list.append([i, j])
    random.shuffle(ambition_list)
    ambition_list = ambition_list[0: int(number_of_seats * 6 * n)]
    parts = [[], [], []]
    for i in range(0, len(ambition_list)):
        if ambition_list[i][1] == 0 or ambition_list[i][1] == 6:
            parts[0].append(ambition_list[i])

        if ambition_list[i][1] == 1 or ambition_list[i][1] == 5:
            parts[1].append(ambition_list[i])

        if ambition_list[i][1] == 2 or ambition_list[i][1] == 4:
            parts[2].append(ambition_list[i])
    random.shuffle(parts[0])
    random.shuffle(parts[1])
    random.shuffle(parts[2])
    ambition_list = (parts[0] + parts[1] + parts[2])


def sort_steffen(n):
    global ambition_list
    global number_of_seats
    ambition_list = []
    g_1 = []
    g_2 = []
    g_3 = []
    g_4 = []
    for i in range(1, number_of_seats + 1, 2):
        g_1.append([i, 0])
        g_1.append([i, 1])
        g_1.append([i, 2])

        g_2.append([i, 4])
        g_2.append([i, 5])
        g_2.append([i, 6])
    for i in range(2, number_of_seats + 1, 2):
        g_3.append([i, 0])
        g_3.append([i, 1])
        g_3.append([i, 2])

        g_4.append([i, 4])
        g_4.append([i, 5])
        g_4.append([i, 6])
    random.shuffle(g_1)
    random.shuffle(g_2)
    random.shuffle(g_3)
    random.shuffle(g_4)
    ambition_list = g_1 + g_2 + g_3 + g_4


def sort_piramidka(n):
    global ambition_list
    global number_of_seats
    ambition_list = []
    g_1 = []
    g_2 = []
    g_3 = []
    g_4 = []
    g_5 = []
    for i in range(1, number_of_seats + 1):
        for j in range(0, 7):
            if i >= 13 and (j == 0 or j == 6):
                g_1.append([i, j])
            elif (i >= 6 and i <= 12 and (j == 0 or j == 6)) or (i >= 13 and i <= 33 and (j == 1 or j == 5)):
                g_2.append([i, j])
            elif (i >= 1 and i <= 5 and (j == 0 or j == 6)) or (i >= 6 and i <= 22 and (j == 1 or j == 5)):
                g_3.append([i, j])
            elif (i >= 1 and i <= 5 and (j == 1 or j == 5)) or (i >= 22 and i <= 33 and (j == 2 or j == 4)):
                g_4.append([i, j])
            elif i <= 21 and (j == 2 or j == 4):
                g_5.append([i, j])
    random.shuffle(g_1)
    random.shuffle(g_2)
    random.shuffle(g_3)
    random.shuffle(g_4)
    random.shuffle(g_5)
    ambition_list = g_1 + g_2 + g_3 + g_4 + g_5


def sort_steffen_and_group(n):
    global ambition_list
    global number_of_seats
    ambition_list = []
    g_1 = []
    g_2 = []
    g_3 = []
    g_4 = []
    for i in range(1, number_of_seats + 1, 2):
        g_1.append([i, 0])
        g_1.append([i, 1])
        g_1.append([i, 2])

        g_2.append([i, 4])
        g_2.append([i, 5])
        g_2.append([i, 6])
    for i in range(2, number_of_seats + 1, 2):
        g_3.append([i, 0])
        g_3.append([i, 1])
        g_3.append([i, 2])

        g_4.append([i, 4])
        g_4.append([i, 5])
        g_4.append([i, 6])
    random.shuffle(g_1)
    random.shuffle(g_2)
    random.shuffle(g_3)
    random.shuffle(g_4)
    ambition_list = g_1 + g_2 + g_3 + g_4


for iteration in range(0, 10):
    number_of_seats = 33
    plane = [] # список с координатами
    for i in range(0, number_of_seats + 1):
        plane.append([0, 0, 0, 0, 0, 0, 0]) # проход с индексом 0
    other_time_list = []
    for i in range(0, number_of_seats + 1):
        other_time_list.append([0, 0, 0, 0, 0, 0, 0])
    conditions_list = []
    for i in range(0, number_of_seats + 1):
        conditions_list.append([3, 3, 3, 3, 3, 3, 3])
    ambition_list = []
    #################################
    # Выбор метода сортировки condition_list
    # sort_random(1)
    # sort_sections(1, 3, 2, 1)
    # sort_windows(0.3)
    sort_piramidka(0.3)
    # sort_steffen(0.3)
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
            # Файловый вывод
            #f.write(str(step_now) + ";" + str(sat_down_now) + "\n")
            let_one_in()
            sat_down_step_forward = 0
            for i in range(0, len(passenger_list)):
                passenger_list[i].move()
                if (passenger_list[i].get_condition() == 2):
                    sat_down_step_forward += 1
            if (sat_down_step_forward != sat_down_now):
                #print(sat_down_step_forward)
                pass
            step_now += 1
            sat_down_now = sat_down_step_forward
            # f.write(str(step_now) + ";" + str(sat_down_now) + "\n")
            # Вывод результата в файл
            s = ""
            for i in range(0, 34):
                for j in range(0, 7):
                    s += str(conditions_list[i][j])
            f.write(s + "\n")
