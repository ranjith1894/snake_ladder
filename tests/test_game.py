import unittest

from snake_ladder.board import Board
from snake_ladder.dice import NormalDice
from snake_ladder.game import Game
import unittest.mock as mock


def mock_choice(i, values):
    return 5


class TestGame(unittest.TestCase):

    def test_add_board(self):
        game = Game()
        board = Board(100)
        game.add_board(board)
        self.assertEqual(game.board, board)

    def test_add_players(self):
        game = Game()
        game.add_players('Tom')
        self.assertEqual(len(game.players), 1)

    def test_add_dice(self):
        game = Game()
        dice = NormalDice(6)
        game.add_dice(dice)
        self.assertEqual(game.dice, dice)

    def test_has_winner(self):
        game = Game()
        board = Board(100)
        game.add_board(board)
        game.add_players('Tom')
        game.next_player()
        game.current_player.position = 100
        self.assertEqual(game.has_winner(), True)
        game.current_player.position = 50
        self.assertEqual(game.has_winner(), False)

    def test_next_player(self):
        game = Game()
        game.add_players("Ranjith")
        game.add_players("Tom")
        game.add_players("Jack")
        self.assertEqual(game.next_player().name,  "Ranjith")
        self.assertEqual(game.next_player().name,  "Tom")
        self.assertEqual(game.next_player().name, "Jack")
        self.assertEqual(game.next_player().name, "Ranjith")

        game2 = Game()
        game2.add_players("Tom")
        self.assertEqual(game2.next_player().name, "Tom")
        self.assertEqual(game2.next_player().name, "Tom")

    def test_play(self):
        game = Game()
        game.add_players("Ranjith")
        board = Board(20)
        game.add_dice(NormalDice(6))
        game.add_board(board)
        game.next_player()
        self.assertEqual(game.current_player.position, 1)
        board.add_snake(14, 7)

        with mock.patch('random.randint', mock_choice):
            game.play()
            self.assertEqual(game.current_player.position, 6)

    def test_multiple_players(self):
        game = Game()
        game.add_players("Ranjith")
        game.add_players("Tom")
        board = Board(20)
        game.add_dice(NormalDice(6))
        game.add_board(board)
        game.next_player()
        self.assertEqual(game.current_player.name, "Ranjith")
        self.assertEqual(game.current_player.position, 1)
        with mock.patch('random.randint', mock_choice):
            game.play()
            self.assertEqual(game.current_player.position, 6)
            self.assertEqual(game.current_player.name, "Tom")
            game.play()
            self.assertEqual(game.current_player.position, 6)
            self.assertEqual(game.current_player.name, "Ranjith")


if __name__ == '__main__':
    unittest.main()
