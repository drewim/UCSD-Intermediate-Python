from datetime import date

__all__ = ['isInt', 'isFloat', 'isDate']

def isInt(value: str) -> bool:
    """Takes a string as input and evaluates if it can be parsed to an Int data type.
    Returns a bool."""
    try:
        _ = int(value)
        return True
    except:
        return False
    
def isFloat(value: str) -> bool:
    """Takes a string, value as input, and evaluates if it can be parsed to a Float data type. 
    Returns a bool"""
    try:
        _ = float(value)
        return True
    except:
        return False
    
def isDate(value: str) -> bool:
    """EXTRA CREDIT. Accepts string and evaluates if it can be parsed to a datetime data type in ISO 
    serialization format (yyyy-mm-dd). Returns bool"""
    try:
        date.fromisoformat(value)
        return True
    except:
        return False

