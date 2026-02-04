class Product:
    def __init__(self, product_id, product_name, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = category

    def display_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.category}")

    def calculate_discount(self):
        if self.category == "Electronics":
            discount_rate = 0.10
        elif self.category == "Clothing":
            discount_rate = 0.15
        elif self.category == "Grocery":
            discount_rate = 0.05
        else:
            discount_rate = 0.0  # No discount for other categories
        final_price = self.price * (1 - discount_rate)
        return final_price
# Creating an instance of Product
product = Product(product_id=101, product_name="Smartphone", price=20000,
                        category="Electronics")
# Displaying product details
product.display_details()
# Calculating and printing final price after discount
final_price = product.calculate_discount()
print(f"Final Price after discount: ₹{final_price}")
