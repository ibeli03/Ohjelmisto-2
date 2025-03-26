class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):

        new_speed = self.current_speed + speed_change

        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Max Speed: {self.max_speed} km/h, Current Speed: {self.current_speed} km/h, Travelled Distance: {self.travelled_distance} km"


my_car = Car("ABC-123", 142)

my_car.accelerate(30)

my_car.accelerate(70)

my_car.accelerate(50)

print(f"Current speed after acceleration: {my_car.current_speed} km/h")

my_car.accelerate(-200)

print(f"Final speed after emergency brake: {my_car.current_speed} km/h")
