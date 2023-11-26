import datetime as dt


# TODO 1 - Create Bike Rental Class and initialize stock attribute
class BikeRental:
    def __init__(self, stock=0):
        """Initializer for Bike rental class"""
        self.stock = stock

    # 2 - Create a method to display stock
    def display_stock(self):
        """Display bikes that currently available in the system"""
        print(f"We have currently {self.stock} bikes available in the system")
        return self.stock

    # 3 - Create a method to rent bike on hourly bases
    def rent_bike_on_hourly_basis(self, n):
        """Rents a bike on hourly basis"""
        if n <= 0:
            print("The number of bikes must be positive number!")
            return None
        elif n > self.stock:
            print(f"Sorry! We have only {self.stock} bikes available to rent!")
            return None
        else:
            now = dt.datetime.now()
            print(f"You have rented {n} bike(s) on hourly basis today at {now.hour}:{now.minute}:{now.second}")
            print("Your will be charged $5 for each bike per hour")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    # 4 - Create a method to rent bike on daily bases
    def rent_bike_on_daily_basis(self, n):
        """Rents a bike on daily basis"""
        if n <= 0:
            print("The number of bikes must be positive number!")
        elif n > self.stock:
            print(f"Sorry! we have currently {self.stock} bikes available to rent.")
        else:
            now = dt.datetime.today()
            print(f"You have rented {n} bike(s) on daily basis today on {now}")
            print("Your will be charged $20 for each bike daily")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    # 5 - Create a method to rent bike on weekly bases
    def rent_bike_on_weekly_basis(self, n):
        """Rents a bike on weekly basis"""
        if n <= 0:
            print("The number of bikes must be positive number!")
        elif n > self.stock:
            print(f"Sorry! we have currently {self.stock} bikes available to rent.")
        else:
            now = dt.datetime.today()
            print(f"You have rented {n} bike(s) on weekly basis today on {now}")
            print("Your will be charged $60 for each bike weekly")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    # 6 - Create a method  to return bike from the system
    def return_bike(self, request):
        """Accept a rented bike from a customer, increase number of available bikes and return a bill"""
        rental_time, rental_basis, num_of_bikes = request
        bill = 0
        if rental_time and rental_basis and num_of_bikes:
            self.stock += num_of_bikes
            now = dt.datetime.now()
            rental_period = now - rental_time
            # hourly bill calculation
            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * num_of_bikes
            # daily bill calculation
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * num_of_bikes
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * num_of_bikes
            if 3 <= num_of_bikes <= 6:
                print("You are eligible for family rental promotion which 30%.")
                bill = bill * 0.7
            print("Thanks for returning your bike. Hope you enjoyed the service!")
            print(f"The total bill is: ${bill}")
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None


# 7 - Create Customer Class and initialize attributes
class Customer:
    def __init__(self):
        """Initializer for Customer class"""
        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    # 8 - Create a method to request bike from the system
    def request_bike(self):
        """Takes a request from the customer for the number of bikes"""
        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("Invalid input: The number of bikes has to be positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input: The number of bikes has to be positive integer!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    # 9 - Create a method to return bike to the system
    def return_bike(self):
        """Allows customers to return their bikes to the rental shop"""
        if self.rental_basis and self.rental_time and self.bikes:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return 0, 0, 0

