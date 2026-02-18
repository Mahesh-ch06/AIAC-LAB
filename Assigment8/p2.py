def sqroot(a):
    if a < 0:
        return "Cannot compute square root of a negative number."
    elif a == 0:
        return 0
    else:
        return a ** 0.5
print(sqroot(16))  # Output: 4.0
print(sqroot(-4))  # Output: Cannot compute square root of a negative number
print(sqroot(0))   # Output: 0
print(sqroot(25))  # Output: 5.0