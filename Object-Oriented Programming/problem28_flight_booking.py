# Exercise 28: Flight booking with passenger capacity

# Logic
# Passenger stores the passenger's name.
# Flight stores:
# Flight number
# Seat capacity
# List of booked passengers
# book_passenger() checks if seats are available.
# If seats are available, the passenger is added.
# Otherwise, it prints that the flight is fully booked.

class Passenger:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self, flight_no, capacity):
        self.flight_no = flight_no
        self.capacity = capacity
        self.passengers = []

    def book_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger.name} booked on Flight {self.flight_no}.")
        else:
            print(f"Sorry, Flight {self.flight_no} is fully booked.")


flight = Flight("AI202", 2)

p1 = Passenger("Alice")
p2 = Passenger("Bob")
p3 = Passenger("Charlie")

flight.book_passenger(p1)
flight.book_passenger(p2)
flight.book_passenger(p3)