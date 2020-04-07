import pygame
import events
import options
from gameobjects import Snake, Cherry


def game_screen(display, isClosed: bool):
    displayWidth, displayHeight = display.get_size()


    clock = pygame.time.Clock()

    # game objects
    initX, initY = 260, 260
    snake = Snake(blockSize=20, x=initX, y=initY, direction='right')
    cherry = Cherry(sideLength=20, x=initX + 60, y=initY)

    # main loop
    RUN = True
    while RUN:
        # event loop
        moved = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break

            if(event.type == pygame.KEYDOWN) and not(moved):
                events.snake_key_down_events(snake, event)
                moved = True


        # snake movement and events
        snake.const_move(displayWidth, displayHeight, isClosed)
        if snake.is_dead():
            RUN = False
            isDead = True
        else:
            isDead = False

        if snake.is_eating(cherry):
            snake.elongate()
            cherry.rand_pos(snake, displayWidth, displayHeight)

        display.fill((0, 0, 0))
        draw_game_objects(display, snake, cherry, isDead)
        pygame.display.update()

        # framerate and delay
        clock.tick(60)
        delay = calculate_delay(snake)
        pygame.time.delay(delay)


def draw_game_objects(display, snake: Snake, cherry: Cherry, isDead: bool):
    if isDead:
        colorType = 'dead'
    else:
        colorType = 'snake'

    snake.draw_snake(display,
                     options.colors[colorType]['head'],
                     options.colors[colorType]['main'],
                     options.colors[colorType]['second'])
    cherry.draw_self(display, options.colors['cherry'])


def calculate_delay(snake: Snake) -> int:
    delay = 150 - len(snake) // 2
    if delay <= 60:
        delay = 60

    spacePressed = pygame.key.get_pressed()[pygame.K_SPACE]
    if spacePressed:
        return delay // 4
    else:
        return delay
