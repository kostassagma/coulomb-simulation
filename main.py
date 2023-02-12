from numpy import array, ndarray
from vector import Vector
from particle import Particle
import pygame
from pygame.locals import RESIZABLE
pygame.init()


# Create a display surface object
screen = pygame.display.set_mode((800, 600), RESIZABLE)

# Title and icon
pygame.display.set_caption("Coulomb Simulation")

# Particles
q1 = Particle(0.01, 1, Vector(-3, 0), velocity=Vector(10, 0))
q2 = Particle(0.001, 2, Vector(0, 1))
q3 = Particle(0.001, 2, Vector(0, -1))

clock = pygame.time.Clock()

running = True

while running:
    # clock.tick(100)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    q1.move()
    q2.move()
    q3.move()
    pygame.draw.circle(screen, (0, 0, 0),
                       (400+100*q1.pos.x, 300+100*q1.pos.y), 10)
    pygame.draw.circle(screen, (0, 0, 0),
                       (400+100*q2.pos.x, 300+100*q2.pos.y), 10)
    pygame.draw.circle(screen, (0, 0, 0),
                       (400+100*q3.pos.x, 300+100*q3.pos.y), 10)
    pygame.display.update()

pygame.quit()
