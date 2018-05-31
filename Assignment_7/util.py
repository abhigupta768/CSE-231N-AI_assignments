"""
util.py: Utility functions.
"""


from random import randint, random
from math import sqrt
from graph import *


def randomGridSearch(maxWidth, maxHeight):
    """
    Generate a random grid with obstacles, along with start and end points.
    """

    h = randint(maxHeight // 2, maxHeight)
    w = randint(maxWidth // 2, maxWidth)

    numOob = randint(1, round(sqrt(h * w)))

    oob = []
    size = sqrt((h * w) / numOob)

    for _ in range(numOob):
        x = round(random() * w)
        y = round(random() * h)
        a = round(random() * size)
        b = round(random() * size)
        oob.append(((x, y), (x + a, y + b)))

    g = Grid(w, h, oob)

    start = (randint(0, w - 1), randint(0, h - 1))

    while g.isOOB(start):
        start = (randint(0, w - 1), randint(0, h - 1))

    goal = (randint(0, w - 1), randint(0, h - 1))

    while g.isOOB(goal):
        goal = (randint(0, w - 1), randint(0, h - 1))

    return g, start, goal
