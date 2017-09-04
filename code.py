from math import sqrt, pi, atan, sin, cos, log

class ComplexNumber:
    """
    The class of complex numbers.
    """
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary part.
        """
        self.real = real_part
        self.imaginary = imaginary_part
    def __repr__(self):
        """
        Return the string representation of self.
        """
        return "%s + %s i"%(self.real, self.imaginary)
    def __eq__(self, other):
        """
        Test if ``self`` equals ``other``.
        
        Two complex numbers are equal if their real parts are equal and
        their imaginary parts are equal.
        """
        return self.real == other.real and self.imaginary == other.imaginary
    def modulus(self):
        """
        Return the modulus of self.
        
        The modulus (or absolute value) of a complex number is the square
        root of the sum of squares of its real and imaginary parts.
        """
        return sqrt(self.real**2 + self.imaginary**2)
    def sum(self, other):
        """
        Return the sum of ``self`` and ``other``.
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    def product(self, other):
        """
        Return the product of the ``self`` and the ``other``.
        """
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary), (self.real * other.imaginary + self.imaginary * other.real))
    def complex_conjucate(self):
        """
        Replace in-place ``self`` with its complex conjucate.
        """
        self.imaginary = -1 * self.imaginary


class NonZeroComplexNumber(ComplexNumber):
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary parts after checking validity.
        """
        if real_part == 0 and imaginary_part == 0:
            raise ValueError("Real or imaginary part should be nonzero.")
        return ComplexNumber.__init__(self, real_part, imaginary_part)
    def inverse(self):
        """
        Return the multiplicative inverse of ``self``.
        """
        den = self.real**2 + self.imaginary**2
        return NonZeroComplexNumber(self.real/den, -self.imaginary/den)
    def polar_coordinates(self):
        """
        Return the polar coordinate of the ``self``.
        """
        if self.real == 0:
            theta = pi/2
        else:
            theta = atan(float(self.imaginary)/float(self.real))
        r = sqrt(self.real**2 + self.imaginary**2)
        return (r, theta)
    def logarithm(self):
        """
        Return the logarithm of the complex number.
        """
        r , theta = self.polar_coordinates()
        return NonZeroComplexNumber(log(r), theta)


#TEST product method of class ComplexNumber
c = ComplexNumber(2,3)
print (c.product(ComplexNumber(1,2)) == ComplexNumber(-4,7))

#TEST complex_conjucate method of class ComplexNumber
c.complex_conjucate()
print (c == ComplexNumber(2, -3))

#TEST logarith method of class NonZeroComplexNumber 
n = NonZeroComplexNumber(3,4)
print (n.logarithm() == ComplexNumber(1.6094379124341003, 0.9272952180016122))

