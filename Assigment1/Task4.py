# Write a Python code that takes input from user and calculates the factorial of a number using a for loop... Comparative Analysis – Procedural vs Modular AI Code (With vs Without Functions) 

import time

# ========================================
# PROCEDURAL VERSION (Without Functions)
# ========================================
print("=== PROCEDURAL VERSION ===")
start_time_procedural = time.perf_counter()

num = int(input("Enter a number to calculate its factorial: "))

if num < 0:
    result = "Factorial is not defined for negative numbers."
elif num == 0 or num == 1:
    result = 1
else:
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    result = factorial

print(f"The factorial of {num} is {result}")
end_time_procedural = time.perf_counter()
execution_time_procedural = (end_time_procedural - start_time_procedural) * 1000  # Convert to milliseconds
print(f"⏱ Execution Time (Procedural): {execution_time_procedural:.6f} ms")


print("\n" + "="*50 + "\n")


# ========================================
# MODULAR VERSION (With Functions)
# ========================================
print("=== MODULAR VERSION ===")
start_time_modular = time.perf_counter()

def calculate_factorial(num):
    """
    Calculate the factorial of a given number.
    
    Args:
        num (int): The number to calculate factorial for
        
    Returns:
        int or str: The factorial result or error message
    """
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial

def get_user_input():
    """Get and validate user input."""
    return int(input("Enter a number to calculate its factorial: "))

def display_result(num, result):
    """Display the factorial result."""
    print(f"The factorial of {num} is {result}")

# Main execution
num = get_user_input()
result = calculate_factorial(num)
display_result(num, result)

end_time_modular = time.perf_counter()
execution_time_modular = (end_time_modular - start_time_modular) * 1000  # Convert to milliseconds
print(f"⏱ Execution Time (Modular): {execution_time_modular:.6f} ms")


# ========================================
# PERFORMANCE COMPARISON
# ========================================
print("\n" + "="*50)
print("PERFORMANCE ANALYSIS")
print("="*50)
print(f"Procedural Version: {execution_time_procedural:.6f} ms")
print(f"Modular Version:    {execution_time_modular:.6f} ms")

time_difference = abs(execution_time_modular - execution_time_procedural)
if execution_time_procedural < execution_time_modular:
    print(f"\nProcedural was faster by {time_difference:.6f} ms")
elif execution_time_modular < execution_time_procedural:
    print(f"\nModular was faster by {time_difference:.6f} ms")
else:
    print(f"\nBoth versions took the same time")

print("\nNote: For simple operations, timing differences are negligible.")
print("   The real benefits of modular code appear in maintainability and scalability.")
print("="*50 + "\n")



