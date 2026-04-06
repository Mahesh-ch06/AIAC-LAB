"""Check whether a username has access from a predefined user list."""

def check_access(username, user_list):
    return username in user_list


# Example usage:
if __name__ == "__main__":
    users = ["admin", "guest", "editor", "viewer"]
    name = input("Enter username: ")
    if check_access(name, users):
        print("Access Granted")
    else:
        print("Access Denied")


# Pytest for the function
def test_check_access():
    users = ["admin", "guest", "editor", "viewer"]
    assert check_access("admin", users) == True
    assert check_access("guest", users) == True
    assert check_access("editor", users) == True
    assert check_access("viewer", users) == True
    assert check_access("unknown", users) == False


# To run the tests, use the command: python -m pytest Task6.py