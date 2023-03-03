
name = 'Brian'
age = 25

#concatenate
#print('Hello, my name is ' + name + 'am I am ' + str(age))

#Arguments by position
#print('My name is {name} and I am {age}'.format(name = name, age = age))


#F-Strings(3.6+)
#print(f'Hello my name is {name} and I am {age}')


# Common string methods

s = 'Hello python'

# Get length
print(len(s))

# Split
print(s.split())

# Find position
print(s.find('y'))

# capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

#make all lowercase
print(s.lower())

#swap case
print(s.swapcase())
