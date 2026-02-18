'''write a function ArmstrongRange and demonstrate its working using Doctest'''
def ArmstrongRange(start, end):
    """
    This function returns a list of Armstrong numbers in the given range.

    >>> ArmstrongRange(1, 10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> ArmstrongRange(10, 100)
    [153]
    >>> ArmstrongRange(100, 1000)
    [153, 370, 371, 400]
    >>> ArmstrongRange(1, 1000)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
    """
    armstrong_numbers = []
    for num in range(start, end + 1):
        order = len(str(num))
        sum_of_digits = sum(int(digit) ** order for digit in str(num))
        if num == sum_of_digits:
            armstrong_numbers.append(num)
    return armstrong_numbers
