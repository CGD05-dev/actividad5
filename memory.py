"""David Antonio Zarate Villaseñor A01665896
Christopher Gordillo Dominguez A01666339"""
"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import * 
from turtle import *

from freegames import path

car = path('car.gif')
tiles = ['cat', 'dog', 'bird', 'fish', 'lion', 'tiger', 'bear', 'wolf',
         'fox', 'deer', 'horse', 'zebra', 'snake', 'frog', 'owl', 'bat',
         'rat', 'pig', 'cow', 'sheep', 'goat', 'duck', 'hen', 'rooster',
         'rabbit', 'mouse', 'elephant', 'giraffe', 'monkey', 'panda', 'kangaroo', 'koala'] * 2
state = {'mark': None}
hide = [True] * 64
state = {'mark': None, 'taps': 0}  # Contador de taps agregado

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    state['taps'] += 1


    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']


    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 15)
        color('black')
        write(tiles[mark],align ='center', font=('Arial', 25, 'normal'))

    # Display tap count
    up()
    goto(-180, 180)  # Position above the grid
    color('black')
    write(f"Taps: {state['taps']}", font=('Arial', 20, 'normal'))

    # Check if all tiles are revealed
    if all(not hidden for hidden in hide):
        goto(0, -120)  # Position below the grid
        write("You Won!", align="center", font=('Arial', 30, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
