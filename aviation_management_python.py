class Flight:
    def __init__(self, flight_number, destination, seats_available):
        self.flight_number = flight_number
        self.destination = destination
        self.seats_available = seats_available


class Passenger:
    def __init__(self, name, flight_number):
        self.name = name
        self.flight_number = flight_number


class AviationManagementSystem:
    def __init__(self):
        self.flights = []
        self.bookings = []

    def add_flight(self, flight_number, destination, seats):
        flight = Flight(flight_number, destination, seats)
        self.flights.append(flight)
        print(f"Flight added: {flight_number} to {destination} with {seats} seats available.")

    def view_flights(self):
        print("\nAvailable Flights:")
        for flight in self.flights:
            print(f"Flight Number: {flight.flight_number}, Destination: {flight.destination}, Seats Available: {flight.seats_available}")

    def book_flight(self, passenger_name, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                if flight.seats_available > 0:
                    booking = Passenger(passenger_name, flight_number)
                    self.bookings.append(booking)
                    flight.seats_available -= 1
                    print(f"Booking confirmed for {passenger_name} on flight {flight_number}.")
                    return
                else:
                    print(f"No seats available on flight {flight_number}.")
                    return
        print(f"Flight {flight_number} not found.")

    def view_bookings(self):
        print("\nCurrent Bookings:")
        for booking in self.bookings:
            print(f"Passenger: {booking.name}, Flight Number: {booking.flight_number}")


def main():
    system = AviationManagementSystem()
    while True:
        print("\nAviation Management System Menu:")
        print("1. Add Flight")
        print("2. View Flights")
        print("3. Book Flight")
        print("4. View Bookings")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            flight_number = input("Enter Flight Number: ")
            destination = input("Enter Destination: ")
            seats = int(input("Enter Number of Seats: "))
            system.add_flight(flight_number, destination, seats)

        elif choice == '2':
            system.view_flights()

        elif choice == '3':
            passenger_name = input("Enter Passenger Name: ")
            flight_number = input("Enter Flight Number: ")
            system.book_flight(passenger_name, flight_number)

        elif choice == '4':
            system.view_bookings()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
