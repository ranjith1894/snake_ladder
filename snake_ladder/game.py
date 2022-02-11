from snake_ladder.player import Player


class Game:
    """
        A class to represent a game.
        ...
        players : list
            list of players
        current_player : str
            current player
        board : object
            Board object
        dice: object
            Dice object
    """

    def __init__(self):
        self.players = []
        self.current_player = None
        self.board = None
        self.dice = None

    def next_player(self):
        """
        getting the next player from the queue
        :return: obj
        """
        if not self.current_player:
            self.current_player = self.players[0]
            return self.current_player
        index = self.players.index(self.current_player)
        if len(self.players)-1 == index:
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[index+1]
        return self.current_player

    def add_board(self, board):
        """
        initialize board to the game
        :param board:
        :return:
        """
        self.board = board

    def add_players(self, name):
        """
        add players to the game by name
        :param name:
        :return:
        """
        if name in self.players:
            print("Try with another name, name is already exists")
            raise Exception
        player = Player(name, 1)
        self.players.append(player)

    def add_dice(self, dice):
        """
        initialize dice to the the game
        :param dice:
        :return:
        """
        self.dice = dice

    def has_winner(self):
        """
        checking wheather game as winner
        :return: Boolean
        """
        if not self.current_player:
            return False
        return self.board.is_last_position(self.current_player.position)

    def play(self):
        """
        Here is the game is happening -> throwing dice and moving current player to position
        :return:
        """
        self.current_player = self.next_player()
        print(f"Current player {self.current_player.name} is currently at {self.current_player.position} position")
        number = self.dice.throw()
        next_position = self.board.move_player(self.current_player.position, number)
        self.current_player.position = next_position
        print(f"Position updated to {self.current_player.position} ")

