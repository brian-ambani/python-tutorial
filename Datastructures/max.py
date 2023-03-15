x = [200, 15, 17, 90, 101, 67, 1008]

max_value = x[0]

for i in range(len(x)):
    if x[i] > max_value:
        max_value = x[i]

print(max_value)
