'''
Player Class Script
'''
from .game import Game

class Player(object):
    # init function, for Player class we store ip, name and score
    def __init__(self, ip, name):
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0
    
    def update_score(self, x):
        self.score += x
    
    def guess(self, string):
        pass

    def disconnect(self):
        pass

    def get_ip(self):
        pass 

    def get_name(self):
        self.name

    def get_score(self):
        return self.score