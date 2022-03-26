import random

ambition_list = []

list_of_passengers = []
list_of_roads = []
list_of_seats = []

main_road = []
ambition_list = []

list_of_moving_points = []
list_of_seats_coordinates = []

road_wight = 5
seats_width = 6
seats_lenght = 6
distance_between_seats = 3


class passenger():
    def __init__(self, number):
        global ambition_list

        global main_road

        self.number = number

        self.position = -1

        self.visible_position = [self.number, 0, 0]

        self.long = 3 # сделать рандомным
        self.speed = 2 # сделать рандомным
        self.time_to_sit = 2 # сделать рандомным
        self.time_to_bags = 4 # сделать рандомным

        self.oll_time = self.time_to_sit + self.time_to_bags # общее время сесть
        self.condition = 0 # 0 - идёт по главной, 1 - поворачивает, 2 идёт к месту, 3 - садиться, 4 - сидит

        self.ambition = ambition_list[self.number]

        main_road.append(self.visible_position)


    def move(self):
        global list_of_roads
        global main_road

        global sat_down

        global list_of_seats

        global list_of_moving_points
        global list_of_seats_coordinates
        #print(list_of_roads)
        #print(self.visible_position)
        if (self.condition == 0):
            '''идёт по главной'''
            '''определение максимальной длинны шага'''
            max_step_long = 0
            for i in range(0, len(main_road)):
                if (main_road[i][0] == self.number):
                    break
            if (len(main_road) > i + 1):
                if (list_of_passengers[main_road[i + 1][0]].get_last_point() > self.visible_position[1] + self.speed):
                    max_step_long = self.speed
                else:
                    max_step_long = (list_of_passengers[main_road[i + 1][0]].get_last_point() - self.visible_position[1])
            else:
                max_step_long = self.speed

            '''проверка на выход'''
            if (list_of_moving_points[self.ambition[0]] - max_step_long <= self.visible_position[1]):
                '''шаг ровно к точке входа'''
                self.condition = 1
                self.visible_position[2] = self.condition
                self.visible_position[1] = list_of_moving_points[self.ambition[0]]
            else:
                '''обычный шаг'''
                self.visible_position[1] += max_step_long

        elif (self.condition == 1):
            '''готов повернуть''' # считаем, что прохот не достаточно широкий, чтобы идти в 2 потока, но достаточно широкий, чтобы не замедлять
            if (len(list_of_roads[self.ambition[0]]) != 0):
                #print(list_of_roads[self.ambition[0]][0])
                if (list_of_passengers[list_of_roads[self.ambition[0]][0][0]].get_last_point() >= road_wight):
                    '''переносим'''
                    self.condition = 2
                    self.position = self.ambition[0]
                    self.visible_position[1] = 0
                    self.visible_position[2] = self.condition
                    for i in range(0, len(main_road)):
                        if (main_road[i][0] == self.number):
                            main_road.pop(i)
                            break
                    list_of_roads[self.ambition[0]].append(self.visible_position)
                else:
                    '''ждём'''
                    pass
            else:
                '''переносим'''
                self.condition = 2
                self.position = self.ambition[0]
                self.visible_position[1] = 0
                self.visible_position[2] = self.condition
                for i in range(0, len(main_road)):
                    if (main_road[i][0] == self.number):
                        main_road.pop(i)
                        break
                list_of_roads[self.ambition[0]].append(self.visible_position)


        elif (self.condition == 2):
            '''идёт к месту'''
            max_step_long = 0
            for i in range(0, len(list_of_roads[self.position])):
                if (list_of_roads[self.position][i][0] == self.number):
                    break
            if (len(list_of_roads[self.position]) > i + 1):
                if (list_of_passengers[list_of_roads[self.position][i + 1][0]].get_last_point() > self.visible_position[1] + self.speed):
                    max_step_long = self.speed
                else:
                    if (list_of_passengers[list_of_roads[self.position][i + 1][0]].get_condition() == 3):
                        if (len(list_of_roads[self.position]) > i + 2):
                            if (list_of_passengers[list_of_roads[self.position][i + 2][0]].get_last_point() > self.visible_position[1] + self.speed // 2):
                                max_step_long = self.speed // 2
                            else:
                                max_step_long = (list_of_passengers[list_of_roads[self.position][i + 2][0]].get_last_point() - self.visible_position[1])
                        else:
                            max_step_long = self.speed // 2
                    else:
                        max_step_long = (list_of_passengers[list_of_roads[self.position][i + 1][0]].get_last_point() - self.visible_position[1])


            else:
                max_step_long = self.speed

            '''проверка на выход'''

            if (self.ambition[1] - max_step_long <= self.visible_position[1]):
                '''шаг ровно к точке входа'''
                self.condition = 3
                self.visible_position[2] = self.condition
                self.visible_position[1] = self.ambition[1]

                for i in range(0, len(list_of_seats)):
                    if (list_of_seats[i][0] == self.ambition[0] and list_of_seats[i][1] == self.ambition[1]):
                        if (self.ambition[2] > 3 and list_of_seats[i][2] > 3 and list_of_seats[i][0] < self.ambition[2]):
                            self.oll_time += list_of_seats[i][3]
                        elif (self.ambition[2] < 3 and list_of_seats[i][2] < 3 and list_of_seats[i][0] > self.ambition[2]):
                            self.oll_time += list_of_seats[i][3]
            else:
                '''обычный шаг'''
                self.visible_position[1] += max_step_long

        elif (self.condition == 3):
            self.oll_time -= 1
            if (self.oll_time <= 0):
                self.condition = 4

                list_of_seats.append([self.ambition[0], self.ambition[1], self.ambition[2], self.time_to_sit])

                sat_down += 1
                self.position = self.ambition[0]
                self.visible_position[2] = self.condition
                for i in range(0, len(list_of_roads[self.ambition[0]])):
                    if (list_of_roads[self.ambition[0]][i][0] == self.number):
                        list_of_roads[self.ambition[0]].pop(i)
                        break

        else:
            pass
            '''не наступит'''


    def get_last_point(self):
        return self.visible_position[1] - self.long


    def get_condition(self):
        return self.condition


def let_one_in():
    '''пустить ещё кого нибудь'''
    global on_board_now

    global list_of_passengers
    global ambition_list

    global main_road

    if (len(ambition_list) > on_board_now):
        if (len(main_road) != 0):
            if (list_of_passengers[main_road[0][0]].get_last_point() >= road_wight):
                list_of_passengers.append(passenger(on_board_now))
                on_board_now += 1
        else:
            list_of_passengers.append(passenger(on_board_now))
            on_board_now += 1


def take_a_step():

    for i in range(0, len(list_of_roads)):
        list_of_roads[i].sort(key=lambda x: x[0])
        list_of_roads.reverse()

    main_road.sort(key=lambda x: x[0])
    main_road.reverse()
    print(list_of_roads[0])

    for x in range(0, len(list_of_roads)):
        i = 0
        n = len(list_of_roads[x])
        while i < n:
            if (len(list_of_roads[x]) != 0):
                list_of_passengers[list_of_roads[x][i][0]].move()
                if n == len(list_of_roads[x]):
                    i += 1
                else:
                    n = len(list_of_roads[x])

    i = 0
    n = len(main_road)
    while i < n:
        list_of_passengers[main_road[i][0]].move()
        if n == len(main_road):
            i += 1
        else:
            n = len(main_road)

'''####################################################################################################################################################################'''

def build_for_flying_wing():
    '''собрать параметры для летающего крыла'''
    global ambition_list

    global list_of_roads
    global main_road
    global list_of_seats

    global list_of_moving_points
    global list_of_seats_coordinates

    global road_wight
    global seats_width
    global seats_lenght
    global distance_between_seats


    list_of_roads.append([])
    list_of_roads.append([])
    list_of_roads.append([])
    list_of_roads.append([])

    list_of_moving_points.append(seats_width * 3)
    list_of_moving_points.append(seats_width * 3 * 3 + road_wight)
    list_of_moving_points.append(seats_width * 3 * 5 + road_wight * 2)
    list_of_moving_points.append(seats_width * 3 * 7 + road_wight * 3)


def build_for_narrow_body():
    '''собрать параметры для узкофузюляжного'''
    global ambition_list

    global list_of_roads
    global main_road
    global list_of_seats

    global list_of_moving_points
    global list_of_seats_coordinates

    global road_wight
    global seats_width
    global seats_lenght
    global distance_between_seats

    list_of_roads.append([])

    list_of_moving_points.append(seats_width * 3)


def build_for_two_entrance():
    '''собрать параметры для широкого с двумя рядами'''
    global ambition_list

    global list_of_roads
    global main_road
    global list_of_seats

    global list_of_moving_points
    global list_of_seats_coordinates

    global road_wight
    global seats_width
    global seats_lenght
    global distance_between_seats

    list_of_roads.append([])
    list_of_roads.append([])

    list_of_moving_points.append(seats_width * 3)
    list_of_moving_points.append(seats_width * 3 * 3 + road_wight)


def build_ambition_list_for_flying_wing_random(n):
    '''массив с билетами для летающего крыла (случайно)'''
    global ambition_list
    global distance_between_seats
    global seats_lenght

    for i in range(0, 4):
        for j in range(0, 14):
            for k in range(0, 7):
                if (k == 3):
                    continue
                if (i == 0 and j >= 11 and k < 3):
                    continue
                if (i == 3 and j >= 11 and k > 3):
                    continue
                ambition_list.append([i, j * (seats_lenght + distance_between_seats), k])

    random.shuffle(ambition_list)
    ambition_list = ambition_list[0: int(len(ambition_list) * n)]


def build_ambition_list_for_narrow_body_random(n):
    '''массив с билетами для узко фезюляжного (случайно)'''
    global ambition_list
    global distance_between_seats
    global seats_lenght

    for i in range(0, 33):
        for j in range(0, 7):
            if (j == 3):
                continue
            ambition_list.append([0, i * (seats_lenght + distance_between_seats), j])

    random.shuffle(ambition_list)
    ambition_list = ambition_list[0: int(len(ambition_list) * n)]


def build_ambition_list_for_two_entrance_random(n):
    '''массив с билетами для для широкого с двумя рядами (случайно)'''
    global ambition_list
    global distance_between_seats
    global seats_lenght

    for i in range(0, 2):
        for j in range(0, 20):
            for k in range(0, 7):
                if (k == 3):
                    continue
                if (i == 0 and j >= 11 and k < 3):
                    continue
                if (i == 3 and j >= 11 and k > 3):
                    continue
                ambition_list.append([i, j * (seats_lenght + distance_between_seats), k])

    random.shuffle(ambition_list)
    ambition_list = ambition_list[0: int(len(ambition_list) * n)]

'''####################################################################################################################################################################'''

for iteration in range(0, 10):

    ambition_list = []

    list_of_passengers = []
    list_of_roads = []

    list_of_seats = []

    main_road = []
    ambition_list = []

    list_of_moving_points = []
    list_of_seats_coordinates = []
    ####################################################
    #build_for_flying_wing() # для летающего крыла
    #build_for_narrow_body() # для узкофезюляжного
    build_for_two_entrance() # для самолёта с двумя проходами
    ####################################################

    ####################################################
    #build_ambition_list_for_flying_wing_random(1) # для летающего крыла (случайно)
    #build_ambition_list_for_narrow_body_random(1) # для узкофезюляжного (случайно)
    build_ambition_list_for_two_entrance_random(1) # для широкого с двумя проходами (случайно)
    ####################################################
    on_board_now = 0
    sat_down = 0
    step = 0
    with open("main_model_out/out_of_iteration_" + str(iteration) + ".csv", "w") as f:
        while (sat_down < len(ambition_list)):
            step += 1
            let_one_in()
            take_a_step()
            print(sat_down)

            f.write(str(step) + ";" + str(sat_down) + "\n")
