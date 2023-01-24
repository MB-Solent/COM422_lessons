class Car:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.current_speed = 0
        self.max_speed = max_speed
        self.fuel_level = 75

    def accelerate(self):
        self.current_speed = self.current_speed + 1 if self.current_speed + 1 < self.max_speed else self.max_speed

    def brake(self):
        self.current_speed = self.current_speed - 1 if self.current_speed - 1 > 0 else 0

    def refuel(self):
        self.fuel_level = self.fuel + 1 if self.fuel + 1 < 100 else 100

    def __str__(self):
        return f"Car details:\n\tBrand: {self.brand}\n\tSpeed: {self.current_speed}/{self.max_speed}\n\tFuel: {self.fuel_level}%"

