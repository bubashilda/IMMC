import random


class passenger():
    '''класс пасажир'''
    def __init__(self, number):
        global ambition_list
        global speed_factor
        self.speed = 10 #ВРЕМЕННО (обязательно кратен speed_factor)
        self.long = 20 #ВРЕМЕННО #длинна пассажира (в сантиметрах)
        self.width = 50 #ВРЕМЕННО #ширина пассажира (в сантиметрах)
        self.location = [0, 0 - self.long]
        self.ambition = ambition_list[number] # получение посадочного места

    def move(self):
        # шаг за единицу времяни
        self.location[0] += speed
        self.location[1] += speed

    def turn_front(self):
        # поворот передом
        pass

    def turn_side(self):
        # поворот боком
        pass

    def get_location(self):
        # получение массива координат
        return self.location

    def get_ambition(self):
        # получение посадочного места
        return self.ambition

    def add_new_passenger():
        # добавление нового пассажира
        pass


speed_factor = 10 # коэффицент скорости
seat_length = 55 # длинна кресел (в сантиметрах)
other_length = 20 # длинна промежутков между креслами (в сентиметрах)
plane_long = 33 * seat_length * other_length
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
location_list = []


on_board = 0 # людей на борту
while True:
    pass
