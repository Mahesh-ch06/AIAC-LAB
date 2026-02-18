def is_vaild_username(username):
    if len(username) < 3 or len(username) > 16:
        return False
    if not username[0].isalpha():
        return False
    for char in username:
        if not (char.isalnum() or char == '_'):
            return False
    return True
# Test cases
assert is_vaild_username("user_123") == True
assert is_vaild_username("1user") == False
assert is_vaild_username("us") == False
assert is_vaild_username("this_is_a_very_long_username") == False
assert is_vaild_username("valid_user") == True
assert is_vaild_username("invalid-user") == False
assert is_vaild_username("user!name") == False
assert is_vaild_username("user name") == False
print("All assertions passed successfully.")