#This program shows the simulation of 5 balls bouncing under gravitational acceleration.
#It is also accompanied by eleastic collission with walls of the container.
#It is fun to watch.
import pygame, time, random
from rendering import Renderer
from ball import Ball

pygame.init()

# Setting screen size of pygame window to 800 by 600 pixels
screen = pygame.display.set_mode((800, 600))

# Adding title
pygame.display.set_caption('Ball Bounce Simulation')

# Initialize renderer
renderer = Renderer(screen, 'background-img.jpg', 'ball.png')

# List of balls created as objects
Ball_List = [Ball(renderer) for _ in range(5)]

# The main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.02)
    renderer.render_background()
    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()
    pygame.display.update()