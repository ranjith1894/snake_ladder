import unittest
from snake_ladder.dice import NormalDice, CrookedDice


class TestDice(unittest.TestCase):

    def test_check_normal_dice(self):
        dice = NormalDice(6)
        self.assertLessEqual(dice.throw(), 6)
        dice = NormalDice(10)
        self.assertLessEqual(dice.throw(), 10)

    def test_check_crooked_dice(self):
        dice = CrookedDice(6)
        self.assertEqual(dice.throw()%2, 0)
        self.assertLessEqual(dice.throw(), 6)


if __name__ == '__main__':
    unittest.main()
