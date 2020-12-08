class Character:

    speed = 10
    points = 0
    sprite = None

    def __init__(self):
        print("The constructor of Character")

    def Walk(self):
        print("Character is going on walkies with speed:", self.speed)

class Mario(Character):

    lives = 3
    items = None

    def __init__(self):
        # Constructor of Character is expanded:
        super().__init__()

        # Mario's speed is higher by default:
        self.speed = 30

    # De Walk functie van character overschrijven:
    def Walk(self):
        print("Mario loopt heel anders maar wel met snelheid:", self.speed)

    def Jump(self):
        print("Mario is jumping!")

# Make instances:
characterA = Character()
marioX = Mario()

characterA.Walk()
marioX.Walk()
marioX.Jump()

print(characterA.speed)
print(marioX.speed)
print(marioX.lives)

# Console shows a memory-address. This is the location of the entire object.
print(marioX)