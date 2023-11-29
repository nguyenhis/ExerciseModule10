#1
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"Moving up from {self.current} to {self.current + 1}")
            self.current += 1
            return True
        else:
            return False
    def floor_down(self):
        if self.current > self.bottom:
            print(f"Moving down from {self.current} to {self.current - 1}")
            self.current -= 1
            return True
        else:
            return False
    def go_to_floor(self, floor):
        if floor > self.current:
            for n in range(floor-self.current):
                self.floor_up()
        elif floor < self.current:
            for n in range(self.current - floor):
                self.floor_down()
        else:
            print(f"We are currently on the floor {self.current}.")

#h = Elevator(1, 6)
#target_floor = int(input("To what floor you want to go? "))
#h.go_to_floor(target_floor)
#h.go_to_floor(1)
#2
class Building:
    def __init__(self, bottom, top, elevators):
        self.elevators = []
        for n in range(elevators):
            self.elevators.append(Elevator(bottom,top))

    def run_elevator(self, elevator, floor):
        print(f"Moving elevator {elevator}: ")
        self.elevators[elevator - 1].go_to_floor(floor)
#3
    def fire_alarm(self):
        print("Fire alarm!")
        for e in self.elevators:
            e.go_to_floor(e.bottom)

building = Building(1, 6 ,3)
building.run_elevator(1,6 )
building.run_elevator(3,2)
building.run_elevator(2, 3)
building.run_elevator(1,3)
building.fire_alarm()

#4
import random

class Car:
    def __init__(self, regPlate, maxSpeed):
        self.regPlate = regPlate
        self.maxSpeed = maxSpeed
        self.speed = 0
        self.odometer = 0

    def accelerate(self, acceleration):
        self.speed = min(max(self.speed + acceleration, 0), self.maxSpeed)

    def drive(self, time):
        self.odometer += self.speed * time

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print("-------------------------------")
        for car in self.cars:
            print(f"{car.regPlate}: Max Speed - {car.maxSpeed} km/h, Odometer - {car.odometer} km")
        print("-------------------------------")

    def race_finished(self):
        for car in self.cars:
            if car.odometer >= self.distance:
                return True
        return False

Porsche = Car("ABC-313", 240)

print(f"Register plate {Porsche.regPlate}, Max speed {Porsche.maxSpeed} km/h, "
      f"Current Speed {Porsche.speed} km/h, Odometer {Porsche.odometer} km.")

Porsche.accelerate(30)
Porsche.accelerate(70)
Porsche.accelerate(50)
print(f"Current Speed is {Porsche.speed} km/h.")
Porsche.accelerate(-200)
print(f"Current Speed is {Porsche.speed} km/h.")

Porsche.accelerate(60)
Porsche.drive(1.5)
print(f"Distance Travelled: {Porsche.odometer} km.")


cars = [Car("ABC-" + str(i + 1), random.randint(100, 200)) for i in range(10)]


grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not grand_demolition_derby.race_finished():
    if hours % 10 == 0:
        grand_demolition_derby.print_status()
    grand_demolition_derby.hour_passes()
    hours += 1

grand_demolition_derby.print_status()
print("Race finished in", hours, "hours.")

