def PalindromeCheck(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse
assert PalindromeCheck("A man a plan a canal Panama") == True
assert PalindromeCheck("Hello") == False
assert PalindromeCheck("Madam") == True
assert PalindromeCheck("Was it a car or a cat I saw") == True
assert PalindromeCheck("Python") == False
print("All assertions passed successfully.")