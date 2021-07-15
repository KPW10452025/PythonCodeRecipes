dict1 = {"a" : "apple", "b" : "banana", "c" : "car", "d" : "Django", "e" : "elphant"}

for i in dict1.values():
    print(i)
# apple
# banana
# car
# Django
# elphant

for i in dict1:
    print(i)
# a
# b
# c
# d
# e

for i in dict1.items():
    print(i)
# ('a', 'apple')
# ('b', 'banana')
# ('c', 'car')
# ('d', 'Django')
# ('e', 'elphant')

for a, b in dict1.items():
    print(a, b)
# a apple
# b banana
# c car
# d Django
# e elphant
