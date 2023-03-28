class Fruit:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def details(self):
        print(f"my name is {self.name} and color is {self.color}")

apple = Fruit("apples", "red")

apple.details()
