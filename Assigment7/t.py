'''def add_item(item, items=[]):
    items.append(item)
    return items
print(add_item('apple'))  # Output: ['apple']
print(add_item('banana'))  # Output: ['apple', 'banana']
print(add_item('orange'))  # Output: ['apple', 'banana', 'orange']'''

'''a = 30
b = 30
c = 20
print(id(a), id(b), id(c))  # Output: Memory address of a, b, and c
b = 56
print(id(a), id(b), id(c))  # Output: Memory address of a, b, and c
print(type(a), type(b), type(c))  # Output: <class 'int'> <class 'int'> <class 'int'>'''

'''a = [34, [56, 78], 90]
b = a.copy().copy()
b[1][0] = 100
print(a)  # Output: [34, [100, 78], 90]
print(b)  # Output: [34, [100, 78], 90]'''

'''Task: Analyze given code where tuple unpacking fails. Use AI to
fix it.
# Bug: Wrong unpacking
a, b = (1, 2, 3)

Expected Output: Correct unpacking or using _ for extra values.

a, b, *rest = (1, 2, 3)
print(a)     # Output: 1
print(b)     # Output: 2
print(rest)  # Output: [3]'''

def func():
    x = 5
    y = 10
    return x, y
a, b = func()
print(a)  # Output: 5
print(b)  # Output: 10

def calculate_area():
    return length * width
length = 5
width = 10
area = calculate_area()
print(area)  # Output: 50

def add_values():
    return 5 + "10"
result = add_values()
print(result)  # This will raise a TypeError because you cannot add an integer and a

def compute(a, value = 50):
    return a + value + 10
result = compute(5)
print(result)  # Output: 65
