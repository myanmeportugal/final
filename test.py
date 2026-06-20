import main
import unittest

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)
        self.assertEqual(main.add(-1, -5), -6)

if __name__ == "__main__":
    unittest.main()