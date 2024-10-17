__all__ = ["GCD", "Fraction"]
from functools import total_ordering 
from decimal import *

getcontext().prec = 100

def GCD(num1, num2):
    '''
    Determines the Greatest Common Divisor of two numbers
    Args:
        num1(int): First number
        num2(int): Second number
    Returns:
        Greatest common divisor of the two numbers
    '''
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    return GCD(num2, num1 % num2)


@total_ordering  # decorator allows us to define only __eq__ and __lt__ and it does the rest!
class Fraction:
    '''
    Represents a fraction in the form n/d.
    '''    

    #===============================================================================
    # Special methods and overrides
    #===============================================================================
    def __init__(self, numerator = 0, denominator = 1):
        '''
        Initializer/constructor for Fraction.
        Args:
            self(Fraction): The object
            numerator(int): The numerator portion of the fraction
            denominator(int): The denominator portion of the coordinate (cannot be 0)
        '''
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
                
    def __str__(self):
        '''
        Converts this Fraction object to a string.
        Args:
            self(Fraction): The object
        '''
        return f"{self.numerator}/{self.denominator}"
        
    #===============================================================================
    # Properties (using descriptors)
    #===============================================================================
    class Numerator: 
        '''Numerator of a fraction'''
        def __get__(self, instance, owner):
            return instance.__numerator

        def __set__(self, instance, value):
            if (value == None) or (type(value) is not int):
                instance.__numerator = 0
            else:
                instance.__numerator = value

        def __delete__(self, instance):
            instance.__numerator = 0
            
    class Denominator: 
        '''Denominator of a fraction'''
        def __get__(self, instance, owner):
            return instance.__denominator

        def __set__(self, instance, value):
            if (value == None) or (type(value) is not int):
                instance.__denominator = 1
            else:
                if value == 0:
                    instance.__denominator = 1
                else:
                    if value < 0:
                        instance.numerator *= -1  # only apply sign to numerator
                    instance.__denominator = abs(value)

        def __delete__(self, instance):
            instance.__denominator = 1
    numerator = Numerator()
    denominator = Denominator()
        
    @property  # decorator for read access to value
    def value(self):
        '''
        float representation of the Fraction.
        Args:
            self(Fraction): The object
        Returns:
            Fraction value as a float
        '''
        prec = getcontext().prec
        getcontext().prec = 100
        num = Decimal(self.numerator)
        den = Decimal(self.denominator)
        val = num / den
        getcontext().prec = prec
        return val
        
    #===============================================================================
    # Operator Overloading
    #===============================================================================           
    def __add__(self, other):
        '''
        Adds two Fraction objects
        Args:
            self(Fraction): The object
            other(Fraction): The other Fraction to add to this one
        Returns:
            Result of adding this Fraction to other Fraction
        '''
        if other != None and type(other) is Fraction:
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        elif other != None and type(other) is int:
            return self + Fraction(other, 1)
        return self
    
    def __sub__(self, other):
        '''
        Subtracts two Fraction objects
        Args:
            self(Fraction): The object
            other(Fraction): The other Fraction to subtract from this one
        Returns:
            Result of subtracting other Fraction from this Fraction
        '''
        if other != None and type(other) is Fraction:
            return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
        elif other != None and type(other) is int:
            return self - Fraction(other, 1)
        return self
    
    def __mul__(self, other):
        '''
        Multiplies two Fraction objects
        Args:
            self(Fraction): The object
            other(Fraction): The other Fraction to multiply with this one
        Returns:
            Result of multiplying this Fraction with other Fraction
        '''
        if other != None and type(other) is Fraction:
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif other != None and type(other) is int:
            return self * Fraction(other, 1)
        return self
    
    def __div__(self, other):
        '''
        Divides two Fraction objects
        Args:
            self(Fraction): The object
            other(Fraction): The other Fraction to divide with
        Returns:
            Result of dividing this Fraction by other Fraction
        '''
        if other != None and type(other) is Fraction:
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif other != None and type(other) is int:
            return self / Fraction(other, 1)
        return self
    
    def __truediv__(self, other):
        '''
        Divides two Fraction objects
        Args:
            self(Fraction): The object
            other(Fraction): The other Fraction to divide with
        Returns:
            Result of dividing this Fraction by other Fraction
        Note:
            This is required for __future__.division
        '''
        # See: https://stackoverflow.com/questions/7075082/what-is-future-in-python-used-for-and-how-when-to-use-it-and-how-it-works
        if other != None and type(other) is Fraction:
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif other != None and type(other) is int:
            return self / Fraction(other, 1)
        return self
    
    def __eq__(self, other):
        '''
        Determines if two Fractions are equal
        Args:
            self(Fraction): The object
            other(Fraction): The other Fraction to compare
        Returns:
            True if this equals other, False otherwise
        '''
        if other != None and type(other) is Fraction:
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif other != None and type(other) is int:
            return self == Fraction(other, 1)
        return False
        
    def __lt__(self, other):
        '''
        Determines if one Fraction is less than another
        Args:
            self(Fraction): The object
            other(Fraction): The other Fraction to compare
        Returns:
            True if this is less than other, False otherwise
        '''
        if other != None and type(other) is Fraction:
            return self.value < other.value
        elif other != None and type(other) is int:
            return self.value < Fraction(other, 1)
        return False
    
    
    #===============================================================================
    # Methods
    #===============================================================================        
    def simplify(self):
        '''
        Simplifies the Fraction object
        Args:
            self(Fraction): The object
        '''
        gcd = GCD(abs(self.numerator), self.denominator)
        if gcd > 1:
            self.numerator = int(Decimal(self.numerator) / Decimal(gcd))
            self.denominator = int(Decimal(self.denominator) / Decimal(gcd))
            
    