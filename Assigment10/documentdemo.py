"""documentdemo module.

This module demonstrates how to write documentation for Python code.
It provides utility functions for basic arithmetic operations.
"""


def add(a, b):
    """Return the sum of two numbers.

    Parameters:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: Sum of ``a`` and ``b``.
    """
    return a + b


def sum_1_to_10():
    """Return the sum of numbers from 1 to 10.

    Returns:
        int: Sum of values from 1 through 10.
    """
    total = 0
    for number in range(1, 11):
        total = add(total, number)
    return total
