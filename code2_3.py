from math import *
result = pow(2, 10)
dist1 = sqrt(169)
print(result, "\\", dist1)


class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed

    def speedup(self):
        self.speed += 10

    def speeddown(self):
        self.speed -= 10

    def __eq__(self, carB):
        return self.color == carB.color

    def __str__(self):
        return "color = %s, speed = %d" % (self.color, self.speed)


car1 = Car("black", 10)
car2 = Car("red", 0)
car3 = Car("yellow", 20)
car4 = Car("blue", 30)
car5 = Car("green")
car6 = Car("white", 210)

car2.speedup()
car5.speedup()
car1.speeddown()

car1.color = "red"

print("car2==car6:", car2 == car6)
print("car1==car1:", car1 == car2)
print("[car3]", car3)


class SuperCar(Car):
    def __init__(self, color, speed=0, bTurbo=True):
        super().__init__(color, speed)
        self.bTurbo = bTurbo

    def set_bTurbo(self, bTurbo=True):
        self.bTurbo = bTurbo

    def speedup(self):
        if self.bTurbo == True:
            self.speed += 50
        else:
            super().speedup()

    def __str__(self):
        if self.bTurbo:
            return "[%s] [speed = %d] 터보모드" % (self.color, self.speed)
        else:
            return "[%s] [speed = %d] 일반모드" % (self.color, self.speed)


s1 = SuperCar("gold", 0, True)
s2 = SuperCar("silver", 0, False)

s1.speedup()
s2.speedup()

print("슈퍼카1:", s1)
print("슈퍼카2:", s2)
