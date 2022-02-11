import random


class Dice:
    """
    A class to represent a dice.

    no_of_faces : number
        no_of_faces
    """
    def __init__(self, no_of_faces):
        self.no_of_faces = no_of_faces


class NormalDice(Dice):
    """
    A sub class to represent a NormalDice.
    """
    def throw(self):
        """
        throw dice and get random  number
        :return: number
        """
        result = random.randint(1, self.no_of_faces)
        print(f"Dice thrown -> {result}")
        return result


class CrookedDice(Dice):
    """
    A sub class to represent a CrookedDice.
    """
    def throw(self):
        """
        throw dice and get random even number
        :return: number
        """
        result = random.randrange(2, self.no_of_faces+1, 2)
        print(f"Dice thrown -> {result}")
        return result
