"""
Obligatory snake made in python
Specific options can be seen or modified in the options.json file
"""

import pygame
import options
from screens import game_screen


if __name__ == '__main__':
    pygame.init()

    resolution = options.resolutions['average']

    # setting up the window
    display = pygame.display.set_mode(resolution)
    pygame.display.set_icon(options.icon)
    pygame.display.set_caption('snake.pyw')

    game_screen(display, options.screenTypes['open'])

    pygame.quit()
