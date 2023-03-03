# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# Use a constructor
#numbers2 = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))


# Append to list
fruits.append('mangoes')

#Change value
fruits[0] = 'Blue berrys'

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberry')

# remove with pop
fruits.pop(2)

#Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse = True)

print(fruits)
