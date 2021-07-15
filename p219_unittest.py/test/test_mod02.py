import unittest
import sample_lib

class TestDmo(unittest.TestCase):
    def test_345(self):
        self.assertEqual(sample_lib.mod02.Multiplication(4, 2), 8)
    def test_456(self):
        self.assertEqual(sample_lib.mod02.Division(4, 2), 2)