import pygame

class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.colors = [pygame.Color('white'), pygame.Color('black'), pygame.Color('red'), pygame.Color('blue')]
        self.current_color = 0
        self.update_screen()

    def next_color(self):
        self.current_color = (self.current_color + 1) % len(self.colors)
        self.update_screen()

    def update_screen(self):
        self.screen.fill(self.colors[self.current_color])