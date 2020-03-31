'''
Game Class Script
'''
from .player import Player
from .board import Board
from .round import Round

class Game(object):

    def __init__(self, id, players):
        """
        init game with min of 2 player active
        :param id: int
        :param players: Player[]
        """
        self.id = id
        self.players = []
        self.words_used = []
        self.round = None
        self.board = None
        self.player_draw_ind = 0
        self.start_new_round()

    def start_new_round(self):
        """
        start new round of game (new word to guess)
        :return None
        """
        self.round = Round(
            self.get_word(), 
            self.players[self.player_draw_ind], 
            self.players)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.round.end_round("Round ended")
            self.end_game()
    
    def player_guess(self, player, guess):
        """
        makes the player guess the word
        :param player: Player
        :param guess: str
        :return: bool
        """
        pass

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

        """
        pass

    def update_board(self, x, y, color):
        pass

    def end_game(self):
        pass
    
    def get_word(self):
        """
        returns a word that has not yet been used
        :return str
        """
        # TODO: get a list of words
        pass