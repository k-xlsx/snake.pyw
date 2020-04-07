import pygame
import random


class Block:

    def __init__(self,
                 width: int, height: int,
                 x: int, y: int):
        self.width = width
        self.height = height

        self.x = x
        self.y = y


    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw_self(self, display, color: tuple):

        pygame.draw.rect(display, color, (self.x, self.y, self.width, self.height))


class Square(Block):
    def __init__(self,
                 sideLength,
                 x: int, y: int):
        super().__init__(sideLength, sideLength,
                         x, y)


class Snake:

    def __init__(self,
                 blockSize,
                 x: int, y: int,
                 direction: str='up',
                 initialLength: int=1):
        self.blockSize = blockSize
        self.blocks = [Square(blockSize, x, y)]
        self.head = self.blocks[0]
        for i in range(initialLength - 1):
            self.elongate()

        self.speed = blockSize
        self.direction = direction

    def __getitem__(self, key):
        return self.blocks[key]

    def __setitem__(self, key, value):
        self.blocks[key] = value

    def __delitem__(self, key):
        del self.blocks[key]

    def __len__(self):
        return len(self.blocks)


    def const_move(self,
                   displayWidth: int, displayHeight: int,
                   isClosed: bool):
        visibleDisplayWidth = displayWidth - self.head.width
        visibleDisplayHeight = displayHeight - self.head.height

        self._follow_self()

        if self.direction == 'down':
            self.head.y += self.speed

            if self.head.y > visibleDisplayHeight:
                if isClosed:
                    self.head.y -= self.speed
                else:
                    self.head.y = 0

        if self.direction == 'up':
            self.head.y -= self.speed

            if self.head.y < 0:
                if isClosed:
                    self.head.y += self.speed
                else:
                    self.head.y = visibleDisplayHeight

        if self.direction == 'right':
            self.head.x += self.speed

            if self.head.x > visibleDisplayWidth:
                if isClosed:
                    self.head.x -= self.speed
                else:
                    self.head.x = 0

        if self.direction == 'left':
            self.head.x -= self.speed

            if self.head.x < 0:
                if isClosed:
                    self.head.x += self.speed
                else:
                    self.head.x = visibleDisplayWidth

    def elongate(self):
        try:
            if self[-1].y == self[-2].y:
                x = self.blocks[-1].x + self.blockSize
                y = self.blocks[-1].y
            else:
                x = self.blocks[-1].x
                y = self.blocks[-1].y + self.blockSize
            y = self.blocks[-1].y
        except IndexError:
            x = self.blocks[-1].x + self.blockSize
            y = self.blocks[-1].y
        finally:
            self.blocks.append(Square(self.blockSize,
                                      x, y))

    def change_direction(self, newDirection: str):
        self.direction = newDirection

    def draw_snake(self, display,
                   headColor: tuple,
                   mainColor: tuple,
                   secondColor: tuple):
        i = 0
        for block in self.blocks:
            if i == 0:
                block.draw_self(display, headColor)
            elif i % 2 == 0:
                block.draw_self(display, mainColor)
            else:
                block.draw_self(display, secondColor)

            i += 1

    def is_eating(self, cherry) -> bool:
        if(self.head.x == cherry.x and
           self.head.y == cherry.y):
            return True
        else:
            return False

    def is_dead(self, isClosed: bool=False) -> bool:
        for i in range(1, len(self)):
            if(self[i].x == self.head.x and
               self[i].y == self.head.y):
                return True

        return False


    def _follow_self(self):
        for i in sorted(range(1, len(self)), reverse=True):
            try:
                self[i].move(self[i - 1].x, self[i - 1].y)
            except IndexError:
                break


class Cherry(Square):

    def rand_pos(self, snake: Snake,
                 displayWidth: int, displayHeight: int):
        snakeCoords = {(block.x, block.y)
                       for block in snake.blocks}

        validXs = tuple([x
                         for x in range(displayWidth - self.width)
                         if x % snake.blockSize == 0 and x])
        validYs = tuple([y
                         for y in range(displayHeight - self.height)
                         if y % snake.blockSize == 0])

        randomCoords = (random.choice(validXs), random.choice(validYs))
        while randomCoords in snakeCoords:
            randomCoords = (random.choice(validXs), random.choice(validYs))

        self.move(randomCoords[0], randomCoords[1])
