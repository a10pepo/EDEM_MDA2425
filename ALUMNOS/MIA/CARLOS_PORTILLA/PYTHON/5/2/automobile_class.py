import time

class Car:
    make: str
    model: str
    speed: float = 0
    color: str

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False
        self.speed = 0

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model} has started.")
        else:
            print(f"{self.make} {self.model} is already running.")

    def accelerate(self, increment):
        if self.is_running:
            self.speed += increment
            print(f"{self.make} {self.model} has accelerated. Current speed: {self.speed} km/h.")
        else:
            print(f"Cannot accelerate. {self.make} {self.model} is not running.")

    def brake(self, decrement):
        if self.is_running and self.speed > 0:
            self.speed = max(0, self.speed - decrement)
            print(f"{self.make} {self.model} has braked. Current speed: {self.speed} km/h.")
        else:
            print(f"Cannot brake. {self.make} {self.model} is not moving or not running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print(f"{self.make} {self.model} has stopped and turned off.")
        else:
            print(f"{self.make} {self.model} is already turned off.")


def automobile_class_demo():
    car = Car("Toyota", "Camry")
    print(f'''
-----------------------
''')
    print(car.make, car.model)
    time.sleep(0.5)
    car.start()
    time.sleep(0.5)
    for _ in range(3):
        car.accelerate(37)
        time.sleep(0.5)
    for _ in range(3):
        car.brake(35)
        time.sleep(0.5)
    car.brake(100)
    time.sleep(0.5)
    car.stop()
    time.sleep(0.5)
    print(f'''
-----------------------
''')

if __name__ == "__main__":
    automobile_class_demo()
