class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")


vasya = Human("Vasya")
katya = Human("Katya")

car = Auto("Audi")

car.add_passenger(katya)
car.add_passenger(katya)
car.add_passenger(katya)
car.add_passenger(katya)
car.add_passenger(vasya)
car.add_passenger(vasya)
car.add_passenger(vasya)
car.print_passengers_names()


