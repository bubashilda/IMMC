import random
import pandas as pd
import csv

with open('res.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    arr = []
    for i in range(300):
        arr.append([])

    for i in range(1, 1000):
        filename = f'models/data/simple_model_out/out_of_iteration_{i}.csv'
        with open(filename, 'r') as file:
            for string in file:
                tmp = string.split(';')
                arr[int(tmp[0]) - 1].append(int(tmp[1]))

    for i in range(len(arr)):
        if len(arr[i]) != 0:
            sum = 0
            for j in arr[i]:
                sum += j
            arr[i] = sum/len(arr[i])
            writer.writerow([i + 1, round(arr[i] / 198, 4)])
