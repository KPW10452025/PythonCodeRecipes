# @classmethod
#     def setUpClass():

import unittest
class TestSample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("在全部的測試前執行")
    def test_assertEqual(self):
        self.assertEqual(1, 1)
        print("測試 test_assertEqual")

# 在全部的測試前執行
# 測試 test_assertEqual
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK