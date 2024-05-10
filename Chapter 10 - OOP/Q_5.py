# Write a class Train which has methods to book a ticket, get status(no. of seats) and get fare information of trains running under Indian Railways.

class Train:
    def __init__(self, train_name, total_seats, fare_per_tickets):
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare_per_ticket = fare_per_tickets

    def book_ticket(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"{num_tickets} ticket(s) booked successfully for {self.train_name}.")
        else:
            print("Sorry, not enough seats available.")

    def get_status(self):
        print(f"Available seats for {self.train_name}: {self.available_seats}/{self.total_seats}")

    def get_fare_info(self):
        print(f"Fare per ticket for {self.train_name}: {self.fare_per_ticket} INR")

# Example usage:
if __name__ == "__main__":
    # Creating an instance of Train
    train1 = Train("VandeBharat Express", 1700, 1250)

    # Booking tickets
    train1.book_ticket(4)
    train1.get_status()

    # Getting fare information
    train1.get_fare_info()




    


