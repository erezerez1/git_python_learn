class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

class ElectricCar(Car):
# Represent aspects of a car, specific to electric vehicles.

    def __init__(self, make, model, year):
# Initialize attributes of the parent class.
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
# Print a statement describing the battery size.
        print(f"This car has a {self.battery_size}-kWh battery.")


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
