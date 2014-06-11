import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement):
    IMAGE = "Cat"
    
    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        # else
        return None

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!" % (len(player.inventory)))


####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    # Initialize and register rock 1
    rock_positions = [(2, 1), (1, 2), (3, 2), (2, 3)]

    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    for rock in rocks:
        print rock

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

    GAME_BOARD.draw_msg("This game is wicked awesome.")
    # Add these lines
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)



def keyboard_handler():
    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"
    
    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER)


        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)





 
    # if KEYBOARD[key.UP]:
    #     GAME_BOARD.draw_msg("You pressed up")
    #     next_y = PLAYER.y - 1
    #     GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #     GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)

    # elif KEYBOARD[key.DOWN]:
    #     GAME_BOARD.draw_msg("You pressed down")
    #     next_y = PLAYER.y + 1
    #     GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #     GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)

    # elif KEYBOARD[key.LEFT]:
    #     GAME_BOARD.draw_msg("You pressed left")
    #     next_x = PLAYER.x - 1
    #     GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #     GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)

    # elif KEYBOARD[key.RIGHT]:
    #     GAME_BOARD.draw_msg("You pressed right")
    #     next_x = PLAYER.x + 1
    #     GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #     GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)

    # elif KEYBOARD[key.SPACE]:
    #     GAME_BOARD.erase_msg()



