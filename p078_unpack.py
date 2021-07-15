# Unpack is an type of error.

list1 = ["apple", "banana","car"]
a, b, c = list1
print(a, b, c) # apple banana car
print(c) # car

list2 = [1, 2, 3, 4, 5]
# a, b = list2
# ValueError: too many values to unpack (expected 2)

list3 = [1, 2]
# a, b, c, d = list3
# ValueError: not enough values to unpack (expected 4, got 2)