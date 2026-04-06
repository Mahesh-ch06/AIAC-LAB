"""Calculate net salary after tax.

This module provides a small helper function to compute net salary
from a gross salary and a tax rate.
"""
def calculate_net_salary(salary, tax_rate):
    """
    Calculate the net salary after deducting tax.

    Args:
        salary (float): The gross salary.
        tax_rate (float): The tax rate as a decimal.

    Returns:
        float: The net salary.
    """
    tax = salary * tax_rate
    return salary - tax

# Example usage:
salary = 50000
net_salary = calculate_net_salary(salary, 0.2)
print(net_salary)
# To generate documentation using pydoc, you can run the following command in the terminal:
# python -m pydoc -w Task5
# This will create an HTML file named Task5.html with the documentation for the calculate_net_salary function.
