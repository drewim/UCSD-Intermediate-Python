from Fraction import *
from decimal import *
from functools import reduce

class LeibnizPiIterator:
    def __init__(self) -> None:
        pass

    def __iter__(self):
        self.fraction = Fraction(numerator = 0, denominator= 1)
        self.n: int = 1
        self.add_next: bool = True
        return self
    
    def __next__(self):
        if self.add_next:
             self.fraction += Fraction(numerator = 4, denominator = self.n)
        else:
            self.fraction -= Fraction(numerator = 4, denominator = self.n)
        self.add_next = not self.add_next
        self.n += 2
        return self.fraction.value
    
def NilakanthaPiGenerator():
    fraction = Fraction(numerator=3, denominator=1)
    num = 2
    add_next = True
    yield fraction
    while True:
        operand = Fraction(numerator=4, denominator= (num * (num + 1) * (num + 2)))
        fraction = fraction + operand if add_next else fraction - (operand)
        add_next = not add_next
        num += 2
        yield fraction.value

def compose(*functions): 
    return reduce(lambda f, g: lambda x: g(f(x)), functions) 

def milesToYards(value) -> float:
    return value * 1760

def yardsToMiles(value) -> float:
    return value * 0.0005681818181818 

def yardsToFeet(value) -> float:
    return value * 3 

def feetToYards(value) -> float:
    return value * 0.3333333333333333 

def feetToInches(value) -> float:
    return value * 12

def inchesToFeet(value) -> float:
    return value * 0.0833333333333333

def inchesToCm(value) -> float:
    return value * 2.54

def cmToInches(value) -> float:
    return value * 0.3937007874015748 

def cmToMeters(value) -> float:
    return value * 0.01

def metersToCm(value) -> float:
    return value * 100

def metersToKm(value) -> float:
    return value * .001

def kmToMeters(value) -> float:
    return value * 1000

def kmToAu(value) -> float:
    return value * 0.000000006684587122268445

def auToKm(value) -> float:
    return value * 149597870.700

def auToLy(value) -> float:
    return value * 0.00001581250740982065847572

def lyToAu(value) -> float:
    return value * 63241.07708426628026865358

def mmToCm(value) -> float:
    return value * 0.1

def cmToMm(value) -> float:
    return value * 10

def mmToUm(value) -> float:
    return value * 1000

def umToMm(value) -> float:
    return value * (1/1000)

def umToAngstrom(value) -> float:
    return value * 10000

def angstromToUm(value) -> float:
    return value * (1/10000)

if __name__ == '__main__':
    def iterate(func, iterations: int = 100000, pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")):
        for i, x in enumerate(func()) :
            result = x
            if i % 100000 == 0: print(f"iterations = {i:,}, {x}")
            if i > iterations: break
        print(f"pi after {iterations} iterations: {result: .50f}")
        print(f"Difference: {abs(pi50 - result): 0.50f}")

    pi50 = Decimal("3.14159265358979323846264338327950288419716939937510") 
    iterations = 1000000 

    # iterate(func = LeibnizPiIterator, iterations=100000)
    # iterate(func = LeibnizPiIterator, iterations=10000000)
    # iterate(func = NilakanthaPiGenerator, iterations=100000)
    # iterate(func = NilakanthaPiGenerator, iterations=10000000)

    milesToFeet = compose(milesToYards, yardsToFeet, feetToInches)
    print(milesToFeet(2))
    feetToMeters = compose(feetToInches, inchesToCm, cmToMeters)
    print(feetToMeters(5))
    metersToInches = compose(metersToCm, cmToInches)
    print(metersToInches(1))
    milesToKm = compose(milesToYards, yardsToFeet, feetToInches, inchesToCm, cmToMeters, metersToKm)
    print(milesToKm(10))
    kmToMiles = compose(kmToMeters, metersToCm, cmToInches, inchesToFeet, feetToYards, yardsToMiles)
    print(kmToMiles(1))
    kmToInches = compose(kmToMeters, metersToCm, cmToInches)
    print(kmToInches(12.7))
    inchesToKm = compose(inchesToCm, cmToMeters, metersToKm)
    print(inchesToKm(500000))
    metersToLy = compose(metersToKm, kmToAu, auToLy)
    print(metersToLy(9460730472580800))
    angstromToMeters = compose(angstromToUm, umToMm, mmToCm, cmToMeters)
    print(angstromToMeters(1))
    mileToAngstrom = compose(milesToYards, yardsToFeet, feetToInches, inchesToCm, cmToMm, mmToUm, umToAngstrom)
    print(mileToAngstrom(1))