class passenger():
    '''класс пасажир'''
    def __init__(self, number):
        global ambition_list

        self.number = number
        self.ambition = ambition_list[self.number]
        self.position = [0, 3]

    def move(self):
        global plane

        if (self.position[0] == self.amambition[0]):
            pass
        else:
            if plane


plane = []
for i in range(0, 33 + 1):
    plane.append([0, 0, 0, 0, 0, 0, 0]) # проход с индексом 0

ambition_list = []
for i in range(1, 33 + 1):
    for j in range(0, 6):
        if (j == 3):
            continue
        ambition_list.append([i, j])
        random.shuffle(ambition_list)
