from math import gcd
import unittest


class Fraction:
    """Class representing a fraction and operations on it.

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE: den != 0 (denominator must not be zero).
        POST: The fraction is stored in its reduced form (simplified).
        RAISE: ValueError if den == 0.
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        common_divisor = gcd(num, den)
        self.num = num // common_divisor
        self.den = den // common_divisor
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den

    @property
    def numerator(self):
        return self.num

    @property
    def denominator(self):
        return self.den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction.

        PRE: None.
        POST: Returns a string in the form 'a/b' or 'a' if b == 1.
        """
        return f"{self.num}/{self.den}" if self.den != 1 else f"{self.num}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number.

        A mixed number is the sum of an integer and a proper fraction.

        PRE: None.
        POST: Returns a string in the form 'integer part + proper fraction'.
        """
        integer_part = self.num // self.den
        remainder = abs(self.num % self.den)
        if remainder == 0:
            return str(integer_part)
        return f"{integer_part} + {remainder}/{self.den}" if integer_part != 0 else f"{remainder}/{self.den}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overload the + operator for fractions.

        PRE: other is a Fraction.
        POST: Returns a new Fraction representing the sum of self and other, in reduced form.
        RAISE: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overload the - operator for fractions.

        PRE: other is a Fraction.
        POST: Returns a new Fraction representing the difference between self and other, in reduced form.
        RAISE: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Overload the * operator for fractions.

        PRE: other is a Fraction.
        POST: Returns a new Fraction representing the product of self and other, in reduced form.
        RAISE: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        """Overload the / operator for fractions.

        PRE: other is a Fraction and other != 0.
        POST: Returns a new Fraction representing the division of self by other, in reduced form.
        RAISE: TypeError if other is not a Fraction.
               ZeroDivisionError if other equals 0.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Fraction(self.num * other.den, self.den * other.num)

    def __pow__(self, power):
        """Overload the ** operator for fractions.

        PRE: power is an integer.
        POST: Returns a new Fraction raised to the specified power, in reduced form.
        RAISE: TypeError if power is not an integer.
        """
        if not isinstance(power, int):
            raise TypeError("Power must be an integer.")
        return Fraction(self.num ** power, self.den ** power)

    def __eq__(self, other):
        """Overload the == operator for fractions.

        PRE: other is a Fraction.
        POST: Returns True if self and other are equivalent fractions, False otherwise.
        RAISE: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        return self.num == other.num and self.den == other.den

    def __float__(self):
        """Return the decimal value of the fraction.

        PRE: None.
        POST: Returns a float representing the fraction's value.
        """
        return self.num / self.den

    def __abs__(self):
        """Return the absolute value of the fraction.
        PRE: None.
        POST: Returns a new Fraction representing the absolute value of the fraction.
        """
        new_num = abs(self.num)
        new_den = abs(self.den)
        return Fraction(new_num, new_den)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if the fraction's value is 0.

        PRE: None.
        POST: Returns True if the fraction is 0, False otherwise.
        """
        return self.num == 0

    def is_integer(self):
        """Check if the fraction is an integer (e.g., 8/4, 3, 2/2, ...).

        PRE: None.
        POST: Returns True if the fraction is an integer, False otherwise.
        """
        return self.num % self.den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1.

        PRE: None.
        POST: Returns True if the fraction is proper, False otherwise.
        """
        return abs(self.num) < self.den

    def is_unit(self):
        """Check if the fraction's numerator is 1 in its reduced form.

        PRE: None.
        POST: Returns True if the numerator is 1 in its reduced form, False otherwise.
        """
        return self.num == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction.

        Two fractions are adjacent if the absolute value of the difference between them is a unit fraction.

        PRE: other is a Fraction.
        POST: Returns True if the fractions are adjacent, False otherwise.
        RAISE: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        return  abs(self - other).is_unit()


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
