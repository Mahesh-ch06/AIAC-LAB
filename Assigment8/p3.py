'''write a function primefactors and check functionallity by passing different numbers to it.'''
def primefactors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
print(primefactors(28))  # Output: [2, 2, 7]
print(primefactors(18))  # Output: [2, 3, 3]
print(primefactors(29))  # Output: [29]
print(primefactors(100)) # Output: [2, 2, 5, 5]
print(primefactors(1))   # Output: []
