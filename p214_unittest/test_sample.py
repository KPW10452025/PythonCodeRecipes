import unittest
from sample import Addition, Subtraction, Multiplication, Division

class TestDmo(unittest.TestCase):
    def test_123(self):
        self.assertEqual(Addition(4, 2), 6)
    def test_234(self):
        self.assertEqual(Subtraction(4, 2), 2)
    def test_345(self):
        self.assertEqual(Multiplication(4, 2), 8)
    def test_456(self):
        self.assertEqual(Division(4, 2), 2)

# 最後進行測試有兩種方法
# 第一種測試方法為，直接在終端機輸入 python3 -m unittest 檔案全名
# 目前這個檔案就是輸入 python3 -m unittest test_sample.py
# 如果測試通過就會得到

# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s
#
# OK

# 為了知道故意會得到什麼結果
# 所以調整程式碼如下
#   def test_456(self):
#       self.assertEqual(Division(4, 2), 2)
# 改成
#   def test_456(self):
#       self.assertEqual(Division(4, 2), 1)
# 得到的結果為

# ...F
# ======================================================================
# FAIL: test_456 (test.TestDmo)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p214_unittest/test.py", line 12, in test_456
#     self.assertEqual(Division(4, 2), 1)
# AssertionError: 2.0 != 1
#
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s
#
# FAILED (failures=1)



# 第二種測試方法為，在測試檔案中加入以下編碼

# if __name__ == '__main__':
    # unittest.main()

# 這段編碼的好處是，終端機輸入只要是
# python3 檔案全命
# 目前這個檔案就是輸入 test_sample.py 即可