'''# Legacy script with inline repeated logic
price = 250
tax = price * 0.18
total = price + tax
print("Total Price:", total)
price = 500
tax = price * 0.18
total = price + tax
print("Total Price:", total)'''

# Refactored code using a function to eliminate repetition
def calculate_total_price(price):
    tax = price * 0.18
    total = price + tax
    return total
# Example usage:
prices = [250, 500]
for price in prices:
    total_price = calculate_total_price(price)
    print(f"Total Price: {total_price}")
    