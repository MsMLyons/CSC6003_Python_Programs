class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"The {self.make} {self.model} has started")

    def stop(self):
        print(f"The {self.make} {self.model} has stopped")

my_car = Car("Toyota", "4Runner")
my_car.start()
my_car.stop()