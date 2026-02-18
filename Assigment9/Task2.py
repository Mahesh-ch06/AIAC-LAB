def classify_value(x):
    if isinstance(x, int):
        if x == 0:
            return "Zero"
        elif x % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Invalid Input"
# Test cases
assert classify_value(0) == "Zero"
assert classify_value(4) == "Even"
assert classify_value(7) == "Odd"
assert classify_value(-2) == "Even"
assert classify_value(-3) == "Odd"
assert classify_value(3.5) == "Invalid Input"
assert classify_value("string") == "Invalid Input"
print("All assertions passed successfully.")
