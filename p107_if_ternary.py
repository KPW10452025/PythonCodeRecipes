# Ternary Conditional Operator

num3 = 6
num4 = 7

# 三目運算寫法
print("apple" if num4 > num3 else "banana")
# apple

def rectangle(a, b):
    return a*b if a>0 and b>0 else "a and b need to larger than 0."

print(rectangle(1,3)) # 3
print(rectangle(1,0)) # a and b need to larger than 0.
print(rectangle(0,3)) # a and b need to larger than 0.
print(rectangle(0,0)) # a and b need to larger than 0.

def division(a, b):
    return a/b if b>0 else "b > 0 is necessary."

print(division(1, 3))
print(division(1, 0))

def division2(a, b):
    if b > 0:
        return a/b
    else:
        return "b > 0 is necessary."

print(division2(1, 3))
print(division2(1, 0))
