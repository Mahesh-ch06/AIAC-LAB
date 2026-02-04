class ElectricityBill:
    def __init__(self, customer_id, name, units_consumed):
        self.customer_id = customer_id
        self.name = name
        self.units_consumed = units_consumed

    def display_details(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Units Consumed: {self.units_consumed}")

    def calculate_bill(self):
        if self.units_consumed <= 100:
            rate_per_unit = 5
        elif 101 <= self.units_consumed <= 300:
            rate_per_unit = 7
        else:
            rate_per_unit = 10
        total_bill = self.units_consumed * rate_per_unit
        return total_bill
# Creating an instance of ElectricityBill
bill = ElectricityBill(customer_id=1, name="Alice", units_consumed=250)
# Displaying customer details
bill.display_details()
# Calculating and printing total bill amount
total_amount = bill.calculate_bill()
print(f"Total Bill Amount: ₹{total_amount}")
