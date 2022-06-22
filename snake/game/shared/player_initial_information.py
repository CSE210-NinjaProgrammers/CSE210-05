from typing import TypedDict
from game.shared.color import Color


class PlayerInitialInformation(TypedDict):
    color: Color
    x_position: int
    y_position: int