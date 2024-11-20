import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        sum_real = round(self.real + no.real, 2)
        sum_img =  round(self.imaginary + no.imaginary,2)
        return Complex(sum_real, sum_img)
    
    def __sub__(self, no):
        sub_real = round(self.real - no.real, 2)
        sub_img = round(self.imaginary - no.imaginary, 2)
        return Complex(sub_real, sub_img)
    
    def __mul__(self, no):
        mul_real = round(self.real*no.real - self.imaginary*no.imaginary, 2)
        mul_img = round(self.real*no.imaginary + self.imaginary*no.real, 2)
        return Complex(mul_real, mul_img)
    
    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)    
    
    def __truediv__(self, no):
        mod_no = no.mod()
        mod = mod_no.real**2
        real_part = self.real*no.real + self.imaginary*no.imaginary
        imag_part = self.imaginary*no.real - self.real*no.imaginary
        return Complex(real_part/mod, imag_part/mod)

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


comp1 = Complex(3, 2)
comp2 = Complex(4, 5)
print("Complex number 1: ", comp1)
print("Complex number 2: ", comp2)
comp3 = comp1 + comp2
print("The + of complex number 1 and complex number 2 is:\n", comp3)
comp4 = comp1 - comp2
print("The - of complex number 1 and complex number 2 is:\n", comp4)
comp5 = comp1 * comp2
print("The * of complex number 1 and complex number 2 is:\n", comp5)
comp6 = comp1 / comp2
print("The / of complex number 1 and complex number 2 is:\n", comp6)
print("The module of complex number 1 and complex number 2 number are:", comp1.mod(),"and", comp2.mod())
#print("%.2f" % sum_real + " + " + "%.2f" % sum_img + "i")

