import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.player_initial_information import PlayerInitialInformation


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, initial_information: PlayerInitialInformation):
        super().__init__()
        self._segments = []
        self._body_color = initial_information["color"]
        self._prepare_body(initial_information["x_position"], initial_information["y_position"])

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._body_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, initial_position_x, initial_position_y):
        x = int(initial_position_x)
        y = int(initial_position_y)

        position = Point(x * constants.CELL_SIZE, y)
        velocity = Point(1 * constants.CELL_SIZE, 0)
        text = "8"
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(self._body_color)
        self._segments.append(segment)