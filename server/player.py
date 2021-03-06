'''
Player Class Script
'''
from .game import Game

class Player(object):
    # init function, for Player class we store ip, name and score
    def __init__(self, ip, name):
        """
        init the player object
        :param ip: str
        :param name: str
        """
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0
    
    def set_game(self, game):
        """
        sets the player-game association
        :param game: Game
        :return: None
        """
        self.game = game

    def update_score(self, x):
        """
        updates player score
        :param x: int
        :return: None
        """
        self.score += x
    
    def guess(self, wrd):
        """
        makes a player guess
        :param wrd: str
        :return: bool
        """
        return self.game.player_guess(self, wrd)

    def disconnect(self):
        """
        call to disconnect player
        :return:
        """
        pass

    def get_ip(self):
        """
        get player ip address
        :return: str
        """
        pass 

    def get_name(self):
        """
        return player name
        :return: str
        """
        self.name

    def get_score(self):
        """
        get player score
        :return: int
        """
        return self.score