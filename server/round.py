'''
Single Round Class Script
'''
import time as t
from _thread import start_new_thread
from .game import Game
from .chat import Chat

class Round(object):
    def __init__(self, word, player_drawing, players):
        """
        init object
        :param word: str
        :param player_drawing: Player
        :param players: Player[]
        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = {player:0 for player in players}
        self.time = 75
        self.players = players
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())
    
    def skip(self):
        """
        return true if round skipped threshold met
        :return Bool
        """
        self.skips += 1
        if self.skips > len(self.players) - 2:
            self.skips = 0
            return True
        
        return False


    def time_thread(self):
        """
        runs in thread to keep track of time
        :return None
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up!")
    
    def guess(self, player, wrd):
        """
        guessing check function
        :param player: Player
        :param wrd: str
        :return: bool
        """
        correct = wrd = self.word
        if correct:
            self.player_guessed.append(player)
            # TODO: implement scoring system

    def player_left(self, player):
        """
        removing player that lef from the list
        :param player: Player
        :return None
        """
        # TODO: might not work
        if player in self.player_scores:
            del self.player_scores[player]
        
        if player in self.player_guessed:
            self.player_guessed.remove(player)
        
        if player == self.player_drawing:
            self.end_round("Drawing player leaves")
    
    def end_round(self, msg):
        # TODO: implement end round functions
        pass


