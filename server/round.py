'''
Single Round Class Script
'''

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
        self.time = 0
    
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
            self.end_round()
    
    def end_round(self):
        # TODO: implement end round functions
        pass


