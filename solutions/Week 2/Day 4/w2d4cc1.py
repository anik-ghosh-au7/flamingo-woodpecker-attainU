class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        r = self.real + no.real
        i = self.imaginary + no.imaginary
        return Complex(r, i)

    def __sub__(self, no):
        r = self.real - no.real
        i = self.imaginary - no.imaginary
        return Complex(r, i)

    def __mul__(self, no):
        r = self.real * no.real - self.imaginary * no.imaginary
        i = self.real * no.imaginary + self.imaginary * no.real
        return Complex(r, i)

    def __truediv__(self, no):
        denominator = no.real ** 2 + no.imaginary ** 2
        r = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        i = (-self.real * no.imaginary + self.imaginary * no.real) / denominator
        return Complex(r, i)

    def mod(self):
        r = pow(self.real ** 2 + self.imaginary ** 2, 0.5)
        i = 0.00
        return Complex(r, i)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


a = Complex(2, 1)
b = Complex(5, 6)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.mod())
print(b.mod())

# -------------------------------------------------------------------------------------------------------------------------

# Explanation :

# a = 2.00+1.00i
# b = 5.00+6.00i

# addition

#   (2.00 + 1.00 i)
# + (5.00 + 6.00 i)
# =  7.00 + 7.00 i


# subtraction

#   (2.00 + 1.00 i)
# - (5.00 + 6.00 i)
# = -3.00 + 7.00 i


# multiplication

#   (2.00 + 1.00 i)
# * (5.00 + 6.00 i)
# = ((2.00 * 5.00)-(1.00 * 6.00)) + ((2.00 * 6.00)+(5.00 * 1.00)) i
# =  4.00 + 17.00 i


# division

#   (2.00 + 1.00 i)
# / (5.00 + 6.00 i)
# = (((2.00 * 5.00)+(1.00 * 6.00))/((5.00)^2 + (6.00)^2)) + ((-(2.00 * 6.00)+(1.00 * 5.00))/((5.00)^2 + (6.00)^2)) i
# =  0.26 - 0.11 i


# mod (a)

#  |(2.00 + 1.00 i)|
# = sq.rt((2.00)^2 + (1.00)^2)) + 0.00 i
# = 2.24 + 0.00 i

# mod (b)

#  |(5.00 + 6.00 i)|
# = sq.rt((5.00)^2 + (6.00)^2)) + 0.00 i
# = 7.81 + 0.00 i
