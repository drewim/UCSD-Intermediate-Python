# Python II - Lab 1 - Drew Imhof

def part1() -> None:
    """ Take in user input and check if input is a palindrome and prints answer to screen """
    user_input: str = take_input(text= "Enter a string (palindrome): ")
    palindrome: bool = check_for_palindrome(user_input)
    print("Is '" + user_input + "'a palindrome? " + str(palindrome))

def check_for_palindrome(text: str) -> bool:
    """ Takes in a user-entered string and returns a bool of whether that string is a palindrome or not"""
    text: str = text.lower() # (A == a)
    text: str = text.replace(" ", "") # replace spaces to handle sentence-long palindromes
    reversed_text: str = ""
    for ch in text:
        if ch == " ": continue
        reversed_text: str = ch + reversed_text
        # print(reversed)
    return True if reversed_text == text else False

def part2() -> None:
    """ Score password based on length and type of characters contained. Prints string with password score to screen """
    password: str = take_input(text= "Enter a string (password): ")
    score: str = str(score_password(password))
    print("Your password score is: " + score)

def score_password(text: str) -> int:
    """ Takes in a password string and scores it based on its different characters and length.
    Returns an integer score from 0-7."""
    upper_flag: bool = 0
    lower_flag: bool = 0
    number_flag: bool = 0
    symbol_flag: bool = 0

    score: int = score_password_length(text)

    for ch in text:
        # uppercase test
        if ch.isupper() == True and upper_flag == 0:
            upper_flag = 1
            score += 1
        # lowercase test
        elif ch.islower() == True and lower_flag == 0:
            lower_flag = 1
            score += 1
        # number test
        elif ch in '0123456789' and number_flag == 0:
            number_flag = 1
            score += 1
        # symbol test
        elif ch in '!@#$%^&*' and symbol_flag == 0:
            symbol_flag = 1
            score += 1
    return score

def score_password_length(text: str) -> int:
    """ Takes in a string password and scores it based on the length"""
    score: int = 0
    text_length: int = len(text)
    if text_length >= 16:
        score += 3
    elif text_length > 8:
        score += 2
    elif text_length == 8:
        score += 1
    return score

def part3() -> None:
    """ Calculate compounded interest for entered principal,
     interest rate, and duration, then print in tabulated format """
    principal: float = float(take_input(text = "Enter principal amount (ex: 1000.00): "))
    apr: float = float(take_input(text = "Enter the interest rate percentage (ex: 4.5): "))
    term: int = int(take_input(text = "Enter the term in years (ex: 10): "))
    interest, balance = calculate_interest(principal, apr, term)
    print_tabulated_data(interest, balance, term)

def calculate_interest(amount: float, rate: float, years: int) -> list[float]:
    """ Calculates interest and resulting balance. Takes initial amount, rate, and time as input. 
    Returns a list of interest and balance for the given time frame."""
    interest: list = []
    balance: list = []
    current_balance: float = amount
    for x in range(years):
        interest.append( current_balance * rate/100)
        balance.append(current_balance + interest[x])
        current_balance = balance[-1]
    return interest, balance

def print_tabulated_data(interest: list[float], balance: list[float], years: int) -> None:
    """ Takes interest and balance list for given amount of years and prints them in a tabulated form"""
    text = ["Year", "Interest", "Balance"]
    print(f"{text[0]: ^4}" + f"{text[1]: >14}" + f"{text[2]: >16}")
    border = "=" * 34
    print(f"{border}")
    for x in range(years):
        print(f"{x+1: >4}" + f"  $ {interest[x]: >10,.2f}" + f"  $ {balance[x]: >12,.2f}")
    return

def take_input(text = "Enter a string: ") -> str:
    """ Prompts user to give input"""
    return input(text)

if __name__ == "__main__":
    part1()
    part2()
    part3()