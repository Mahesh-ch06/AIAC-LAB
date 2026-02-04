class TaxiRide:
    def __init__(self, ride_id, driver_name, distance_km, waiting_time_min):
        self.ride_id = ride_id
        self.driver_name = driver_name
        self.distance_km = distance_km
        self.waiting_time_min = waiting_time_min

    def display_details(self):
        print(f"Ride ID: {self.ride_id}")
        print(f"Driver Name: {self.driver_name}")
        print(f"Distance (km): {self.distance_km}")
        print(f"Waiting Time (min): {self.waiting_time_min}")

    def calculate_fare(self):
        fare = 0
        if self.distance_km <= 10:
            fare += self.distance_km * 15
        elif 10 < self.distance_km <= 30:
            fare += 10 * 15 + (self.distance_km - 10) * 12
        else:
            fare += 10 * 15 + 20 * 12 + (self.distance_km - 30) * 10
        fare += self.waiting_time_min * 2
        return fare
# Creating an instance of TaxiRide
ride = TaxiRide(ride_id=1, driver_name="Rajesh", distance_km
                     =35, waiting_time_min=15)
# Displaying ride details
ride.display_details()
# Calculating and printing total fare
total_fare = ride.calculate_fare()
print(f"Total Fare: ₹{total_fare}")
