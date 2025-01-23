import pandas as pd
import random

# Sample train data
train_data = {
    'Train': ['Shatabdi Express', 'Chennai Express', 'Vandhe Bharath', 'Duronto Express'],
    'Sleeper Seats': [100, 150, 200, 120],
    'AC Seats': [50, 75, 60, 40],
    'Sleeper Price': [500, 700, 300, 600],
    'AC Price': [1200, 1500, 800, 1000]
}

# Create DataFrame
trains = pd.DataFrame(train_data)

# Function to check seat availability
def check_availability(train, class_type, num_seats):
    if train in trains['Train'].values:
        index = trains[trains['Train'] == train].index[0]
        if class_type == 'Sleeper':
            if trains.loc[index, 'Sleeper Seats'] >= num_seats:
                return True
        elif class_type == 'AC':
            if trains.loc[index, 'AC Seats'] >= num_seats:
                return True
        else:
            print("Invalid class type.")
            return False
    else:
        print("Train not found.")
        return False

# Function to book tickets
def book_tickets(train, class_type, num_seats):
    if check_availability(train, class_type, num_seats):
        index = trains[trains['Train'] == train].index[0]
        if class_type == 'Sleeper':
            trains.loc[index, 'Sleeper Seats'] -= num_seats
            price = trains.loc[index, 'Sleeper Price']
        elif class_type == 'AC':
            trains.loc[index, 'AC Seats'] -= num_seats
            price = trains.loc[index, 'AC Price']
        pnr_number = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))
        print("Tickets booked successfully!")
        print(f"PNR Number: {pnr_number}")
        print(f"Total fare: {price * num_seats}")
    else:
        print("Booking failed. Seats not available.")

# Example usage
book_tickets('Shatabdi Express', 'AC', 2)
book_tickets('Chennai Express', 'Sleeper', 5)

# Display updated train availability
print("\nUpdated Train Availability:\n", trains)
