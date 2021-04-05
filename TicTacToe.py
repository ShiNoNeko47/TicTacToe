#!/usr/bin/python

import pygame

class player:
    number = 1
    def __init__(self, name):
        self.name = name

        if self.name == '':
            self.name = 'Player{0}'.format(player.number)

        self.symbol = lambda : ('X' if player.number % 2 else 'O')
        self.symbol = self.symbol()
        player.number += 1
        self.points = 0

def output(field):
    for row in field:
        line = ''

        for column in row:
            line += column

        print(line)

def draw(window, symbol, coordinates, color):
    if symbol == 'X':
        pygame.draw.line(window, color, (coordinates[0]-75,coordinates[1]-75), (coordinates[0]+75, coordinates[1]+75))
        pygame.draw.line(window, color, (coordinates[0]+75,coordinates[1]-75), (coordinates[0]-75, coordinates[1]+75))

    if symbol == 'O':
        pygame.draw.circle(window, color, coordinates, 75, 1)

def check_field(field):
    for i in range(3):
        if all(field[i][0] == j for j in (field[i][1], field[i][2])):
            if field[i][0] != ' ':
                return True

        if all(field[0][i] == j for j in (field[1][i], field[2][i])):
            if field[0][i] != ' ':
                return True

    if all(field[0][0] == j for j in (field[1][1], field[2][2])):
        if field[0][0] != ' ':
            return True

    if all(field[2][0] == j for j in (field[1][1], field[0][2])):
        if field[2][0] != ' ':
            return True

    return False

def main(game_counter, players):

    field = [
            list('   '),
            list('   '),
            list('   ')
            ]

    current_player = 0

    pygame.init()

    window = pygame.display.set_mode((600, 600))

    color = (255, 255, 255)

    playing = True
    while playing:

        pygame.draw.line(window, color, (200, 0), (200, 600))
        pygame.draw.line(window, color, (400, 0), (400, 600))
        pygame.draw.line(window, color, (0, 200), (600, 200))
        pygame.draw.line(window, color, (0, 400), (600, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                global loop
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinateX = int(event.pos[0]/200)
                coordinateY = int(event.pos[1]/200)

                if field[coordinateY][coordinateX] == ' ':
                    draw(window, players[current_player].symbol, event.pos, color)
                    field[coordinateY][coordinateX] = players[current_player].symbol

                    if check_field(field):
                        output(field)
                        print('{0} wins\n'.format(players[current_player].name))
                        playing = False

                    current_player = (current_player+1)%2

        if playing:
            playing = False
            for row in field:
                if ' ' in row:
                    playing = True

        pygame.display.update()

if __name__ == '__main__':
    p1 = player(input())
    p2 = player(input())
    players = [p1, p2]
    loop = True
    game_counter = 0

    while loop:
        main(game_counter, players)
        game_counter += 1

