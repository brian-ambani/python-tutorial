num_list = [10, 20, 30, 40]

print(num_list)

def multiply_by_2(x):
    x[0] *= 2
    x[1] *= 2
    x[2] *= 2
    x[3] *= 2

multiply_by_2(num_list)

print(num_list)
