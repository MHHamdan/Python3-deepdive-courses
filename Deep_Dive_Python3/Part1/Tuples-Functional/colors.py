from random import randint, random 
from collections import namedtuple

Color = namedtuple('Color', ' red green blue alpha ')

def random_color():
    red = blue = green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, blue, green, alpha)