import csv

arr = []
for i in range(4000):
    arr.append(0)
ITERATIONS = 1000
PART = 1
maximum = 0
for i in range(ITERATIONS):
    with open(f'../main_model/main_model_out/out_of_iteration_{i}.csv') as file:
        for line in file:
            tmp = line.split(';')
            arr[int(tmp[0])] += int(tmp[1])
        maximum += int(tmp[0])
arr[maximum // ITERATIONS] = 1
arr = arr[0:(maximum // ITERATIONS) + 1]
for i in range(maximum // ITERATIONS):
    arr[i] /= (ITERATIONS * 198 * PART)
print(maximum / ITERATIONS)
with open('../main_model/results/two_aisle.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['time', 'part'])
    for i in range(len(arr)):
        writer.writerow([i + 1, round(float(arr[i]), 3)])