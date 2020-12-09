class Vehicle:

    speed = 0
    wheels = 4
    color = None
    sprite = None

    def Drive(self):
        # DEZE FUNCTIE WORDT IN FERRARI() OVERSCHREVEN
        print("This vehicle is driving at a speed of:", self.speed, "KM/H.\n")

    def Color(self):
        # OP DEZE FUNCTIE WORDT IN FERRARI() VOORTGEBOUWD
        print("The color value of this vehicle is:", self.color)

class Ferrari(Vehicle): # (VEHICLE) WANT HIJ ERFT ALLES VAN VEHICLE

    # NIEUWE VARIABELEN VAN FERRARI()
    model = "458 Italia"
    topSpeed = 337

    def __init__(self):
        
        self.color = "Yellow"
        self.speed = 120

    def Drive(self):
        print("This Ferrari is driving at a speed of:", self.speed, "KM/H.\n")

    def Color(self):
        super().Color()
        self.color = "Red"
        print("Changing the color to Red... the new color is:", self.color)

Up = Vehicle()

Italia = Ferrari()

Up.Color() # WORDT IN CLASS B AANGEVULD
Up.Drive() # WORDT IN CLASS B OVERSCHREVEN

Italia.Color() # WORDT HIER AANGEVULD
Italia.Drive() # WORDT HIER OVERSCHREVEN

    
        
