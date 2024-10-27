from tabulate import tabulate  # You need to install tabulate using: pip install tabulate

class Automobile:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False
        self.speed = 0

    def start(self):
        if not self.is_running:
            self.is_running = True
        return f"{self.make} {self.model} has started." if not self.is_running else f"{self.make} {self.model} is already running."

    def accelerate(self, increment):
        if self.is_running:
            self.speed += increment
        return f"{self.make} {self.model} has accelerated. Current speed: {self.speed} km/h." if self.is_running else f"Cannot accelerate. {self.make} {self.model} is not running."

    def brake(self, decrement):
        if self.is_running and self.speed > 0:
            self.speed = max(0, self.speed - decrement)
        return f"{self.make} {self.model} has braked. Current speed: {self.speed} km/h." if self.is_running else f"Cannot brake. {self.make} {self.model} is not moving or not running."

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
        return f"{self.make} {self.model} has stopped and turned off." if self.is_running else f"{self.make} {self.model} is already turned off."


# Car class inherits from Automobile
class Car(Automobile):
    def accelerate(self, increment):
        super().accelerate(increment * 1.2)

    def brake(self, decrement):
        super().brake(decrement * 1.1)


# Motorbike class inherits from Automobile
class Motorbike(Automobile):
    def accelerate(self, increment):
        super().accelerate(increment * 1.5)

    def brake(self, decrement):
        super().brake(decrement * 0.8)


# Truck class inherits from Automobile
class Truck(Automobile):
    def accelerate(self, increment):
        super().accelerate(increment * 0.7)

    def brake(self, decrement):
        super().brake(decrement * 1.5)

def automobile_children_classes_demo():
    # Create instances of Car, Motorbike, and Truck
    car = Car("Audi", "A3")
    motorbike = Motorbike("Yamaha", "YBR")
    truck = Truck("Dodge", "Challenger")

    # List to store test results
    results = []

    # Perform operations and store results in the results list
    vehicles = [car, motorbike, truck]
    for vehicle in vehicles:
        # Start the vehicles
        vehicle.start()
        results.append([vehicle.make, vehicle.model, "Start", vehicle.speed, vehicle.is_running])

        # Accelerate the vehicles
        for _ in range(3):
            vehicle.accelerate(10)
            results.append([vehicle.make, vehicle.model, "Accelerate", vehicle.speed, vehicle.is_running])

        # Brake the vehicles
        for _ in range(3):
            vehicle.brake(5)
            results.append([vehicle.make, vehicle.model, "Brake", vehicle.speed, vehicle.is_running])

        # Stop the vehicles
        vehicle.stop()
        results.append([vehicle.make, vehicle.model, "Stop", vehicle.speed, vehicle.is_running])

    # Display the results in a table
    headers = ["Make", "Model", "Action", "Speed (km/h)", "Is Running?"]
    print(tabulate(results, headers, tablefmt="fancy_grid"))
    
if __name__ == "__main__":
    automobile_children_classes_demo()
