def evenoddchecker(num: int) -> str:
    """Return 'Even' if the number is even, otherwise 'Odd'.

    Parameters:
        num (int): The number to check.

    Returns:
        str: 'Even' if the number is even, otherwise 'Odd'.
    """
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    print(evenoddchecker.__doc__)