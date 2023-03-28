class Robot:
    pass
x = Robot()
y = Robot()

x.name = "Tom"
x.build_year = 1979
y.name = "caliban"
y.build_year = 1993

#print(x.name)

print(x.__dict__)
print(y.__dict__)
