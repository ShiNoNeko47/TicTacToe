class Player:
    number = 1
    def __init__(self, name):
        self.name = name

        if self.name == '':
            self.name = 'Player{0}'.format(Player.number)

        self.symbol = lambda : ('X' if Player.number % 2 else 'O')
        self.symbol = self.symbol()
        Player.number += 1
        self.points = 0

