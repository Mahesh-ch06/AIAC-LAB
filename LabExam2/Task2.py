def is_palindrome(text: str) -> bool:
    """Check whether a string is a palindrome.

    Args:
        text (str): Input string.

    Returns:
        bool: True if text reads the same forward and backward, else False.
        
    Raises:
        TypeError: If the provided `text` is not a string or sliceable type.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Compare original and reversed
    return text == reversed_text


# Example usage
print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False
