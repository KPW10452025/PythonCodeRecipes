#   def setUp():

import unittest
class TestSample(unittest.TestCase):
    def setUp(cls):
        print("在每次的測試前執行")
    def test_assertEqual(self):
        self.assertEqual(1, 1)
        print("測試 test_assertEqual")
    def test_assertNotEqual(self):
        self.assertNotEqual(2, 1)
        print("測試 test_assertNotEqual")
    def test_assertTrue(self):
        self.assertTrue(True)
        print("測試 test_assertTrue")

# 在每次的測試前執行
# 測試 test_assertEqual
# .在每次的測試前執行
# 測試 test_assertNotEqual
# .在每次的測試前執行
# 測試 test_assertTrue
# .
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
# 
# OK