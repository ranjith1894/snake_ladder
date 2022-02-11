import unittest
from snake_ladder.game_objects import Snake, Ladder


class TestGameObjects(unittest.TestCase):

    def test_create_valid_snake(self):
        self.assertIsInstance(Snake(11, 3), Snake)
        self.assertIsInstance(Snake(45, 34), Snake)
        self.assertIsInstance(Snake(55, 10), Snake)

    def test_create_valid_ladder(self):
        self.assertIsInstance(Ladder(11, 33), Ladder)
        self.assertIsInstance(Ladder(15, 34), Ladder)
        self.assertIsInstance(Ladder(5, 10), Ladder)

    def test_invalid_ladder(self):
        self.assertRaises(Exception, Ladder(99, 33))
        self.assertRaises(Exception, Ladder(10, 5))
        self.assertRaises(Exception, Ladder(83, 33))

    def test_invalid_snake(self):
        self.assertRaises(Exception, Snake(10, 33))
        self.assertRaises(Exception, Snake(2, 5))
        self.assertRaises(Exception, Snake(1, 33))


if __name__ == '__main__':
    unittest.main()
