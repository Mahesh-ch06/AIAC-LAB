# Write a Python code that implements the Bubble Sort algorithm and compares its execution time with built in sort method using a list of 5000 random integers.

import random
import time
def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def main() -> None:
    # Generate a list of 5000 random integers
    random_list = [random.randint(1, 10000) for _ in range(5000)]
    
    # Copy the list for built-in sort comparison
    list_for_builtin_sort = random_list.copy()
    
    # Measure execution time for Bubble Sort
    start_time = time.time()
    sorted_list_bubble = bubble_sort(random_list)
    bubble_sort_time = time.time() - start_time
    print(f"Bubble Sort took {bubble_sort_time:.6f} seconds.")
    
    # Measure execution time for built-in sort
    start_time = time.time()
    sorted_list_builtin = sorted(list_for_builtin_sort)
    builtin_sort_time = time.time() - start_time
    print(f"Built-in Sort took {builtin_sort_time:.6f} seconds.")
    
    # Verify both sorting methods yield the same result
    assert sorted_list_bubble == sorted_list_builtin, "Sorting results do not match!"
if __name__ == "__main__":
    main()
