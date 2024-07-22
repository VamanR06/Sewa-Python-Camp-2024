# Basic Drawing Pygame Functions
import pygame

# Draw Triangle Function
def draw_triangle(screen, center, length, color):
    x, y = center
    centroid = (3/4)**0.5 / length

    pygame.draw.polygon(screen, color, [
        (x, y - centroid),
        (x + length/2, y + (length - centroid)),
        (x - length/2, y + (length - centroid))
    ])

# Initialize Pygame
pygame.init()

# Screen variable to control components on screen
screen = pygame.display.set_mode([800, 600])

# Rect objects for shapes
box = pygame.Rect(350, 250, 100, 100)
window = pygame.Rect(390, 290, 20, 20)
ellipse = pygame.Rect(500, 400, 50, 20)

runGame = True

while runGame:
    # Event loop to check for any events (keypress, mouse, leaving game, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    # Draws rect object on screen
    pygame.draw.rect(screen, (0, 255, 255), box)
    pygame.draw.rect(screen, (255, 255, 0), window)
    pygame.draw.polygon(screen, (200, 20, 20), [(100, 100), (125, 130), (112, 200), (90, 225)])
    pygame.draw.circle(screen, (50, 75, 150), (600, 100), 50)
    pygame.draw.ellipse(screen, (200, 50, 200), ellipse)
    draw_triangle(screen, (200, 200), 100, (255, 255, 255))

    # Updates display
    pygame.display.update()
    
pygame.quit()

# Moving Objects
import pygame

pygame.init()

# Controls FPS
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 600])

box = pygame.Rect(100, 275, 50, 50)

# X Speed of box
box_velocity_x = 3

runGame = True

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    # Changes background color
    screen.fill((0, 0, 0))

    # Checks if box is touching the edges of screen
    if box.right >= screen.get_width() or box.left <= 0:
        box_velocity_x *= -1

    # Moves box based on velocity
    box.x += box_velocity_x

    pygame.draw.rect(screen, (20, 225, 200), box)

    pygame.display.update()

    # FPS
    clock.tick(60)
    
pygame.quit()

# Moving objects with keyboard
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 600])

box = pygame.Rect(100, 275, 50, 50)

box_velocity_x = 3

runGame = True

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

        # Key press events (if key pressed, move box)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box.x -= box_velocity_x

            elif event.key == pygame.K_RIGHT:
                box.x += box_velocity_x

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (20, 225, 200), box)

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
