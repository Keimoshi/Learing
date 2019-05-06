"""一个骰子的游戏"""
from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        num = randint(1, self.sides)
        print(num)
print("--------6面骰子--------")
for i in range(10):
    test_1 = Die()
    test_1.roll_die()

print("--------10面骰子--------")
for i in range(10):
    test_1 = Die(10)
    test_1.roll_die()

print("--------20面骰子--------")
for i in range(10):
    test_1 = Die(20)
    test_1.roll_die()