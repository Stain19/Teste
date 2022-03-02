from turtle import *


def figura(n, side):
    """
    Drawn a square
    """
    angle = 360 / n
    ride_and_turn(side, angle, n)


def ride_and_turn(side, angle, n=1):
    if n == 1:
        forward(side)
        left(angle)
    elif n > 1:
        forward(side)
        left(angle)
        ride_and_turn(side, angle, n -1)
figura(3,100)
figura(4,100)
figura(5,100)
figura(6,100)
done()