'''
Game Class Script
'''
from .player import Player
from .board import Board
from .round import Round

class Game(object):

    def __init__(self, id, players, thread):
        """
        init game with min of 2 player active
        :param id: int
        :param players: Player[]
        :param thread: Thread
        """
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.connected_thread = thread
        self.start_new_round()

    def start_new_round(self):
        """
        start new round of game (new word to guess)
        :return None
        """
        self.round = Round(
            self.get_word(), 
            self.players[self.player_draw_ind], 
            self.players,
            self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.round.end_round("Round ended")
            self.end_game()
    
    # def create_board(self):
    #     """
    #     creats new board
    #     """
    #     self.board = Board()

    def player_guess(self, player, guess):
        """
        makes the player guess the word
        :param player: Player
        :param guess: str
        :return: bool
        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """
        call to clean up objects when player disconnects
        :param player: Player
        :raise Exception()
        """
        pass

    def skip(self):
        """
        increments the round skips, if skips are greater than threshold, starts
        new round
        :return None
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No roundstarted yet")
        pass

    def round_ended(self):
        """
        If the round ends call this
        :return None
        """
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):
        """
        calls update method on board
        :param x: int
        :param y: int
        :param color: (int, int, int)
        :return: None
        """
        if not self.board:
            raise Exception("No board created")
        self.board.update(x, y, color)

    def end_game(self):
        """
        ends the game
        :return:
        """
        # TODO: implement
        pass
    
    def get_word(self):
        """
        returns a word that has not yet been used
        :return str
        """
        # TODO: get a list of words
        pass