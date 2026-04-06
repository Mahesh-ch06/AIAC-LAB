import time
time1 = time.time()
nums = [i for i in range(1,1000000)]
squares = []
for n in nums:
    squares.append(n**2)
time2 = time.time()
print("Time taken: ", time2-time1)
print(len(squares))
# refactor above code to reduce time complexity and memory usage
time3 = time.time()
squares = [n**2 for n in range(1, 1000000)]
time4 = time.time()
print("Time taken: ", time4-time3)
print(len(squares))
