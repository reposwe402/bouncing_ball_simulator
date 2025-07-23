import pygame

class Renderer:
    def __init__(self, screen, background_image_path, ball_image_path):
        self.screen = screen
        self.background = pygame.image.load(background_image_path)
        self.ball_image = pygame.image.load(ball_image_path)

    def render_background(self):
        self.screen.blit(self.background, (0, 0))

    def render_ball(self, X, Y):
        self.screen.blit(self.ball_image, (X, Y))
