from roboid import *

hamster = Hamster()

while True:
    hamster.wheels(50,50)
    if (hamster.left_proximity() > 50.0) or (hamster.right_proximity() > 50.0):
        hamster.leds("red")
        hamster.turn_left(1,30)