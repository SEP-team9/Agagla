import pygame
import time
from agagla import shared_objects
from random import seed, randint
from random import random

NUM_STARS = 100

seed(544354)


class Star:

    def __init__(self, position):
        self.position = position
        self.last_tick = time.time()

    def rand_float(self, minimum, maximum):
        return minimum + (random() * (maximum - minimum))

    def randomize(self, first_render):
        self.radius = randint(2, 6)
        if first_render:
            self.brightness = randint(0, 255)
        else:
            self.brightness = 0
        self.dimming = self.brightness >= 255
        self.step_time = randint(25, 100) * 1_000_000
        self.speed = 0.10
        self.velocity = pygame.Vector2(self.rand_float(-self.speed, self.speed),
                                       self.rand_float(-self.speed, self.speed))

    def tick(self):
        curr_time = time.time_ns()
        if curr_time - self.last_tick < self.step_time: return
        self.last_tick = curr_time
        # Since these are so small and so simple any sort of movement looks terrible so I disabled it.
        # self.position += self.velocity
        if self.dimming:
            self.brightness -= 1
        else:
            self.brightness += 1
            if self.brightness >= 255: self.dimming = True

    def is_dead(self):
        return self.brightness <= -1 and self.dimming

    def draw(self, screen):
        # def draw_point(relative_x, relative_y):
        #     our_x = int(self.position.x + relative_x)
        #     our_y = int(self.position.y + relative_y)
        #     if our_x < 0 or our_y < 0 or our_x > shared_objects.get_window_width() or our_y > shared_objects.get_window_height(): return
        #     pixel_brightness = self.brightness - (abs(relative_x) * 50) - (abs(relative_y) * 50)
        #     if pixel_brightness <= 0: return
        #     screen.set_at((our_x, our_y), (int(pixel_brightness), int(pixel_brightness), int(pixel_brightness)))
        #
        # draw_point(0, 0)
        # for i in range(-self.radius, self.radius + 1):
        #     draw_point(i, 0)
        #     draw_point(0, i)
        #     draw_point(i, i)
        #     draw_point(-i, i)
        #     draw_point(i, -i)
        color = (255, 255, 255)
        pygame.draw.rect(screen, color, pygame.Rect(self.position.x, self.position.y, self.radius, self.radius))


class Background:

    def __init__(self):
        self.stars = [None for y in range(NUM_STARS + 1)]
        self.first_render = True
        self.last_time = 0
        self.blink = False
        self.gsm = shared_objects.get_gsm()

    def render(self):
        for i in range(0, NUM_STARS):
            current = self.stars[i]
            if current is None or current.is_dead():
                current = Star(pygame.Vector2(randint(0, shared_objects.get_window_width()),
                                              randint(0, shared_objects.get_window_height())))
                current.randomize(self.first_render)
                self.stars[i] = current
            else:
                current.tick()
                current.draw(pygame.display.get_surface())

        self.first_render = False
        return None
