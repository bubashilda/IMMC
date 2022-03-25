import random

list_of_passengers = [] # массив пассажирами
list_of_roads = [[], []] # массив с дорогами, 0 - главные(ая), 1 - длинная
ambition_list = [] # массив с координатами сидений
# все расстояния в дицеметрах (10 см)
road_width = 5 # ширина прохода
seats_width = 6 # ширина кресла
seats_length = 6 #длинна кресла
distance_between_seats = 3 # расстояне между креслами


class road():
    def __init__(self, number, long, out_list):
        self.number = number # индекс текущего элемента в соответствующем массиве
        self.local_list_of_agents = [-1] * long # список с агентами, находящимися на дороге
        self.out_list = out_list # массив с координатами выхода


    def act(self):
        global list_of_passengers
        for i in self.local_list_of_agents:
            list_of_passengers[i].move()


class main_road(road):
    def __init__(self, number, long, outs):
        road.__init__(self, number, long, outs)


    def add_new(self):
        pass


    def remove(self):
        pass


class long_roads(road):
    def __init__(self, number, long, out_list):
        road.__init__(self, number, long, out_list)


class passenger():
    def __init__(self, number):
        global ambition_list
        self.number = number
        self.position = [0, 0, 0] # x, y, z
        self.long = random.choice([2, 3, 4]) # не точно (хз)
        self.speed = random.choice([1, 2, 3, 4]) # не точно (хз)
        self.time_to_sit = random.choice([2, 3, 4, 5, 6, 7, 8, 9]) # не точно (хз)
        self.condition = 0  # 0 - идёт, 1 - садится, 2 - сидит
        self.ambition = ambition_list[self.number]


    def move(self):
        global list_of_roads
        #print(list_of_roads[self.position[0]][self.position[2]].out_list)
        #print(len(list_of_roads[self.position[0]][self.position[2]].local_list_of_agents))
        move_it_to = 0
        for i in range(self.position[2], self.position[2] + self.speed + road_width):
            if (self.position[0] == 0):
                if












    def get_last_point(self):
        return (self.position[1] - self.long)


def make_outs_list_1():
    global seats_width
    global road_width
    out_list = []
    for i in range(0, 4):
        out_list.append(seats_width * 3 + seats_width * 3 * 2 * i + road_width * i - 1)
    return out_list


def make_out_list_2():
    global seats_length
    global distance_between_seats
    out_list = []
    for i in range(0, 14):
        out_list.append((seats_length + distance_between_seats) * i - 1)
    return out_list


def build_for_flying_wing():
    global list_of_roads
    global seats_width
    global road_width
    global seats_length
    global distance_between_seats
    out_list = make_outs_list_1()
    list_of_roads[0].append(main_road(0, seats_width * 3 * 8 + road_width * 4, out_list))
    out_list = make_out_list_2()
    for i in range(0, 4):
        list_of_roads[1].append(long_roads(i, (seats_length + distance_between_seats) * 14, out_list))


def random_ambition_list_for_flying_wing(n):
    global ambition_list
    for i in range(0, 4):
        for j in range(0, 14):
            for k in range(0, 7):
                if k == 3:
                    continue
                if (i == 0 and j >= 11 and k >= 3):
                    continue
                if (i == 3 and j >= 11 and k <= 3):
                    continue
                ambition_list.append([i, j, k])
    random.shuffle(ambition_list)



for iteration in range(0, 10):
    build_for_flying_wing()
    random_ambition_list_for_flying_wing(1)
    sat_down = 0
    on_board_now = 0
    list_of_passengers.append(passenger(on_board_now))
    on_board_now += 1


    with open("main_model_out/out_of_iteration_" + str(iteration) + ".csv", "w") as f:
        while (sat_down != len(ambition_list)):
            for i in range(0, len(list_of_roads[0])):
                list_of_roads[0][i].act()
            for i in range(0, len(list_of_roads[1])):
                list_of_roads[1][i].act()



















#
