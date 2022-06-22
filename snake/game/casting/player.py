from game.casting.snake import Snake

class Player(Snake):
    def __init__(self, body_color, initial_position_x, initial_position_y):
        super().__init__()
        self._body_color = body_color
        self._prepare_body(initial_position_x, initial_position_y)
        