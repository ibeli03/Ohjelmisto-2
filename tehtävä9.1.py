class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
my_car = Car("ABC-123", 142)
print(f"Registration number: {my_car.registration_number}")
print(f"Maximum speed: {my_car.maximum_speed}")
print(f"Current speed: {my_car.current_speed}")
print(f"Travelled distance: {my_car.travelled_distance}")