'''
Player Class Script
'''

class Player(object):
    # init function, for Player class we store ip, name and score
    def __init__(self, ip, name, score):
        self.ip = ip
        self.name = name
        self.score = score
    
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