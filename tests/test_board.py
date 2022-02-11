import unittest
from snake_ladder.board import Board

class TestBoard(unittest.TestCase):

    def test_add_snake(self):
        board = Board(100)
        self.assertEqual(board.game_objects, [])
        board.add_snake(55, 11)
        self.assertEqual(len(board.game_objects), 1)

    def test_add_ladder(self):
        board = Board(100)
        self.assertEqual(board.game_objects, [])
        board.add_ladder(6, 11)
        self.assertEqual(len(board.game_objects), 1)

    def test_check_and_move_if_game_objects(self):
        board = Board(100)
        board.add_snake(55, 11)
        board.add_ladder(6, 12)
        self.assertEqual(board.check_and_move_if_game_objects(55), 11)
        self.assertEqual(board.check_and_move_if_game_objects(6), 12)

    def test_move_player(self):
        board = Board(100)
        board.add_snake(55, 11)
        board.add_ladder(6, 12)
        self.assertEqual(board.move_player(54, 1), 11)
        self.assertEqual(board.move_player(4, 2), 12)
        self.assertEqual(board.move_player(19, 1), 20)

    def test_is_last_positon(self):
        board = Board(100)
        self.assertEqual(board.is_last_position(100), True)
        self.assertEqual(board.is_last_position(98), False)


if __name__ == '__main__':
    unittest.main()
