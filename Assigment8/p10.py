def EvenOddCheck(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
assert EvenOddCheck(4) == "Even"
assert EvenOddCheck(7) == "Odd"
assert EvenOddCheck(0) == "Even"
print("All assertions passed successfully.")