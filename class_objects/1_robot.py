class Robot:
    def __init__(self, name=None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a bot without a name")
x = Robot()
x.say_hi()
y = Robot("Tom")
y.say_hi()
