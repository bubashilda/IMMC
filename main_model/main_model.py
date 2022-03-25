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
        self.local_list_of_agents = [0] * long # список с агентами, находящимися на дороге
        self.out_list = out_list # массив с координатами выхода


    def act():
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
        self.number = number
        self.position = [0, 0, 0] # x, y, z
        self.long = random.choice([2, 3, 4]) # не точно (хз)
        self.speed = [1, 2, 3, 4] # не точно (хз)
        self.time_to_sit = random.choice([2, 3, 4, 5, 6, 7, 8, 9]) # не точно (хз)
        self.condition = 0  # 0 - идёт, 1 - садится, 2 - сидит


    def move(self):
        global list_of_roads
        list_of_roads[self.position[0]][self.position[1]][self.position[2]]


    def get_last_point(self):
        return (self.position[1] - self.long)


def make_outs_list_1():
    out_list = []
    for i in range(0, 4):
        out_list.append(seats_width * 3 + seats_width * 2 * i + road_width * i)
    return out_list


def make_out_list_2():
    out_list = []
    for i in range(0, 14):
        out_list.append((seats_length + distance_between_seats) * i)
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



for iteration in range(0, 10):
    build_for_flying_wing()
    sat_down = 0
    on_board_now = 0
    list_of_passengers.append(passenger(on_board_now))
    on_board_now += 1

    ambition_list =


    with open("main_model_out/out_of_iteration_" + str(iteration) + ".csv", "w") as f:
        while (sat_down != len(ambition_list)):
            for i in range(0, len(list_of_roads[0])):
                list_of_roads[0][i].act()
            for i in range(0, len(list_of_roads[1])):
                list_of_roads[1][i].act()
