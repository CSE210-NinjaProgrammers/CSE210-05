from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        left_player_score = cast.get_first_actor("left_player_score")
        right_player_score = cast.get_first_actor("right_player_score")
        left_player = cast.get_first_actor("left_player")
        right_player = cast.get_first_actor("right_player")
        left_player_segments = left_player.get_segments()
        right_player_segments = right_player.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(right_player)
        self._video_service.draw_actors(left_player_segments)
        self._video_service.draw_actors(right_player_segments)
        self._video_service.draw_actor(left_player_score)
        self._video_service.draw_actor(right_player_score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()