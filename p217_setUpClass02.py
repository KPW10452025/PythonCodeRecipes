# @classmethod
#     def setUpClass():

import unittest
class TestSample(unittest.TestCase):

    Sample01 = None # 定義變量 Sample01

    @classmethod                        # classmethod 裝飾器
    def setUpClass(cls):                # 定義 setUpClass() 方法
        TestSample.Sample01 = 3.1415926 # 對類屬性 Sample01 賦值

    def test_assertEqual(self):
        Sample02 = TestSample.Sample01  # 類名.屬性：調用使用
        print(Sample02)

# 3.1415926
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# 
# OK

# 由結果可以發現，一開始設定的 Sample01 為 None。
# 因為 setUpClass 最優先執行，使得 TestSample.Sample01 = 3.1415926
# 之後 Sample02 = TestSample.Sample01
# 所以 print(Sample02) 可以得到 3.1415926