import example
import unittest


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(3, 4), 7)

    def test_sub_1(self):
        self.assertEqual(example.subtract(4, 3), 1)

    def test_mul_1(self):
        self.assertEqual(example.mulityply(3, 4), 12)

    def test_div_1(self):
        self.assertEqual(example.divide(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
