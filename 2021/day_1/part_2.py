with open ("./../data/in_data_day_1.txt") as file:
    data = [int(i) for i in file.read().strip().split("\n")]

n = len(data)
count = 0

# compute moving sum
prev_moving_sum = 1 << 60
moving_sum = sum(data[:3])

for i in range(n-3):
    if moving_sum > prev_moving_sum:
        count += 1

    prev_moving_sum = moving_sum

    # update the moving sum 
    moving_sum -= data[i]
    moving_sum += data[i+3]

if moving_sum > prev_moving_sum:
    count += 1

print(count)
