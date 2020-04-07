import pygame
from gameobjects import Snake


def snake_key_down_events(snake: Snake, keyDownEvent):
    if(keyDownEvent.key == pygame.K_DOWN and
       snake.direction != 'up'):
        snake.change_direction('down')

    elif(keyDownEvent.key == pygame.K_UP and
         snake.direction != 'down'):
        snake.change_direction('up')

    elif(keyDownEvent.key == pygame.K_RIGHT and
         snake.direction != 'left'):
        snake.change_direction('right')

    elif(keyDownEvent.key == pygame.K_LEFT and
         snake.direction != 'right'):
        snake.change_direction('left')
