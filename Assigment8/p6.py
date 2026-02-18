def is_armstrong_number(n):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that equals the sum of its digits raised to the power of the number of digits.
    >>> is_armstrong_number(153)
    True
    >>> is_armstrong_number(153)
    False
    >>> is_armstrong_number(370)
    True
    >>> is_armstrong_number(371)
    True
    >>> is_armstrong_number(400)
    False
    """
    order = len(str(n))
    sum_of_digits = sum(int(digit) ** order for digit in str(n))
    return n == sum_of_digits
