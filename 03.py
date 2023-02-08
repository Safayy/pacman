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

class GameObject:
    pass

class Wall(GameObject):
    pass

class GameRenderer:
    pass

class MovableObject(GameObject):
    pass


class Hero(MovableObject):
    pass


class Ghost(MovableObject):
    pass


class Cookie(GameObject):
    pass

class Powerup(GameObject):
    pass

class Pathfinder:
    pass

class PacmanGameController:
    pass

if __name__ == "__main__":
    print("Starting game")