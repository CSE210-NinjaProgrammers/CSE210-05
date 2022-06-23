from game.casting.actor import Actor
import constants

# class Score(Actor):
#     """
#     A record of points made or lost. 
    
#     The responsibility of Score is to keep track of the points the player has earned by eating food.
#     It contains methods for adding and getting points. Client should use get_text() to get a string 
#     representation of the points earned.

#     Attributes:
#         _points (int): The points earned in the game.
#     """
#     def __init__(self):
#         super().__init__()
#         self._points = 3
#         self.set_color(constants.WHITE)
    
#     def get_points(self):
#         return self._points
     

#     def subtract_points(self):
#         """Adds the given points to the score's total points.
        
#         Args:
#             points (int): The points to add.
#         """
#         self._points -= 1


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.
    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self,position,player):
        super().__init__()
        self._position=position
        self._points = 3
        self.set_text(f"Player {player}: {self._points}")

    def get_points(self):
        return self._points

    def subtract_points(self, player):
        """Subtract the given points to the score's total points.
        
        Args:
            points (int): The points to subtract.
        """
        self._points -= 1
        self.set_text(f"Player {player}: {self._points}")
