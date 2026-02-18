def DecimalToBinary(decimal):
    '''
    This function takes a decimal number as input and returns its binary representation as a string.
    >>> DecimalToBinary(10)
    '1010'
    >>> DecimalToBinary(0)
    '0'
    >>> DecimalToBinary(255)
    '11111111'
    >>> DecimalToBinary(5)
    '101'
    >>> DecimalToBinary(16)
    '1000'
    '''
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary
