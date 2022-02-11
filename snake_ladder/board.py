from snake_ladder.game_objects import Snake, Ladder


class Board:
    """
    A class to represent a board.

    no_of_squares: int
        no of squares of board
    game_objects: list
        list of ladders or snakes in the board

    """
    def __init__(self, no_of_squares):
        self.no_of_squares = no_of_squares
        self.game_objects = []

    def add_snake(self, start, end):
        """
        add new snake to board
        :param start:
        :param end:
        :return:
        """
        snake = Snake(start, end).create()
        self.game_objects.append(snake)

    def add_ladder(self, start, end):
        """
        add new ladder to board
        :param start:
        :param end:
        :return:
        """
        ladder = Ladder(start, end).create()
        self.game_objects.append(ladder)

    def check_and_move_if_game_objects(self, position):
        """
        checking if any ladders or snakes at current position
        if exists move to the corresponding end

        :param position:
        :return: position
        """
        for game_object in self.game_objects:
            if position == game_object.start:
                print(f"Got a {type(game_object).__name__}")
                return game_object.next_position()
        return position

    def move_player(self, current_position, number):
        """
        moving the player to next based on dice number
        and if any game objects present move to its end position

        :param current_position:
        :param number:
        :return: next_position
        """
        next_position = current_position + number
        if next_position <= self.no_of_squares:
            next_position = self.check_and_move_if_game_objects(next_position)
        else:
            print("Exceeded the maximum position")
            return current_position
        return next_position

    def is_last_position(self, position):
        """
        checking wheather current position is end of the board
        :param position:
        :return:
        """
        if position == self.no_of_squares:
            return True
        return False
