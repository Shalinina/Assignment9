class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_in_speed):
        new_speed = self.current_speed + change_in_speed
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

    def drive(self, no_of_hours):
        self.travelled_distance += self.current_speed * no_of_hours


new_car = Car("ABC-123", 142)
print("Properties of New Car are as below:\n")
print("The registration Number of New Car is: " + new_car.reg_number + "\nMaximum Speed of the Car is: "
      + str(new_car.max_speed) + "\nThe default Current Speed of car is: " + str(new_car.current_speed)
      + "\nThe default travelled_Distance is: " + str(new_car.travelled_distance))
new_car.accelerate(30)
print("After increase the speed of car by 30 km/h:\n The new current seed is: ", new_car.current_speed)
new_car.accelerate(70)
print("After increase Speed of car by 70 km/h:\n The New current speed is:", new_car.current_speed)
new_car.accelerate(50)
print("After increase the speed of car by 50 km/h:\n The new Current speed is :", new_car.current_speed)
new_car.drive(2)
print("After driving for 2 hours:\n The new travelled distance is:", new_car.travelled_distance)
new_car.accelerate(-200)
print("Use the emergency brake by forcing a -200 km/h:\n The new Current speed equals to 0:", new_car.current_speed)
