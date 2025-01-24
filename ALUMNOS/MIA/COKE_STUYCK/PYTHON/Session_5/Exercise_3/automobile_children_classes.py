from tabulate import tabulate  # You need to install tabulate using: pip install tabulate
import time

class Automobile:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False
        self.speed = 0

    def start(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.make} {self.model} has started."
        else:
            return f"{self.make} {self.model} is already running."

    def accelerate(self, increment):
        if self.is_running:
            self.speed += increment
            return f"{self.make} {self.model} has accelerated. Current speed: {self.speed} km/h."
        return f"Cannot accelerate. {self.make} {self.model} is not running."

    def brake(self, decrement):
        if self.is_running and self.speed > 0:
            self.speed = max(0, self.speed - decrement)
            return f"{self.make} {self.model} has braked. Current speed: {self.speed} km/h."
        return f"Cannot brake. {self.make} {self.model} is not moving or not running."

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
            return f"{self.make} {self.model} has stopped and turned off."
        return f"{self.make} {self.model} is already turned off."


# Car class inherits from Automobile
class Car(Automobile):
    def accelerate(self, increment):
        return super().accelerate(increment * 1.2)  # Return the result

    def brake(self, decrement):
        return super().brake(decrement * 1.1)  # Return the result


# Motorbike class inherits from Automobile
class Motorbike(Automobile):
    def accelerate(self, increment):
        return super().accelerate(increment * 1.5)  # Return the result

    def brake(self, decrement):
        return super().brake(decrement * 0.8)  # Return the result


# Truck class inherits from Automobile
class Truck(Automobile):
    def accelerate(self, increment):
        return super().accelerate(increment * 0.7)  # Return the result

    def brake(self, decrement):
        return super().brake(decrement * 1.5)  # Return the result


def automobile_children_classes_demo():
    # Create instances of Car, Motorbike, and Truck
    car = Car("Audi", "A3")
    motorbike = Motorbike("Yamaha", "YBR")
    truck = Truck("Dodge", "Challenger")
    
    print('''
-----------------------
''')

    # Perform operations and display results
    vehicles = [car, motorbike, truck]
    for vehicle in vehicles:
        # Start the vehicles
        print(vehicle.start())  # This will now correctly show if it started or is already running
        time.sleep(0.5)

        # Accelerate the vehicles
        for _ in range(3):
            print(vehicle.accelerate(30))  # This will now show the correct output
            time.sleep(0.5)
            
        # Brake the vehicles
        for _ in range(5):
            print(vehicle.brake(40))  # This will now show the correct output
            time.sleep(0.5)

        # Stop the vehicles
        print(vehicle.stop())
        time.sleep(0.5)
        print('''
----------------------- 
''')
    
if __name__ == "__main__":
    automobile_children_classes_demo()
