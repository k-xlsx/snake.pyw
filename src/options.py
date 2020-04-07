import pygame
import json
import os


def get_options() -> list:
    optionsPath = os.path.abspath(os.path.dirname(__file__))[:-3] + r'\assets\options.json'
    iconPath = os.path.abspath(os.path.dirname(__file__))[:-3] + r'\assets\snakeicon.ico'

    try:
        with open(optionsPath, 'r') as optionsFile:
            options = json.load(optionsFile)

        options['icon'] = pygame.image.load(iconPath)
        return options
    except FileNotFoundError:
        raise FileNotFoundError('options.json not found in the assets folder')


__options = get_options()

colors = __options['colors']
resolutions = __options['resolutions']
screenTypes = __options['screenTypes']
icon = __options['icon']
