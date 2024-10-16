class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True


class Guest:
    def __init__(self, name, room_number):
        self.name = name
        self.room_number = room_number


class HotelManagementSystem:
    def __init__(self):
        self.rooms = []
        self.bookings = []

    def add_room(self, room_number, room_type, price):
        room = Room(room_number, room_type, price)
        self.rooms.append(room)
        print(f"Room {room_number} of type {room_type} added at price {price}.")

    def view_rooms(self):
        print("\nAvailable Rooms:")
        for room in self.rooms:
            availability = "Available" if room.is_available else "Not Available"
            print(f"Room Number: {room.room_number}, Type: {room.room_type}, Price: {room.price}, Status: {availability}")

    def check_in(self, guest_name, room_number):
        room = self.find_room(room_number)
        if room:
            if room.is_available:
                guest = Guest(guest_name, room_number)
                self.bookings.append(guest)
                room.is_available = False
                print(f"Check-in successful for {guest_name} in room {room_number}.")
            else:
                print(f"Room {room_number} is not available.")
        else:
            print(f"Room {room_number} not found.")

    def check_out(self, room_number):
        room = self.find_room(room_number)
        if room:
            if not room.is_available:
                room.is_available = True
                self.bookings = [booking for booking in self.bookings if booking.room_number != room_number]
                print(f"Check-out successful for room {room_number}.")
            else:
                print(f"Room {room_number} is already available.")
        else:
            print(f"Room {room_number} not found.")

    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def view_bookings(self):
        print("\nCurrent Bookings:")
        for booking in self.bookings:
            print(f"Guest: {booking.name}, Room Number: {booking.room_number}")


def display_menu():
    print("\nHotel Management System Menu:")
    print("1. Add Room")
    print("2. View Rooms")
    print("3. Check In")
    print("4. Check Out")
    print("5. View Bookings")
    print("6. Exit")


def main():
    system = HotelManagementSystem()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            room_number = input("Enter Room Number: ")
            room_type = input("Enter Room Type: ")
            price = float(input("Enter Room Price: "))
            system.add_room(room_number, room_type, price)

        elif choice == '2':
            system.view_rooms()

        elif choice == '3':
            guest_name = input("Enter Guest Name: ")
            room_number = input("Enter Room Number: ")
            system.check_in(guest_name, room_number)

        elif choice == '4':
            room_number = input("Enter Room Number: ")
            system.check_out(room_number)

        elif choice == '5':
            system.view_bookings()

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
