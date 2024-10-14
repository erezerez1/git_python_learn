 class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
    """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 40
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery."
