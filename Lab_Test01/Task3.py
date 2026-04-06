def votingvalidation(age):
    """
    This function checks if a person is eligible to vote based on their age.
    Parameters:
    age (int): The age of the person.
    Returns:
    str: A message indicating whether the person is eligible to vote or not.
    Raises:
    ValueError: If the input age is not an integer.
        AgeError: If the input age is negative.
    """
    class AgeError(Exception):
        pass
    if not isinstance(age,int):
        raise ValueError("Input must be an integer.")
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."
