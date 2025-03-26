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



car = Car("ABC-123", 142)
print(f"Registration Number: {car.registration_number}")
print(f"Maximum Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Travelled Distance: {car.travelled_distance} km")

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current Speed after acceleration: {car.current_speed} km/h")

car.accelerate(-200)
print(f"Final Speed after emergency brake: {car.current_speed} km/h")

car.drive(1.5)
print(f"Travelled Distance after 1.5 hours: {car.travelled_distance} km")




