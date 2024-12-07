class Driver:
    def __init__(self, name):
        self.name = name
        self.car = None

    def buy_car(self, car):
        self.car = car
        print(f"{self.name} Купил {car.model}.")

    def drive(self):
        if self.car:
            if self.car.fuel > 0:
                print(f"{self.name} Решил поездить в его новеньком {self.car.model}.")
                self.car.fuel -= 10
            else:
                print(f"В {self.car.model} Кончилось топливо...")
        else:
            print(f"{self.name} Нету машины что бы поездить!")

class Car:
    def __init__(self, model, fuel):
        self.model = model
        self.fuel = fuel

    def refuel(self, amount):
        self.fuel += amount
        print(f"{self.model} Заправлено, топливо: {self.fuel}")

driver = Driver("V1")
car = Car("Gabriel", 50)

driver.buy_car(car)
driver.drive()
car.refuel(20)
driver.drive()
