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
    '''общий объект дорога'''
    def __init__(self, number, long, out_list):
        self.number = number # индекс текущего элемента в соответствующем массиве
        self.local_list_of_agents = [-1] * long # список с агентами, находящимися на дороге
        self.out_list = out_list # массив с координатами выхода
        self.moved = []


    def act(self):
        global list_of_passengers
        self.moved = []
        for i in self.local_list_of_agents:
            if (i != -1 and i not in self.moved):
                list_of_passengers[i].move()
                self.moved.append(i)


    def can_i_add_one(self):
        global road_width
        for i in range(0, road_width):
            if (self.local_list_of_agents[i] != -1):
                return False
        return True


    def add_new(self, number):
        self.local_list_of_agents[0] = number





class main_road(road):
    '''главная дорога (к другим дорогам)'''
    def __init__(self, number, long, outs):
        road.__init__(self, number, long, outs)


class long_roads(road):
    '''дорога к креслам'''
    def __init__(self, number, long, out_list):
        road.__init__(self, number, long, out_list)


class passenger():
    def __init__(self, number):
        global ambition_list
        self.number = number
        self.position = [-1, 0, 0] # x, y, z  #предпологается совпадение
        self.long = random.choice([2, 3, 4, 5]) # не точно (хз)
        self.speed = random.choice([1, 2, 3, 4]) # не точно (хз)
        self.time_to_sit = random.choice([2, 3, 4, 5, 6, 7, 8, 9]) # не точно (хз)
        self.time_to_bags = random.choice([4, 5, 6, 7, 8, 9, 10, 11]) # не точно (хз)
        self.oll_time = self.time_to_sit + self.time_to_bags
        self.condition = 0  # 0 - идёт, 1 - садится, 2 - сидит, 3 - поворачаивает
        self.ambition = ambition_list[self.number]


    def move(self):
        global list_of_roads
        global sat_down
        global step
        #print(list_of_roads[self.position[0]][self.position[2]].out_list)
        #print(len(list_of_roads[self.position[0]][self.position[2]].local_list_of_agents))
        # перемещения не учитывают очереди
        #print(" ")
        #print(" ")
        #print(" ")
        #print(list_of_roads[0][0].local_list_of_agents)
        #print(" ")
        #print(" ")
        #print(" ")
        if (self.condition == 0 or self.condition == 3):
            if (self.position[0] == -1):
                if (self.position[1] >= list_of_roads[0][0].out_list[self.ambition[0]]):
                    # тут выполняем поворот (перемещение в другой массив)
                    self.condition = 3

                    if (list_of_roads[1][self.ambition[0]].can_i_add_one()):
                        print(str(step) + " повернул" + str(self.position), end=" ",)
                        list_of_roads[0][0].local_list_of_agents[self.position[1]] = -1
                        list_of_roads[1][self.ambition[0]].add_new(self.number)
                        self.condition = 0
                        self.position[0] = self.ambition[0]
                        self.position[1] = 0
                        list_of_roads[1][self.ambition[0]].local_list_of_agents[self.position[1]] = self.number
                        print(str(step) + " повернул" + str(self.position) + " " + str(self.ambition) + " " + str(self.number))
                elif (list_of_roads[0][0].out_list[self.ambition[0]] - self.position[1] > self.speed):
                    # тут шаг
                    print("шагнул в главной" + " " + str(self.number))
                    list_of_roads[0][0].local_list_of_agents[self.position[1]] = -1
                    self.position[1] += self.speed
                    #print(self.position)
                    list_of_roads[0][0].local_list_of_agents[self.position[1]] = self.number
                else:
                    # тут явное перемещение
                    list_of_roads[0][0].local_list_of_agents[self.position[1]] = -1
                    self.position[1] = list_of_roads[0][0].out_list[self.ambition[0]] + 1
                    list_of_roads[0][0].local_list_of_agents[self.position[1]] = self.number
            else:
                if (self.position[1] >= list_of_roads[1][self.ambition[0]].out_list[self.ambition[1]]):
                    # начинаем садиться
                    self.condition = 1
                elif (list_of_roads[1][self.ambition[0]].out_list[self.ambition[1]] - self.position[1] > self.speed):
                    # тут шаг
                    print("шагнул в длинной" + " " + str(self.number))
                    list_of_roads[1][self.position[0]].local_list_of_agents[self.position[1]] = -1
                    self.position[1] += self.speed
                    #print(self.position)
                    list_of_roads[1][self.position[0]].local_list_of_agents[self.position[1]] = self.number
                else:
                    # тут явное перемещение
                    list_of_roads[1][self.position[0]].local_list_of_agents[self.position[1]] = -1
                    self.position[1] = list_of_roads[1][self.ambition[0]].out_list[self.ambition[1]] + 1
                    list_of_roads[1][self.position[0]].local_list_of_agents[self.position[1]] = self.number
        elif (self.condition == 1):
            self.oll_time -= 1
            if (self.oll_time <= 0):
                list_of_roads[1][self.position[0]].local_list_of_agents[self.position[1]] = -1
                self.condition = 2
                sat_down += 1
                print(str(step) + " сел"  + str(self.position) + " " + str(self.ambition) + " " + str(self.number))
        else:
            pass
            # тут аген точно сидит
    def get_last_point(self):
        return (self.position[1] - self.long)


def let_one_in():
    global on_board_now
    global ambition_list5
    global list_of_roads
    global list_of_passengers
    if (on_board_now < len(ambition_list) and list_of_roads[0][0].can_i_add_one()):
        list_of_passengers.append(passenger(on_board_now))
        list_of_roads[0][0].add_new(on_board_now)
        on_board_now += 1
        print(str(step) +  " +1")


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
        for j in range(0, 14):
            for k in range(0, 7):
                if k == 3:
                    continue
                if (i == 0 and j >= 11 and k < 3):
                    continue
                if (i == 3 and j >= 11 and k > 3):
                    continue
                ambition_list.append([i, j, k])
    random.shuffle(ambition_list)



for iteration in range(0, 1):
    build_for_flying_wing()
    random_ambition_list_for_flying_wing(1)
    sat_down = 0
    on_board_now = 0
    step = 0
    with open("main_model_out/out_of_iteration_" + str(iteration) + ".csv", "w") as f:
        while (sat_down < len(ambition_list)):
            step += 1
            #print("step: " + str(step) + " " + "on_board_now" + " = " + str(on_board_now))
            let_one_in()
            for i in range(0, len(list_of_roads[1])):
                list_of_roads[1][i].act()
            list_of_roads[0][0].act()
            print("село: " + str(sat_down))



















#
