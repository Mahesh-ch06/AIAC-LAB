def is_armstrong_number(n):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that equals the sum of its digits raised to the power of the number of digits.
    >>> is_armstrong_number(153)  # 153 is an Armstrong number
    True
    >>> is_armstrong_number(154)  # 154 is not an Armstrong number
    False
    >>> is_armstrong_number(370)  # Armstrong number
    True
    >>> is_armstrong_number(371)  # Armstrong number
    True
    >>> is_armstrong_number(400)  # Not an Armstrong number
    False
    """
    order = len(str(n))
    sum_of_digits = sum(int(digit) ** order for digit in str(n))
    return n == sum_of_digits
