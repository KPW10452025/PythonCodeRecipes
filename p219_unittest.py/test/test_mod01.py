import unittest
import sample_lib

class TestDmo(unittest.TestCase):
    def test_123(self):
        self.assertEqual(sample_lib.mod01.Addition(4, 2), 6)
    def test_234(self):
        self.assertEqual(sample_lib.mod01.Subtraction(4, 2), 2)
