import pygame

def draw(window, symbol, coordinates, color):
    if symbol == 'X':
        pygame.draw.line(window, color, (coordinates[0]-75,coordinates[1]-75), (coordinates[0]+75, coordinates[1]+75))
        pygame.draw.line(window, color, (coordinates[0]+75,coordinates[1]-75), (coordinates[0]-75, coordinates[1]+75))

    if symbol == 'O':
        pygame.draw.circle(window, color, coordinates, 75, 1)


