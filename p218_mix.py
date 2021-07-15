# setUp
# setUpClass
# tearDown
# tearDownClass

import unittest

class SampleTest(unittest.TestCase):

    Sample01 = 0

    @classmethod
    def setUpClass(cls):
        SampleTest.Sample01 += 10
        print(SampleTest.Sample01)

    @classmethod
    def tearDownClass(cls):
        SampleTest.Sample01 -= 10
        print(SampleTest.Sample01)

    def setUp(cls):
        SampleTest.Sample01 *= 2
        print(SampleTest.Sample01)

    def tearDown(cls):
        SampleTest.Sample01 *= 3
        print(SampleTest.Sample01)

    def test_assertEqual(self):
        self.assertEqual(1, 1)
        print("測試 test_assertEqual")
        print(SampleTest.Sample01)

    def test_assertNotEqual(self):
        self.assertNotEqual(2, 1)
        print("測試 test_assertNotEqual")
        print(SampleTest.Sample01)

    def test_assertTrue(self):
        self.assertTrue(True)
        print("測試 test_assertTrue")
        print(SampleTest.Sample01)

# 10                        Sample01 = 0 最一開始測試會 + 10 
# 20                        每次測試前 * 2
# 測試 test_assertEqual
# 20
# 60                        每次測試後 * 3
# .120                      每次測試前 * 2
# 測試 test_assertNotEqual
# 120
# 360                       每次測試後 * 3
# .720                      每次測試前 * 2
# 測試 test_assertTrue
# 720
# 2160                      每次測試後 * 3
# .2150                     完成測試後 - 10
# 
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
# 
# OK
