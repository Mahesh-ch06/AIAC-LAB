'''Genrate a lists of automorphic numbers in a given range'''
import time as t
def is_automorphic(num):
    square = num * num
    num_str = str(num)
    square_str = str(square)
    return square_str.endswith(num_str)
def automorphic_numbers_in_range(start, end):
    automorphic_numbers = []
    for num in range(start, end + 1):
        if is_automorphic(num):
            automorphic_numbers.append(num)
    return automorphic_numbers
start_time = t.time()
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
automorphic_numbers = automorphic_numbers_in_range(start_range, end_range)
print(f"Automorphic numbers between {start_range} and {end_range}: {automorphic_numbers}")
end_time = t.time()
print(f"Time taken: {end_time - start_time} seconds\n")


'''Genrate a lists of automorphic numbers in a given range using while loop'''
print("Using while loop:")
def automorphic_numbers_in_range_while(start, end):
    automorphic_numbers = []
    num = start
    while num <= end:
        if is_automorphic(num):
            automorphic_numbers.append(num)
        num += 1
    return automorphic_numbers
start_time = t.time()
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
automorphic_numbers = automorphic_numbers_in_range_while(start_range, end_range)
print(f"Automorphic numbers between {start_range} and {end_range}: {automorphic_numbers}")
end_time = t.time()
print(f"Time taken: {end_time - start_time} seconds")
