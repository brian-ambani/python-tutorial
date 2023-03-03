# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple

fruits = ('Apples', 'oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Oranges'))

#single value needs a trailing comma
fruits2 = ('Apples',)

#print(fruits2, type(fruits2))

# Get value
print(fruits[1])

# Delete tuple
# del fruit2

# get length
print(len(fruits))




# A set is a collection which is unordered and unindexed. No duplicate members.

# Create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)


# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')


# Add duplicate
fruits_set.add('Apples')

# Clear
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)

