class ParkingSlotNode:
    """
    A node representing an available parking slot in the linked list.
    """
    def __init__(self, slot_id: str):
        self.slot_id = slot_id
        self.next = None  # Pointer to the next available slot

class ParkingLotFreeList:
    """
    Manages available parking slots using a Singly Linked List.
    This acts as a 'free list' where we only track empty spaces.
    """
    def __init__(self):
        self.head = None
        self.available_count = 0

    def add_empty_slot(self, slot_id: str):
        """
        Adds a freed parking slot back to the available pool (head of the list).
        Time Complexity: O(1)
        """
        new_slot = ParkingSlotNode(slot_id)
        # Point the new slot to the current head, then make it the new head
        new_slot.next = self.head
        self.head = new_slot
        self.available_count += 1
        print(f"[UPDATE] Slot {slot_id} is now empty and added to available pool.")

    def assign_parking_slot(self) -> str:
        """
        Assigns the next available parking slot to a vehicle by removing it from the list.
        Time Complexity: O(1)
        """
        if self.head is None:
            print("[ALERT] The parking lot is completely full!")
            return None
        
        # Take the slot at the head of the list
        assigned_slot = self.head.slot_id
        # Move the head pointer to the next available slot
        self.head = self.head.next
        self.available_count -= 1
        
        print(f"[SUCCESS] Vehicle assigned to slot: {assigned_slot}")
        return assigned_slot

    def display_available_count(self):
        """Prints the total number of available slots."""
        print(f"Current available slots: {self.available_count}")


# ==========================================
# Demonstration of the Linked List Parking
# ==========================================
if __name__ == "__main__":
    # Initialize the parking lot manager
    city_parking = ParkingLotFreeList()
    
    # Let's say the system boots up and registers 3 empty slots
    print("--- Initializing Parking Lot ---")
    city_parking.add_empty_slot("A-01")
    city_parking.add_empty_slot("A-02")
    city_parking.add_empty_slot("B-14")
    
    city_parking.display_available_count()
    
    print("\n--- Vehicles Arriving ---")
    # Cars arrive and are instantly assigned the next available slot from the head
    car1_slot = city_parking.assign_parking_slot()
    car2_slot = city_parking.assign_parking_slot()
    
    city_parking.display_available_count()
    
    print("\n--- Vehicle Leaving ---")
    # The first car leaves, so we push its slot back onto the free list
    city_parking.add_empty_slot(car1_slot)
    
    city_parking.display_available_count()