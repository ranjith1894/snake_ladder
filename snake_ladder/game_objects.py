
class GameObjects:
    """
    A class to represent a GameObjects.

    start: int
        starting position of snake/ladder
    end: int
        ending position of snake/ladder
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def next_position(self):
        """
        getting next position
        :return:
        """
        return self.end


class Snake(GameObjects):
    def create(self):
        """
        creating of a new snake
        :return:
        """
        if self.start < self.end:
            raise ValueError("Invalid snake")
        return self


class Ladder(GameObjects):
    def create(self):
        """
        creating of a new ladder
        :return:
        """
        if self.end < self.start:
            raise ValueError("Invalid Ladder")
        return self
