import math

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

    def is_pass(self):
        return self.grade >= 50

student1 = Student("Alice", 16, 75)
student1.display_info()
print("Passed:", student1.is_pass())

#Q1.1 Attributes of the Student class:
"""
name,age and grade
"""
#Q1.2 Purpose of the is_pass() method:
"""
To check if the student's grade is 50 or above.
"""
#Q1.3 Output of student1.is_pass():
"""
True
"""

# Q2,Q3 Fraction class implementation:
class Fraction :
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        # Ensure denominator is positive
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        # Reduce the fraction
        common_divisor = math.gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def display(self):
        print(f"{self.numerator}/{self.denominator}")

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

f= Fraction(1, 2)
f.display()  # Output: 1/2

# Test cases for reduced form and negative denominator
f1 = Fraction(4, 12)
print(f1)  # Output: 1/3
f2 = Fraction(6, -9)
print(f2)  # Output: -2/3
f3 = Fraction(-3, 8)
print(f3)  # Output: -3/8