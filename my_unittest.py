import unittest
from libs.fraction.fraction import Fraction


class FractionTestCase(unittest.TestCase):
    def test_fraction_init(self):
        self.assertRaises(ValueError, Fraction, 1, 0)
        self.assertEqual(Fraction(3, 6).__str__(), "1/2", "Fraction(3, 6)")
        self.assertEqual(Fraction(-1, -1).__str__(), "1", "Fraction(-1, -1)")
        self.assertEqual(Fraction(2, -9).__str__(), "-2/9", "Fraction(2, -9)")
        self.assertEqual(Fraction(-10, 2).__str__(), "-5", "Fraction(-10, 2)")

    def test_fraction_str(self):
        self.assertEqual(str(Fraction(3, 6)), "1/2", "str(Fraction(3, 6))")

    def test_fraction_as_mixed_number(self):
        self.assertEqual(Fraction(10, 3).as_mixed_number(), "3 + 1/3", "Fraction(10, 3).as_mixed_number()")
        self.assertEqual(Fraction(1, 3).as_mixed_number(), "1/3", "Fraction(1, 3).as_mixed_number()")

    def test_fraction_add(self):
        self.assertRaises(TypeError, Fraction(1, 8).__add__, "hello")
        self.assertEqual(Fraction(1, 2) + Fraction(5, 8), Fraction(9, 8), "Fraction(1, 2) + Fraction(5, 8)")

    def test_fraction_sub(self):
        self.assertRaises(TypeError, Fraction(1, 8).__sub__, "hello")
        self.assertEqual(Fraction(1, 2) - Fraction(5, 8), Fraction(-1, 8), "Fraction(1, 2) - Fraction(5, 8)")

    def test_fraction_mul(self):
        self.assertRaises(TypeError, Fraction(1, 8).__mul__, "hello")
        self.assertEqual(Fraction(1, 2) * Fraction(5, 8), Fraction(5, 16), "Fraction(1, 2) * Fraction(5, 8)")

    def test_fraction_truediv(self):
        self.assertRaises(TypeError, Fraction(1, 8).__truediv__, "hello")
        self.assertRaises(ZeroDivisionError, Fraction(1, 2).__truediv__, Fraction(0, 5))
        self.assertEqual(Fraction(1, 2) / Fraction(5, 8), Fraction(4, 5), "Fraction(1, 2) / Fraction(5, 8)")

    def test_fraction_pow(self):
        self.assertRaises(TypeError, Fraction(1, 8).__pow__, "hello")
        self.assertEqual(Fraction(1, 2) ** 7, Fraction(1, 128), "Fraction(1, 2) ** 7")

    def test_fraction_eq(self):
        self.assertRaises(TypeError, Fraction(1, 8).__eq__, "hello")
        self.assertEqual(Fraction(1, 2), Fraction(3, 6), "Fraction(1, 2) == Fraction(3, 6)")

    def test_fraction_float(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5, "float(Fraction(1, 2))")

    def test_fraction_abs(self):
        self.assertEqual(abs(Fraction(1, -2)), Fraction(1, 2), "abs(Fraction(1, -2))")

    def test_fraction_is_zero(self):
        self.assertTrue(Fraction(0, 7).is_zero(), "Fraction(0, 7) is zero")

    def test_fraction_is_integer(self):
        self.assertTrue(Fraction(12, 6).is_integer(), "Fraction(12, 6) is integer")

    def test_fraction_is_proper(self):
        self.assertTrue(Fraction(1, 3).is_proper(), "Fraction(1, 3) is proper")

    def test_fraction_is_unit(self):
        self.assertTrue(Fraction(1, 3).is_unit(), "Fraction(1, 3) is unit")

    def test_fraction_is_adjacent_to(self):
        self.assertRaises(TypeError, Fraction(1, 3).is_adjacent_to, "hello")
        self.assertTrue(Fraction(1, 3).is_adjacent_to(Fraction(1, 4)), "Fraction(1, 3) is adjacent to Fraction(1, 4)")


if __name__ == '__main__':
    unittest.main()

