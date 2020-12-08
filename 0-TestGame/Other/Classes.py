
class Mario :

    _lives = 3
    _speed = 30.0

    def Test(self):
        print("hallo")

InstanceMario = Mario()
print(InstanceMario._lives)

print(InstanceMario._speed)
InstanceMario._speed = 50.0
print(InstanceMario._speed)
InstanceMario.Test()
