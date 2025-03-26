import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            car.accelerate()
            car.drive()
    def print_status(self):
        print(f"\nStatus of {self.name} Race: ")
        print(f"{'Registration':<15}{'Max speed':<12}{'Distance traveled':<20}")
        print("-" * 50)

        for car in self.cars:
            print(f"{car.registration_number:<15}{car.max_speed:<12}{car.distance_travelled:<20}")
    def race_finished(self):
        for car in self.cars:
            if car.distance_travelled >= self.distance:
                return False
            return False


cars = []

for i in range(1, 11):
    max_speed = random.randint(100, 200)
    registration_number = f"ABC-{i}"
    cars.append(Car(registration_number, max_speed))
race = Race("Grand demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()

race.print_status()
print(f"\nRace finished after {hours} hours!")




