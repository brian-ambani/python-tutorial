# Problem Statement
# Gravitational force is the attractive force that exists between two masses. It can be calculated by using the following formula:

           # GMm/r**2 

# where G is the gravitational constant, M and m are the two masses, and r is the distance between them.

# You must implement this equation in Python to calculate the gravitational force between Earth and the moon.

# Sample Input
# G = 6.67 * 10** -11

# MEarth = 6.0 * 10**24

# mMoon = 7.34 * 10**22

# r = 3.84 * 10**8

# Sample Output
# FG = 1.99 * 10**20

# Coding Challenge
# All the values have already been given to you. You must write the formula in Pythonic syntax and store the answer in the grav_force variable.


G = 6.7 * (10 ** -11)
M = 6.0 * (10 ** 24) # Mass of Earth
m = 7.34 * (10 ** 22) # mass of the Moon
r = 3.84 * (10 ** 8)

gravity_force = (G * M * m) / (r ** 2)
print(gravity_force)

