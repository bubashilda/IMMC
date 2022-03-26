import csv

arr = []
for i in range(1000):
    arr.append(0)
ITERATIONS = 1000
maximum = 0
for i in range(ITERATIONS):
    with open(f'../models/data/simple_model_out/out_of_iteration_{i}.csv') as file:
        for line in file:
            tmp = line.split(';')
            arr[int(tmp[0])] += int(tmp[1])
        maximum += int(tmp[0])
arr[maximum // ITERATIONS] = 1
arr = arr[0:(maximum // ITERATIONS) + 1]
for i in range(maximum // ITERATIONS):
    arr[i] /= (ITERATIONS * 198)
print(maximum / ITERATIONS)
with open('../models/data/results/wind-mid-aisle.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['time', 'part'])
    for i in range(len(arr)):
        writer.writerow([i + 1, round(float(arr[i]), 3)])
