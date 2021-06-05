import example
import unittest


class TestCase(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(example.add(3,4), 7)


if __name__ == '__main__':
    unittest.main()
