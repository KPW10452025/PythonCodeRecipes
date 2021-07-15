# @classmethod
#     def tearDownClass():

import unittest
class TestSample(unittest.TestCase):

    Sample01 = None

    @classmethod
    def tearDownClass(self):
        TestSample.Sample01 = 1.41421
    
    def test_assertEqual(self):
        Sample02 = TestSample.Sample01
        print(Sample02)

# None
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# 
# OK

# 由結果可以發現，一開始設定的 Sample01 為 None。
# 因為 setUpClass 最後執行
# 此時會跳過
# @classmethod
# def tearDownClass(self):
#     TestSample.Sample01 = 1.41421
# 所以此時的 TestSample.Sample01 仍然是 None
# 之後 Sample02 = TestSample.Sample01
# 所以 print(Sample02) 得到的是 None