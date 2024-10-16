#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Class to represent a Flight
class Flight {
public:
    string flightNumber;
    string destination;
    int seatsAvailable;

    Flight(string flightNum, string dest, int seats)
        : flightNumber(flightNum), destination(dest), seatsAvailable(seats) {}
};

// Class to represent a Passenger
class Passenger {
public:
    string name;
    string flightNumber;

    Passenger(string passengerName, string flightNum)
        : name(passengerName), flightNumber(flightNum) {}
};

// Class to manage the Aviation System
class AviationManagementSystem {
private:
    vector<Flight> flights;
    vector<Passenger> bookings;

public:
    // Function to add a new flight
    void addFlight(string flightNumber, string destination, int seats) {
        flights.emplace_back(flightNumber, destination, seats);
        cout << "Flight added: " << flightNumber << " to " << destination << " with " << seats << " seats available." << endl;
    }

    // Function to view all flights
    void viewFlights() {
        cout << "\nAvailable Flights:" << endl;
        for (const auto& flight : flights) {
            cout << "Flight Number: " << flight.flightNumber
                 << ", Destination: " << flight.destination
                 << ", Seats Available: " << flight.seatsAvailable << endl;
        }
    }

    // Function to book a flight
    void bookFlight(string passengerName, string flightNumber) {
        for (auto& flight : flights) {
            if (flight.flightNumber == flightNumber) {
                if (flight.seatsAvailable > 0) {
                    bookings.emplace_back(passengerName, flightNumber);
                    flight.seatsAvailable--;
                    cout << "Booking confirmed for " << passengerName << " on flight " << flightNumber << "." << endl;
                    return;
                } else {
                    cout << "No seats available on flight " << flightNumber << "." << endl;
                    return;
                }
            }
        }
        cout << "Flight " << flightNumber << " not found." << endl;
    }

    // Function to view all bookings
    void viewBookings() {
        cout << "\nCurrent Bookings:" << endl;
        for (const auto& booking : bookings) {
            cout << "Passenger: " << booking.name << ", Flight Number: " << booking.flightNumber << endl;
        }
    }
};

// Main function
int main() {
    AviationManagementSystem system;
    int choice;

    do {
        cout << "\nAviation Management System Menu:" << endl;
        cout << "1. Add Flight" << endl;
        cout << "2. View Flights" << endl;
        cout << "3. Book Flight" << endl;
        cout << "4. View Bookings" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                string flightNumber, destination;
                int seats;
                cout << "Enter Flight Number: ";
                cin >> flightNumber;
                cout << "Enter Destination: ";
                cin >> destination;
                cout << "Enter Number of Seats: ";
                cin >> seats;
                system.addFlight(flightNumber, destination, seats);
                break;
            }
            case 2:
                system.viewFlights();
                break;
            case 3: {
                string passengerName, flightNumber;
                cout << "Enter Passenger Name: ";
                cin >> passengerName;
                cout << "Enter Flight Number: ";
                cin >> flightNumber;
                system.bookFlight(passengerName, flightNumber);
                break;
            }
            case 4:
                system.viewBookings();
                break;
            case 5:
                cout << "Exiting the system." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 5);

    return 0;
}
