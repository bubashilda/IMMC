# model of disembarking in a general case
# DEBUG!
import random

WIDTH_AISLE = 5
passengers_on_board = 32
aisles = []
buffer = []


class Aisle:
    def __init__(self, seating, y):
        self.seating = seating
        self.y = y
        self.standing = []

    # insert passenger in an aisle
    def insertion_in_aisle(self):
        for i in range(len(self.seating)):
            # aisle end coordinates
            x1 = WIDTH_AISLE * i
            x2 = WIDTH_AISLE * (i + 1)
            is_in_range = False
            for elem in self.standing:
                if x1 <= elem.x < x2 or x1 < elem.x + WIDTH_AISLE < x2:
                    is_in_range = True
            if not is_in_range:
                inx_aisle = self.seating[i].index([])
                inx_desired = -1
                inx_left = -1
                inx_right = -1
                for j in range(inx_aisle - 1, -1, -1):
                    if self.seating[i][j] != 0:
                        inx_left = j
                        break
                for j in range(inx_aisle + 1, len(self.seating[i])):
                    if self.seating[i][j] != 0:
                        inx_right = j
                        break
                if inx_right == -1 and inx_left != -1:
                    inx_desired = inx_left
                elif inx_right != -1 and inx_left == -1:
                    inx_desired = inx_right
                elif inx_right != -1 and inx_left != -1:
                    if self.seating[i][inx_left].aggression > self.seating[i][inx_right].aggression:
                        inx_desired = inx_left
                    else:
                        inx_desired = inx_right
                inx_insert_in_standing = -1
                for j in range(len(self.standing)):
                    if self.standing[j].x < x1:
                        inx_insert_in_standing = j + 1
                if inx_desired != -1:
                    self.seating[i][inx_desired].state = 1
                    self.seating[i][inx_desired].x = x1
                    self.seating[i][inx_desired].y = self.y * WIDTH_AISLE
                    self.standing.insert(inx_insert_in_standing, self.seating[i][inx_desired])
                    self.seating[i].pop(inx_desired)
                    self.seating[i].insert(inx_desired, 0)

    # do something on the passenger depending on his state
    def move(self):
        global buffer
        index = {'to_insert': -1, 'to_remove': 0}
        for i in range(len(self.standing)):
            if self.standing[i].state == 1 and self.standing[i].time_to_stand > 0:
                self.standing[i].time_to_stand -= 1
            elif self.standing[i].state == 1 and self.standing[i].time_to_stand == 0:
                if self.standing[i].time_to_get_lug == 0:
                    self.standing[i].state = 3
                else:
                    self.standing[i].state = 2
                    self.standing[i].time_to_get_lug -= 1

            if self.standing[i].state == 2 and self.standing[i].time_to_get_lug > 0:
                self.standing[i].time_to_get_lug -= 1
            elif self.standing[i].state == 2 and self.standing[i].time_to_get_lug == 0:
                if i == len(self.standing) - 1:
                    self.standing[i].state = 3
                else:
                    if self.standing[i + 1].state != 4:
                        self.standing[i].state = 3

            if self.standing[i].state == 3:
                if i == 0:
                    if self.standing[i].x == 0:
                        is_busy = False
                        for elem in buffer:
                            if self.standing[i].y + WIDTH_AISLE > elem.y > self.standing[i].y \
                                    or self.standing[i].y + WIDTH_AISLE > elem.y + WIDTH_AISLE > self.standing[i].y:
                                is_busy = True
                        if not is_busy:
                            inx = 0
                            for j in range(len(buffer)):
                                if buffer[j].y < self.standing[i].y:
                                    inx = j + 1
                            index['to_insert'] = inx
                    elif self.standing[i].x - self.standing[i].speed > 0:
                        self.standing[i].x = self.standing[i].x - self.standing[i].speed
                    elif self.standing[i].x - self.standing[i].speed <= 0:
                        self.standing[i].x = 0
                else:
                    if self.standing[i].x - self.standing[i].speed >= self.standing[i - 1].x + WIDTH_AISLE:
                        self.standing[i].x = self.standing[i].x - self.standing[i].speed
                    elif self.standing[i].x - self.standing[i].speed < self.standing[i - 1].x + WIDTH_AISLE:
                        self.standing[i].x = self.standing[i - 1].x + WIDTH_AISLE
                        # self.standing[i].state = 4 TODO

            if self.standing[i].state == 4:
                pass

        if index['to_insert'] != -1:
            self.standing[0].y = self.y
            buffer.insert(index['to_insert'], self.standing[0])
            self.standing.pop(0)
        self.insertion_in_aisle()


class Passenger:
    # state = 0 means passenger is seating, state = 1 --- is standing
    # state = 2 --- is getting luggage, state = 3 --- is going, 4 --- is overtaking
    def __init__(self, speed, time_to_stand, time_to_get_lug, aggression, x=0, y=0):
        self.speed = speed
        self.time_to_stand = time_to_stand
        self.time_to_get_lug = time_to_get_lug
        self.state = 0
        self.aggression = aggression
        self.x = x
        self.y = y


def move_in_buffer():
    global buffer
    global passengers_on_board
    to_delete = []
    for i in range(len(buffer)):
        if i == 0:
            if buffer[i].y < 0:
                to_delete.append(i)
                passengers_on_board -= 1
            else:
                buffer[i].y -= buffer[i].speed
        else:
            if i - 1 not in to_delete:
                if buffer[i].y - buffer[i].speed < buffer[i - 1].y + WIDTH_AISLE:
                    buffer[i].y = buffer[i - 1].y + WIDTH_AISLE
                else:
                    buffer[i].y -= buffer[i].speed
            else:
                if buffer[i].y - buffer[i].speed < 0:
                    to_delete.append(i)
                else:
                    buffer[i].y -= buffer[i].speed
    for i in range(len(to_delete)):
        buffer.pop(to_delete[i] - i)


sec = 0
# Здесь задаются ряды
aisles.append(Aisle(seating=[[Passenger(1, 1, 1, 1), [], Passenger(1, 1, 1, 1), Passenger(1, 1, 1, 1)]], y=3))
while passengers_on_board != 0:
    for aisle in aisles:
        aisle.move()
    move_in_buffer()
    sec += 1
    print(sec, passengers_on_board)
