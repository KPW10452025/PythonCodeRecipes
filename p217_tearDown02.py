#   def tearDown():

import unittest
class TestSample(unittest.TestCase):

    Sample01 = 0

    def tearDown(cls):
        TestSample.Sample01 += 1

    def test_assertEqual(self):
        self.assertEqual(1, 1)
        print("測試 test_assertEqual")
        Sample02 = TestSample.Sample01
        print(Sample02)

    def test_assertNotEqual(self):
        self.assertNotEqual(2, 1)
        print("測試 test_assertNotEqual")
        Sample03 = TestSample.Sample01
        print(Sample03)

    def test_assertTrue(self):
        self.assertTrue(True)
        print("測試 test_assertTrue")
        Sample04 = TestSample.Sample01
        print(Sample04)

# 測試 test_assertEqual
# 0
# .測試 test_assertNotEqual
# 1
# .測試 test_assertTrue
# 2
# .
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
# 
# OK
