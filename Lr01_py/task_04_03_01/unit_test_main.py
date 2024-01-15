import unittest
from roman import Roman

class RomanTestCase(unittest.TestCase):
    def test_init_with_roman(self):
        r = Roman("X")
        self.assertEqual(r.arabic, 10)

    def test_init_with_arabic(self):
        r = Roman(5)
        self.assertEqual(str(r), "V")

    def test_init_with_invalid_value(self):
        with self.assertRaises(TypeError):
            r = Roman(3.14)

    def test_addition(self):
        r1 = Roman("X")
        r2 = Roman(5)
        result = r1 + r2
        self.assertEqual(result.arabic, 15)
        self.assertEqual(str(result), "XV")

    def test_subtraction(self):
        r1 = Roman("X")
        r2 = Roman(5)
        result = r1 - r2
        self.assertEqual(result.arabic, 5)
        self.assertEqual(str(result), "V")

    def test_multiplication(self):
        r1 = Roman("X")
        r2 = Roman(5)
        result = r1 * r2
        self.assertEqual(result.arabic, 50)
        self.assertEqual(str(result), "L")

    def test_floor_division(self):
        r1 = Roman("X")
        r2 = Roman(5)
        result = r1 // r2
        self.assertEqual(result.arabic, 2)
        self.assertEqual(str(result), "II")

    def test_to_arabic(self):
        result = Roman.to_arabic("MMXVI")
        self.assertEqual(result, 2016)

    def test_to_roman(self):
        result = Roman.to_roman(2016)
        self.assertEqual(result, "MMXVI")

if __name__ == "__main__":
    unittest.main()
