# @classmethod
#     def tearDownClass():

import unittest
class TestSample(unittest.TestCase):
    @classmethod
    def tearDownClass(self):
        print("在全部的測試後執行")
    def test_assertEqual(self):
        self.assertEqual(1, 1)
        print("測試 test_assertEqual")

# 測試 test_assertEqual
# .在全部的測試後執行
# 
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# 
# OK