import math
num1 = 0
while num1 <= 100:
    if num1 % 7 == 0:
        print(num1, "is the number I want.")
    num1 += 1
# 0 is the number I want.
# 7 is the number I want.
# 14 is the number I want.
# 21 is the number I want.
# 28 is the number I want.
# 35 is the number I want.
# 42 is the number I want.
# 49 is the number I want.
# 56 is the number I want.
# 63 is the number I want.
# 70 is the number I want.
# 77 is the number I want.
# 84 is the number I want.
# 91 is the number I want.
# 98 is the number I want.

ls = [1, 4, 9, 64, 49, 100, -49, -81]
for l in ls:
    if l < 0:
        print("l need to larger than 0.")
        # continue
    else:
        s = math.sqrt(l)
        print(s)
# 1.0
# 2.0
# 3.0
# 8.0
# 7.0
# 10.0
# l need to larger than 0.
# l need to larger than 0.

list1s = [1, 4, 9, 64, 49, 100, -49, -81]
for list1 in list1s:
    if list1 < 0:
        print("the number in the list need to larger than 0.")
        continue
    s = math.sqrt(list1)
    print(list1, "-->", s)
# 1 --> 1.0
# 4 --> 2.0
# 9 --> 3.0
# 64 --> 8.0
# 49 --> 7.0
# 100 --> 10.0
# the number in the list need to larger than 0.
# the number in the list need to larger than 0.
