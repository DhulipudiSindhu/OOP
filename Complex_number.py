Complex Numbers
# Submission Guidelines
Create a folder /home/ec2-user/environment/oop_submissions/oop_asssignment_004. Make use of the below example command
```shell
$ mkdir -p /home/ec2-user/environment/oop_submissions/oop_asssignment_004/


-   Copy your code file to the submission folder. Make use of the below example command

```shell
$ cp complex_number.py /home/ec2-user/environment/oop_submissions/oop_assignment_004/

Complex Number: A complex number is a number that can be expressed in the form a + bi, where a is real part and b is imaginary part

In this assignment you need to write a ComplexNumber class which behaves similar to complex number

Coding Guidelines:

Write all your code in complex_number.py file
Note: Don’t use any Complex Number libraries in python.
You can refer internet for list of magic methods & square root function in math library.
Hints :

For Addition, Subtraction, Multiplication, Division and Equality use magic methods
For calculating square root, use math library
# Task 1 : Instantiation
Your ComplexNumber class should represent the complex numbers.
Real and imaginary parts should be either integers or floats.

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> one_plus_two_i.real_part
1
>>> one_plus_two_i.imaginary_part
2


>>> from complex_number import ComplexNumber
>>> one = ComplexNumber(1)
>>> one.real_part
1
>>> one.imaginary_part
0


>>> from complex_number import ComplexNumber
>>> zero = ComplexNumber()
>>> zero.real_part
0
>>> zero.imaginary_part
0


>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber("1", 2)
ValueError: Invalid value for real part


>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,"2")
ValueError: Invalid value for imaginary part


>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber("1","2")
ValueError: Invalid value for real and imaginary part


# Task 2: Print
Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> print(one_plus_two_i)
1+2i

# Task 3: Conjugate
Your ComplexNumber class should contain conjugate method that return conjugate of the complex_number

Example for conjugate:
Conjugate for complex number 1 + 2i is 1 - 2i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> one_minus_two_i = one_plus_two_i.conjugate()
>>> print(one_plus_two_i)
1+2i
>>> print(one_minus_two_i)
1-2i

# Task 4: Addition
When adding complex number instances using + operator it should return a complex number object

Example for addition:
1 + 2i + 2 + 3i = 3 + 5i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> three_plus_four_i = ComplexNumber(3,4)
>>> four_plus_six_i = one_plus_two_i + three_plus_four_i
>>> print(four_plus_six_i)
4+6i

# Task 5: Subtraction
When subtracting complex number instance using - operator it should return a complex number object.

Example for Subtraction
2 + 2i - 1 + 1i = 1 + 1i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> three_plus_four_i = ComplexNumber(3,4)
>>> two_plus_two_i = three_plus_four_i - one_plus_two_i
>>> print(two_plus_two_i)
2+2i

# Task 6: Multiplication
When multiplying complex number instances using * operator, it should return multiplication of complex number instances
Example for Multiplication
1+2i * 3+4i = -5+10i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> three_plus_four_i = ComplexNumber(3,4)
>>> minus_five_plus_ten_i = one_plus_two_i * three_plus_four_i
>>> print(minus_five_plus_ten_i)
-5+10i

# Task 7: Division
When dividing two complex number instances using / operator, it should return a complex number object.

Example for Division
1+2i / 3+4i = -0.44+0.08i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> three_plus_four_i = ComplexNumber(3,4)
>>> point_four_four_plus_point_zero_eight_i = one_plus_two_i / three_plus_four_i
>>> print(point_four_four_plus_point_zero_eight_i)
0.44+0.8i

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> zero = ComplexNumber()
>>> one_plus_two_i / zero
ZeroDivisionError: division by zero

# Task 8: Absolute
Your ComplexNumber class should return absolute of the complex number (Rounded to 3 decimal places)

Example for Absolute
absolute of 1+2i is 2.236 ( sqrt(1 ^2 + 2 ^2) )

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> absolute_value = abs(one_plus_two_i)
>>> absolute_value
2.236


# Task 9: Equality
When comparing complex number instances using ==, it should return True when instances are equal otherwise return False

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> Complex(1,2) == ComplexNumber(1,2)
True
>>> Complex(2,1) == ComplexNumber(1,2)
False




import math
class ComplexNumber:
    def __init__(self, real_part = 0, imaginary_part = 0):
        if type(real_part) == str and type(imaginary_part) == str:
            raise ValueError("Invalid value for real and imaginary part")
            
        if type(real_part) == str:
            raise ValueError("Invalid value for real part")
        
        self.real_part = real_part
            
        if type(imaginary_part) == str:
            raise ValueError("Invalid value for imaginary part")
        
        self.imaginary_part = imaginary_part
   
   
    def __str__(self):
        return f'{self.real_part}{self.imaginary_part:+}i'
        
    def conjugate(self):
        return ComplexNumber(self.real_part, -self.imaginary_part)
        
    def __add__(self, other):
        self.add_real = self.real_part + other.real_part
        self.add_img = self.imaginary_part + other.imaginary_part
        return ComplexNumber(self.add_real, self.add_img)
    
    def __sub__(self, other):
        return ComplexNumber(self.real_part - other.real_part, self.imaginary_part - other.imaginary_part)
    
    def __mul__(self, other):
        mul_real = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
        mul_imaginary = (self.real_part * other.imaginary_part) + (other.real_part * self.imaginary_part)
        return ComplexNumber(mul_real, mul_imaginary)
        

    def __truediv__(self, other):
        k = math.sqrt((other.real_part ** 2) + (other.imaginary_part ** 2))
        div_real = round(((self.real_part/k) * (other.real_part/k)) + ((self.imaginary_part/k) * (other.imaginary_part/k)), 2)
        div_img = round(((self.real_part/k) * (- other.imaginary_part/k) + (self.imaginary_part/k) * (other.real_part/k)),2)
        return ComplexNumber(div_real, div_img)
       
       
    def __abs__(self):
        return (round(math.sqrt(self.real_part ** 2 + self.imaginary_part ** 2),3))
        
    def __eq__(self, other):
        
