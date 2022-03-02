import pyxel
import random
from math import sqrt

pyxel.init(160,120)

#Variables that start the circles

RADIUS = 5
COLOR_ACTIVE = pyxel.COLOR_RED
COLOR_SLEEP = pyxel.COLOR_PURPLE
STEP = 2
pyxel.game_over = False
pyxel.x1 = random.uniform(20,140)
pyxel.y1 = random.uniform(20,100)
pyxel.sleep1 = False
pyxel.x2 = random.uniform(20,140)
pyxel.y2 = random.uniform(20,100)
pyxel.sleep2 = False
pyxel.x3 = random.uniform(20,140)
pyxel.y3 = random.uniform(20,100)
pyxel.sleep3 = False

def start_game():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x1, pyxel.y1):
            pyxel.sleep1 = True
        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x2, pyxel.y2):
            pyxel.sleep2 = True
        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x3, pyxel.y3):
            pyxel.sleep3 = True

    if pyxel.frame_count > 30 * 5:
        pyxel.game_over = True
        pyxel.text(80, 60, "GAME OVER!", pyxel.COLOR_WHITE)
        
    if not pyxel.game_over:
        if not pyxel.sleep1:
           pyxel.x1 = pyxel.x1 + random.uniform( -STEP, STEP)
           pyxel.y1 = pyxel.y1 + random.uniform( -STEP, STEP)
        if not pyxel.sleep2:
           pyxel.x2 = pyxel.x2 + random.uniform( -STEP, STEP)
           pyxel.y2 = pyxel.y2 + random.uniform( -STEP, STEP)
        if not pyxel.sleep3:
           pyxel.x3 = pyxel.x3 + random.uniform( -STEP, STEP)
           pyxel.y3 = pyxel.y3 + random.uniform( -STEP, STEP)
def in_circle(x, y, cx, cy):
    """
    Checks if the point (x, y) is in the circle with radius  cx, cy
    """
    dist = sqrt((x - cx) ** 2 + (y - cy) ** 2)
    return dist <= RADIUS


def drawn():
    pyxel.cls(pyxel.COLOR_BLACK)
    if pyxel.sleep1:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x1, pyxel.y1, RADIUS, color)
    if pyxel.sleep2:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x2, pyxel.y2, RADIUS, color)
    if pyxel.sleep3:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x3, pyxel.y3, RADIUS, color)


pyxel.mouse(True)
pyxel.run(start_game, drawn)