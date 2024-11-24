from math import gcd


class Fraction:
    """Class representing a fraction and operations on it.

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE: num and den must be integers.
        POST: The fraction is stored in its reduced form (simplified).
        RAISE: ZeroDivisionError if den == 0.
        """
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
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
        """
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overload the - operator for fractions.

        PRE: other is a Fraction.
        POST: Returns a new Fraction representing the difference between self and other, in reduced form.
        """
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Overload the * operator for fractions.

        PRE: other is a Fraction.
        POST: Returns a new Fraction representing the product of self and other, in reduced form.
        """
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        """Overload the / operator for fractions.

        PRE: other is a Fraction and other != 0.
        POST: Returns a new Fraction representing the division of self by other, in reduced form.
        RAISE: ZeroDivisionError if other equals 0.
        """
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Fraction(self.num * other.den, self.den * other.num)

    def __pow__(self, power):
        """Overload the ** operator for fractions.

        PRE: power is an integer.
        POST: Returns a new Fraction raised to the specified power, in reduced form.
        """
        return Fraction(self.num ** power, self.den ** power)

    def __eq__(self, other):
        """Overload the == operator for fractions.

        PRE: other is a Fraction.
        POST: Returns True if self and other are equivalent fractions, False otherwise.
        """
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
        """ 
        return  abs(self - other).is_unit()



