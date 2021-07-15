#   def setUp():

import unittest
class TestSample(unittest.TestCase):

    Sample01 = 0

    def setUp(cls):
        TestSample.Sample01 += 1

    def test_assertEqual(self):
        self.assertEqual(1, 1)
        Sample02 = TestSample.Sample01
        print("測試 test_assertEqual")
        print(Sample02)
        
    def test_assertNotEqual(self):
        self.assertNotEqual(2, 1)
        Sample03 = TestSample.Sample01
        print("測試 test_assertNotEqual")
        print(Sample03)

    def test_assertTrue(self):
        self.assertTrue(True)
        Sample04 = TestSample.Sample01
        print("測試 test_assertTrue")
        print(Sample04)

# 測試 test_assertEqual
# 1
# .測試 test_assertNotEqual
# 2
# .測試 test_assertTrue
# 3
# .
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
# 
# OK