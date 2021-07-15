a1 = ()
a2 = (1) # pay attention at here
a3 = (1,)
a4 = (1, 2)

print(a1) # ()
print(a2) # 1  When we var a2 = (1), you will get a 1, and it's not a tuple.
print(a3) # (1,) This is an tuple.
print(a4) # (1, 2)

print(type(a1)) # <class 'tuple'>
print(type(a2)) # <class 'int'>
print(type(a3)) # <class 'tuple'> 
print(type(a4)) # <class 'tuple'>

a5 = 1, 2, 3, 4, 5
a6 = "apple", "banana", "car", "dog"

print(a5) # (1, 2, 3, 4, 5) 
print(a6) # ('apple', 'banana', 'car', 'dog')
print(type(a5)) # <class 'tuple'>
print(type(a6)) # <class 'tuple'>

# Translate a list to tuple.
a7 = ["apple", "banana", "cat"]
print(type(a7)) # <class 'list'>
a7 = tuple(a7)
print(type(a7)) # <class 'tuple'>

# list [1,2,3,4,5]
# tuple (1,2,3,4,5)
# set {1,2,3,4,5}