class Vehicle:

    speed = 50
    wheels = 4
    color = None
    sprite = None

    def Drive(self):
        print("This vehicle is driving with a speed of:", self.speed)

    def Color(self):
        print("This vehicle has", self.wheels, "wheels.")

class Ferrari(Vehicle):

    model = "458 Italia"
    topSpeed = 337

    def __init__(self):
        

