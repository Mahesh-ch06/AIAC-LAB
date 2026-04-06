# write a function using pydoc for documentation that checks if the user can login with the given credentials.
def login(user,password,credentials):
    """Check if the user can login with the given credentials.

    Parameters:
        user (str): The username of the user.
        password (str): The password of the user.
        credentials (dict): A dictionary containing valid username-password pairs.
    Returns:
        bool: True if the user can login, False otherwise.
    """
    if user in credentials and credentials[user] == password:
        return True
    return False
# Example usage:
credentials = {"admin": "admin123", "user1": "password1"}
print(login("admin", "admin123", credentials))  # Output: True
print(login("user1", "wrongpassword", credentials))  # Output: False
    