batman = "Bruce wayne"

first = batman[0]  # accessing the first character
print(first)

# error = batman[len(batman)]
# print(error) will produce an error since the index is out of bound


#instead print this
last = batman[(len(batman)) - 1]
print(last)

