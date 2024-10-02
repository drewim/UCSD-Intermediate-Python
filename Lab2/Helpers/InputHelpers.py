__all__ = ['inputInt', 'inputFloat', 'inputString', 'inputDate']

from Helpers.DataTypeHelpers import *
from datetime import date

def inputInt(prompt: str = "Enter an integer: ", min_value = 0, max_value = 100) -> int:
    """Displays a prompt to take in a value. Loop until entry is an int"""
    validInputEntered: bool = 0
    while validInputEntered == 0:
        value: str = input(prompt)
        if isInt(value):
            integerValue: int = int(value)
            if not isValidEntry(integerValue, min_value, max_value):
                print(f"{integerValue} is out of range. Please enter a value between {min_value} and {max_value}")
                continue
        else: 
            print(f"Invalid entry: {value}. Input needs to be in the int format.")
            continue
        validInputEntered = 1
    return integerValue

def inputFloat(prompt: str = "Enter a float: ", min_value = 0, max_value = 100) -> float:
    """Prompts user to enter a float. Loops until valid entry is made and returns float"""
    validInputEntered: bool = 0
    while validInputEntered == 0:
        value: str = input(prompt)
        if isFloat(value):
            floatValue: float = float(value)
            if not isValidEntry(floatValue, min_value, max_value):
                print(f"{floatValue} is out of range. Please enter a value between {min_value} and {max_value}")
                continue
        else:
            print(f"Invalid entry: {value}. Input needs to be in the float format. Try again.")
            continue
        validInputEntered = 1
    return floatValue

def inputString(prompt: str = "Enter a string: ", min_length: int = 0, max_length: int = 100) -> str:
    """Prompts user to enter a string. Loops until a valid entry is made and returns the valid string"""
    validStringEntered: bool = 0
    while validStringEntered == 0:
        value: str = input(prompt)
        if not isValidStringLength(value, min_length, max_length):
            print(f"Str length {len(value)} for input {value} is out of range. Length must be between {min_length} and {max_length}")
            continue
        validStringEntered = 1
    return value

def inputDate(prompt: str = "Enter a date in ISO format (yyyy-mm-dd): "):
    """Prompts user to enter date in ISO format. When valid entry is made, date is returned"""
    validDateEntered: bool = 0
    while validDateEntered == 0:
        value: str = input(prompt)
        if not isDate(value):
            print(f"{value} needs to be in \"yyyy-mm-dd\" format. Try again")
            continue
        validDateEntered = 1
    return date.fromisoformat(value)


def isValidEntry(value, min_value, max_value) -> bool:
    """Check if value entered lies between the min and max values, inclusively"""
    return True if value >= min_value and value <= max_value else False

def isValidStringLength(value: str, min_length: int, max_length: int) -> bool:
    """Check if string falls between min_length and max_length and return bool"""
    return True if len(value) >= min_length and len(value) <= max_length else False


if __name__ == '__main__':
    print(inputString(min_length=1, max_length=10))
    # print(inputDate())