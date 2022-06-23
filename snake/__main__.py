import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.cycle import Cycle
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("left_player", Snake(constants.LEFT_PLAYER))
    cast.add_actor("right_player", Snake(constants.RIGHT_PLAYER))
    cast.add_actor("left_player_score", Score(Point(0, 0),'one'))
    cast.add_actor("right_player_score", Score(Point(780, 0),'two'))
    # cast.add_actor("right_player_score", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service, "left_player"))
    script.add_action("input", ControlActorsAction(keyboard_service, "right_player"))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Cycle(video_service, keyboard_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()