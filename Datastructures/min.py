x = [1, 3, 7, 0, 7, 2, -12, 0]

min_value = x[0]

for i in range(len(x)):
    if x[i] < min_value:
        min_value = x[i]
        print(min_value)
