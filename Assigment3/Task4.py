# write a python code for prime,composite and neither prime nor composite number using functions Optimize the logic for efficiency.

def check_number_type(n):
    if n <= 1:
        return "neither prime nor composite"
    if n == 2:
        return "prime"
    if n % 2 == 0:
        return "composite"
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return "composite"
    return "prime"
num = int(input("Enter a number to check if it's prime, composite or neither: "))
result = check_number_type(num)
print(f"{num} is {result}.")



