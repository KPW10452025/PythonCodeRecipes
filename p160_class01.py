class User:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def info(self):
        print("name: ", self.name)
        print("weight: ", self.weight)

employee001 = User("James", 75)
print(employee001.name)
# James
print(employee001.weight)
# 75
employee001.info()
# name:  James
# weight:  75

employee001.name = "Jay"
employee001.weight = 66
print(employee001.name)
# Jay
print(employee001.weight)
# 66
employee001.info()
# name:  Jay
# weight:  66
