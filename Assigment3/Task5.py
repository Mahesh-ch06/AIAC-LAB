# write a python code for perfect number using one shot solution
num = int(input("Enter a number to check if it's a perfect number: "))
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i
if sum_of_divisors == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

