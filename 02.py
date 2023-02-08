import pygame
import numpy as np
import tcod
import random
from enum import Enum

class Direction(Enum):
    DOWN = -90
    RIGHT = 0
    UP = 90
    LEFT = 180
    NONE = 360

class ScoreType(Enum):
    COOKIE = 10
    POWERUP = 50
    GHOST = 400


class GhostBehaviour(Enum):
    CHASE = 1
    SCATTER = 2

if __name__ == "__main__":
    print("Starting game")