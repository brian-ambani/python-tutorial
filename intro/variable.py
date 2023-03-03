a = 2
a = a + 3

print(a)
b = 10

print(a + b)

#this is a single line comment
'''
This is a multiline comment.
'''

'''
x = 1           #int
y = 2.5         #float
name = 'John'   #str
is_cool = True  #bool
'''

#multiple assignment

x, y, name, is_cool = (1, 2.5, 'John', True)

print(x, y, name, is_cool)


#casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)
