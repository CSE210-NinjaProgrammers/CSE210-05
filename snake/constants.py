from game.shared.color import Color
from game.shared.player_initial_information import PlayerInitialInformation


COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 10
FONT_SIZE = 15
CAPTION = "Snake"
SNAKE_LENGTH = 1
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)

LEFT_PLAYER: PlayerInitialInformation = {'color': RED, 'x_position': 200, 'y_position': 150}
RIGHT_PLAYER: PlayerInitialInformation = {'color': GREEN, 'x_position': 700, 'y_position': 150}