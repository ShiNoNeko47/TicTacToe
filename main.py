#!/usr/bin/python

import pygame
from player import Player
from output import output
from draw import draw
from check_field import check_field

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
    p1 = Player(input())
    p2 = Player(input())
    players = [p1, p2]
    loop = True
    game_counter = 0

    while loop:
        main(game_counter, players)
        game_counter += 1

