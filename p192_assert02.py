def sum_abs(a, b):
    val = abs(a) + b
    assert val >= 0, "計算結果是小於零"
    return val

val1 = sum_abs(-20, -19)
print(val1)
# 1
val2 = sum_abs(10, -23)
print(val2)
# Traceback (most recent call last):
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p192_assert02.py", line 9, in <module>
#     val2 = sum_abs(10, -23)
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p192_assert02.py", line 3, in sum_abs
#     assert val >= 0, "計算結果是小於零"
# AssertionError: 計算結果是小於零
