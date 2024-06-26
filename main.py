from numpy import array, ndarray
from vector import Vector
from particle import Particle
import pygame
from pygame.locals import RESIZABLE
pygame.init()


# Create a display surface object
screen = pygame.display.set_mode((800, 600), RESIZABLE)
w, h = pygame.display.get_surface().get_size()
width_center = int(w / 2)
height_center = int(h / 2)
position_of_zero = [width_center, height_center]
scaling = 100

# Title and icon
pygame.display.set_caption("Coulomb Simulation")
my_font = pygame.font.SysFont('Arial', 30)

# Particles
# q1 = Particle(0.01, 1, Vector(-3, 0), velocity=Vector(20, 0))
# q2 = Particle(0.01, 1, Vector(-3, 0), velocity=Vector(15, 0))
# q3 = Particle(0.01, 1, Vector(-3, 0), velocity=Vector(25, 0))

qs = [Particle(0.01, 1, Vector(-3, 0), velocity=Vector(20, 0)),
      Particle(0.01, 1, Vector(-3, 0),velocity=Vector(15, 0)),
      Particle(0.01, 1, Vector(-3, 0), velocity=Vector(25, 0)),
      Particle(0.01, 1, Vector(-3, 0), velocity=Vector(22, 0)),
      Particle(0.01, 1, Vector(-3, 0), velocity=Vector(17, 0)),
      Particle(0.01, 1, Vector(-3, 0), velocity=Vector(30, 0))]

# menu shit
mouse_down = False
previous_mouse_pos = [-1, -1]

clock = pygame.time.Clock()


def draw_vertical_line(screen, width, x):
    pygame.draw.line(screen, (0, 0, 0), (x, 0), (
        x, pygame.display.get_surface().get_size()[1]), width)


def draw_horizontal_line(screen, width, y):
    pygame.draw.line(screen, (0, 0, 0), (0, y), (
        pygame.display.get_surface().get_size()[0], y), width)


def draw_grid(screen):
    draw_vertical_line(screen, 3, position_of_zero[0])
    draw_horizontal_line(screen, 3, position_of_zero[1])


running = True

while running:
    # clock.tick(100)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                scaling += 1
            elif event.button == 5 and scaling != 1:
                scaling -= 1
            else:
                mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            previous_mouse_pos = [-1, -1]

    if mouse_down:
        if previous_mouse_pos != [-1, -1]:
            position_of_zero[0] += (pygame.mouse.get_pos()
                                    [0]-previous_mouse_pos[0])
            position_of_zero[1] += (pygame.mouse.get_pos()
                                    [1]-previous_mouse_pos[1])
        previous_mouse_pos = pygame.mouse.get_pos()

    # pygame.draw.circle(screen, (0, 0, 0),
    #                    position_of_zero, 10)

    # draw_grid(screen)

    pygame.draw.line(screen, (0, 0, 0), (0, 300), (1000, 300), 1)

    for q in qs:
        q.move()
        pygame.draw.circle(screen, (0, 0, 0),
                           (400+100*q.pos.x, 300+100*q.pos.y), 10)

    # q1.move()
    # q2.move()
    # q3.move()
    # pygame.draw.circle(screen, (0, 0, 0),
    #                    (400+100*q1.pos.x, 300+100*q1.pos.y), 10)
    # pygame.draw.circle(screen, (0, 0, 0),
    #                    (400+100*q2.pos.x, 300+100*q2.pos.y), 10)
    # pygame.draw.circle(screen, (0, 0, 0),
    #                    (400+100*q3.pos.x, 300+100*q3.pos.y), 10)
    pygame.display.update()

pygame.quit()
