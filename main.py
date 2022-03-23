import random


class passenger():
    '''класс пасажир'''
    def __init__(self, number):
        global ambition_list
        global speed_factor

        self.state_of_man = 0 # текущее состояние агента

        self.speed = 10 ## TODO: сделать случайным
        self.long = 20 ## TODO: сделать случайным
        self.width = 50 ## TODO: сделать случайным

        self.aggression = 1 ## TODO: сделать случайным

        self.ambition = ambition_list[number] # получение посадочного места

        self.location = [0, 0 - self.long]

    def move(self):
        global location_list_step_forward

        location_list_step_forward = []

        self.location[0] += self.speed # шаг за единицу времяни
        self.location[1] += self.speed # шаг за единицу времяни

        location_list_step_forward.append()


    def get_location(self):
        # получение массива координат
        return self.location

    def get_ambition(self):
        # получение посадочного места
        return self.ambition


def step():
    global number_now
    global on_board
    global location_list_now
    global passenger_list

    #print(len(location_list_now))
    if (len(location_list_now) > 1):
        location_list_now.sort(key=lambda x: x[0])

    distance = location_list_now[0][1] # получение расстояния от входа последнего
    if (distance > start_distance):
        on_board += 1
        location_list_now.append([passenger_list[on_board].get_location().append(on_board)])

    for i in range(0, on_board):
        passenger_list[i].move()


aggression_limit_1 = 60
start_distance = 50 # можно сделать случайным


seat_length = 55 # длинна кресел (в сантиметрах)
other_length = 20 # длинна промежутков между креслами (в сентиметрах)
plane_long = 33 * (seat_length + other_length)
plane_width = 60 # ширина прохода в метрах


# создание массива посадочных мест + получение их случайной комбинации
ambition_list = []
for i in range(1, 33 + 1):
    for j in range(0, 6):
        ambition_list.append([i, j])
        # тут изменять порядок захода пассажиров на борт
        random.shuffle(ambition_list) # слуяайная перестановка


# создание списка пассажиров
passenger_list = []
for i in range(0, len(ambition_list)):
    passenger_list.append(passenger(i))


# список координат людей
location_list_now = []
location_list_step_forward = []

on_board = 0 # людей на борту
in_place = 0 # счётчик людей, сидящих на своих местах

location_list_now.append(passenger_list[on_board].get_location())
location_list_now[-1].append(on_board)

location_list_step_forward.append(passenger_list[on_board].get_location())
location_list_step_forward[-1].append(on_board)

on_board += 1

while (in_place != len(passenger_list)):
    step()
