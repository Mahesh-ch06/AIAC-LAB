class CourierService:
    def __init__(self, courier_id, sender_name, weight_kg, distance_km):
        self.courier_id = courier_id
        self.sender_name = sender_name
        self.weight_kg = weight_kg
        self.distance_km = distance_km

    def display_details(self):
        print(f"Courier ID: {self.courier_id}")
        print(f"Sender Name: {self.sender_name}")
        print(f"Weight (kg): {self.weight_kg}")
        print(f"Distance (km): {self.distance_km}")

    def calculate_charges(self):
        # Calculate weight charges
        if self.weight_kg <= 5:
            weight_charge = self.weight_kg * 40
        elif self.weight_kg <= 15:
            weight_charge = (5 * 40) + ((self.weight_kg - 5) * 30)
        else:
            weight_charge = (5 * 40) + (10 * 30) + ((self.weight_kg - 15) * 20)

        # Calculate distance charges
        distance_charge = self.distance_km * 5

        # Total charges
        total_charge = weight_charge + distance_charge
        return total_charge
# Example usage
if __name__ == "__main__":
    # Create an instance of CourierService
    courier = CourierService(courier_id=101, sender_name="Alice", weight_kg=18, distance_km=50)
    courier1 = CourierService(courier_id=102, sender_name="Bob", weight_kg=3, distance_km=20)
    courier2 = CourierService(courier_id=103, sender_name="Charlie", weight_kg=10, distance_km=30)
    courier3 = CourierService(courier_id=104, sender_name="David", weight_kg=25, distance_km=100)
    
    # Display courier details
    courier.display_details()
    courier1.display_details()
    courier2.display_details()
    courier3.display_details()
    
    
    # Calculate and display total charges
    total_cost = courier.calculate_charges()
    print(f"Total Charges: {total_cost}")
# Analysis:
# Time Complexity: O(1) - The calculations and display operations are constant time operations.
# Space Complexity: O(1) - The space used does not grow with input size; it uses a fixed amount of space.
