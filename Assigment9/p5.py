# write a function for add two numbers and test it using pytest with 5 examples
def add(a, b):
    return a + b
def test_add():
    assert add(2, 3) == 5
    assert add(10, 20) == 30
    assert add(-2, -3) == -5
    assert add(-10, -20) == -30
    assert add(-2, 3) == 1
    assert add(10, -20) == -10
