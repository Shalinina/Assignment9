class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

new_car = Car("ABC-123", 142)
print("Properties of New Car are as below:\n")
print("The registration Number of New Car is: " + new_car.reg_number + "\nMaximum Speed of the Car is: "
      + str(new_car.max_speed) + "\nThe default Current Speed of car is: " + str(new_car.current_speed)
      + "\nThe default travelled_Distance is: " + str(new_car.travelled_distance))