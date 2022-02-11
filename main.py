from snake_ladder.game import Game
from snake_ladder.dice import CrookedDice, NormalDice
from snake_ladder.board import Board

if __name__ == '__main__':
    dice_type = None
    while not dice_type:
        try:
            dice_type = int(input("Please select type of dice \n 1.Normal Dice, \n 2.Crooked Dice: \n"))
            if dice_type not in (1, 2):
                print("Invalid input please try again ")
        except ValueError:
            dice_type = None
            print("That's not an option!")

    if dice_type == 1:
        dice = NormalDice(6)
    else:
        dice = CrookedDice(6)
    no_of_squares = 100
    board = Board(no_of_squares)
    board.add_snake(14, 7)

    board.add_snake(88, 75)
    board.add_snake(33, 10)
    board.add_ladder(12, 99)
    board.add_ladder(22, 56)
    board.add_ladder(34, 54)

    game = Game()
    game.add_dice(dice)
    game.add_board(board)
    game.add_players('Ranjith')
    winner = False
    print("##### Game Started #####")
    for i in range(11):
        print(f"\n --------- Turn number {i} ---------")
        game.play()
        if game.has_winner():
            winner = True
            print(f"{game.current_player.name} has won the game !!!!!")
            break
    if not winner:
        print("\nSorry all the turns are over !!!!")
