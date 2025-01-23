
# Railway Ticket Booking System

A basic railway ticket booking system modeled on the Indian Railways system. This project uses Python and the Pandas library to manage train data, check seat availability, book tickets, calculate fares, and generate PNR numbers.

## Features
- Store train information (train names, available seats, and ticket prices).
- Check seat availability for Sleeper and AC classes.
- Book tickets and calculate fares.
- Generate Passenger Name Record (PNR) numbers dynamically.
- Display updated train availability after bookings.

---

## Installation and Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/Dhanush29092004/RailwayBookingSystem.git
   cd RailwayBookingSystem
   ```
2. Install required dependencies:
   - Python 3.x
   - Pandas library:
     ```bash
     pip install pandas
     ```

3. Run the Python script:
   ```bash
   python railway_booking.py
   ```

---

## Usage
### Checking Seat Availability
You can check whether seats are available in a specific train for a particular class:
```python
check_availability(train_name, class_type, num_seats)
```

### Booking Tickets
You can book tickets using the `book_tickets` function:
```python
book_tickets(train_name, class_type, num_seats)
```

### Example
```python
book_tickets('Shatabdi Express', 'AC', 2)
book_tickets('Rajdhani Express', 'Sleeper', 5)
```

---

## Output
After running the booking process, the program will display:
- PNR Number
- Total Fare
- Updated Train Availability

Example Output:
```text
Tickets booked successfully!
PNR Number: IJ7RRHSPHWE
Total Fare: 2400

Tickets booked successfully!
PNR Number: OPEOZLSIFII
Total Fare: 3500

Updated Train Availability:
         Train              Sleeper Seats  AC Seats  Sleeper Price  AC Price
0  Shatabdi Express           100             48           500        1200
1  Rajdhani Express           145             75           700        1500
2       Garib Rath            200             60           300         800
3  Duronto Express            120             40           600        1000
```

---

## File Structure
- `railway_booking.py`: Main script for the railway booking system.
- `README.md`: Documentation for the project.

---

## Technologies Used
- **Python**: Programming language.
- **Pandas**: Data manipulation library.

---

## Future Improvements
- Add dynamic pricing based on seat availability.
- Include additional classes like 1AC, 2AC, and General.
- Create a graphical user interface (GUI).
- Integrate with an actual database (e.g., SQLite, MySQL).

---

## Author
[Dhanush29092004](https://github.com/Dhanush29092004)

---

## License
This project is licensed under the MIT License.
