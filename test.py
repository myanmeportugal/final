import main
import unittest


class TestCalculator(unittest.TestCase):

    def test_add_true(self):
        result = main.add(10, 5)
        self.assertTrue(result == 15)

    def test_sub_false(self):
        result = main.sub(10, 5)
        self.assertFalse(result == 100)

    def test_mul_true(self):
        result = main.mul(10, 5)
        self.assertTrue(result == 50)

    def test_div_by_zero_true(self):
        result = main.div(10, 0)
        self.assertTrue(result == "Invalid! Can't divide by zero!")

    def test_div_by_bigger_false(self):
        result = main.div(5, 10)
        self.assertTrue(
            result == "Invalid! Can't divide small number by greater number!"
        )


if __name__ == "__main__":
    unittest.main()