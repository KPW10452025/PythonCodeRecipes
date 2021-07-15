num1 = 5
num2 = 6

if num1 > num2:
    print("apple")
else:
    print("banana")
# banana

def TriangleAreaFormula(width, height):
    if width > 0 and height > 0:
        return (width * height)/2
    else:
        return "The width and height need to larger than 0."

answer = TriangleAreaFormula(10, 20)
print(answer) # 100.0
answer = TriangleAreaFormula(0, 20)
print(answer) # The width and height need to larger than 0.
answer = TriangleAreaFormula(10, 0)
print(answer) # The width and height need to larger than 0.
answer = TriangleAreaFormula(0, 0)
print(answer) # The width and height need to larger than 0.
