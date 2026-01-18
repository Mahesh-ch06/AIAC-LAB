#write a python program to check given number is armstrong number or not give me a code using one shot solution by providing multiple inputs
num = int(input("Enter a number to check if it's an Armstrong number: "))
sum_of_cubes = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10
if num == sum_of_cubes:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


