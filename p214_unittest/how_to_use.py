# 固定語法
# import unittest

# class 隨意名稱(unittest.TestCase):
#     def test_隨意名稱(self):
#         self.檢測方法(待檢值, 正確答案值)

# 檢測方法有以下幾種
# assertEqual(a, b)            a == b
# assertNotEqual(a, b)         a != b
# assertTrue(a)                bool(a) is True
# assertFalse(a)               bool(a) is False
# assertIs(a, b)               a is b
# assertIsNot(a, b)            a is not b
# assertIsNone(a)              a is None
# assertIsNotNone(a)           a is not None
# assertIn(a, b)               a in b
# assertNotIn(a, b)            a not in b
# assertIsInstance(a, b)       isinstance(a, b)
# assertNotIsInstance(a, b)    not isinstance(a, b)

# 最後進行測試有兩種方法
# 第一種測試方法為，直接在終端機輸入 python3 -m unittest 檔案全名
# 目前這個檔案就是輸入 python3 -m unittest how_to_use.py

import unittest

class HowToUseUnittest(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(1, 1)
    def test_assertNotEqual(self):
        self.assertNotEqual(2, 1)
    def test_assertTrue(self):
        self.assertTrue(True)
    def test_assertFalse(self):
        self.assertFalse(False)
    def test_assertIs(self):
        self.assertIs(1, 1)
    def test_assertIsNot(self):
        self.assertIsNot(2, 1)
    def test_assertIsNone(self):
        self.assertIsNone(None)
    def test_assertIsNotNone(self):
        self.assertIsNotNone(1)
    def test_assertIn(self):
        self.assertIn(1, [1, 2, 3])
    def test_assertNotIn(self):
        self.assertNotIn(4, [1, 2, 3])
    def test_assertIsInstance(self):
        self.assertIsInstance(1, int)
    def test_assertNotIsInstance(self):
        self.assertNotIsInstance(1, str)

# ............
# ----------------------------------------------------------------------
# Ran 12 tests in 0.000s
# 
# OK
