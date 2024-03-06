

class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

# Main program
    new_car = Car("ABC-123", 142)
    print("Initial Speed:", new_car.current_speed)

    # Accelerate by +30 km/h
    new_car.accelerate(30)
    print("Speed after accelerating by +30 km/h:", new_car.current_speed)

    # Accelerate by +70 km/h
    new_car.accelerate(70)
    print("Speed after accelerating by +70 km/h:", new_car.current_speed)

    # Accelerate by +50 km/h
    new_car.accelerate(50)
    print("Speed after accelerating by +50 km/h:", new_car.current_speed)

    # Emergency brake: reduce speed by -200 km/h
    new_car.accelerate(-200)
    print("Speed after emergency brake (-200 km/h):", new_car.current_speed)