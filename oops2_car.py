# Normal car and EV car classes with inheritance

class Car:
    def __init__(self, brand, model, year, cc):
        self.brand = brand
        self.model = model
        self.year = year
        self.cc = cc
    
    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, CC: {self.cc}")

class EvCar(Car):
    def __init__(self, brand, model, year, cc, battery):
        super().__init__(brand, model, year, cc)
        self.battery = battery
    
    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, CC: {self.cc}, Battery: {self.battery}")

class OffCar(Car):
    def __init__(self, brand, model, year, cc, terrain):
        super().__init__(brand, model, year, cc)
        self.terrain = terrain
    
    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, CC: {self.cc}, Terrain: {self.terrain}")

# Create instances
normal_car = Car("Tata", "Safari", 2023, 2500)
electric_car = EvCar("Tesla", "Model 3", 2023, 0, "100 kWh")
offroad_car = OffCar("Jeep", "Wrangler", 2023, 3000, "Mountain")

# Display information
normal_car.car_info()
electric_car.car_info()
offroad_car.car_info()




