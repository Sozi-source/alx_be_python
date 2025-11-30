import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ----------------- Addition Tests -----------------
    def test_addition(self):
        """Test the add method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    # ----------------- Subtraction Tests -----------------
    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-3, -7), 4)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    # ----------------- Multiplication Tests -----------------
    def test_multiplication(self):
        """Test the multiply method with various inputs."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    # ----------------- Division Tests -----------------
    def test_division(self):
        """Test the divide method with normal inputs."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)

    def test_division_by_zero(self):
        """Test dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    # ----------------- Optional: Mixed Type Tests -----------------
    def test_float_and_int_operations(self):
        """Test operations with mixed float and int values."""
        self.assertEqual(self.calc.add(2, 2.5), 4.5)
        self.assertEqual(self.calc.subtract(5.5, 2), 3.5)
        self.assertEqual(self.calc.multiply(3, 2.0), 6.0)
        self.assertEqual(self.calc.divide(7.5, 2), 3.75)

if __name__ == "__main__":
    unittest.main()
 
