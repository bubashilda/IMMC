# model of boarding at a narrow plane
import random

NUM_ROWS = 33
NUM_SEATS_IN_ROW = 6
seating_passengers = []
queue = []
passengers_in_aisle = []


class Passenger:
    def __init__(self, num_row, letter, time_to_put_lug):
        self.num_row = num_row
        self.letter = letter
        self.time_to_put_lug = time_to_put_lug
        self.x = 0


def step():
    to_delete = []
    for i in range(len(passengers_in_aisle)):
        if i == 0:
            if passengers_in_aisle[i].x < passengers_in_aisle[i].num_row:
                passengers_in_aisle[i].x += 1
            elif passengers_in_aisle[i].x == passengers_in_aisle[i].num_row and passengers_in_aisle[i].time_to_put_lug > 0:
                passengers_in_aisle[i].time_to_put_lug -= 1
            elif passengers_in_aisle[i].x == passengers_in_aisle[i].num_row and passengers_in_aisle[i].time_to_put_lug == 0:
                seating_passengers.append(passengers_in_aisle[i])
                passengers_in_aisle[i].x = -1
                to_delete.append(i)
        else:
            if passengers_in_aisle[i].x < passengers_in_aisle[i].num_row and \
                    len(passengers_in_aisle) > 1 and passengers_in_aisle[i - 1].x != passengers_in_aisle[i].x + 1:
                passengers_in_aisle[i].x += 1
            elif passengers_in_aisle[i].x == passengers_in_aisle[i].num_row and passengers_in_aisle[i].time_to_put_lug > 0:
                passengers_in_aisle[i].time_to_put_lug -= 1
            elif passengers_in_aisle[i].x == passengers_in_aisle[i].num_row and passengers_in_aisle[i].time_to_put_lug == 0:
                seating_passengers.append(passengers_in_aisle[i])
                passengers_in_aisle[i].x = -1
                to_delete.append(i)
    for i in range(len(to_delete)):
        passengers_in_aisle.pop(to_delete[i] - i)
    if len(queue) != 0 and (len(passengers_in_aisle) == 0 or len(passengers_in_aisle) != 0 and passengers_in_aisle[-1].x != 1):
        passengers_in_aisle.append(queue[0])
        passengers_in_aisle[-1].x = 1
        queue.pop(0)


dictionary = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'}
for i in range(NUM_ROWS):
    for j in range(NUM_SEATS_IN_ROW):
        queue.append(Passenger(i + 1, dictionary.get(j), 15))
random.shuffle(queue)

sec = 0
while NUM_ROWS * NUM_SEATS_IN_ROW != len(seating_passengers):
    step()
    sec += 1
    print(sec, len(seating_passengers))

